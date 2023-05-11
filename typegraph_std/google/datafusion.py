from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_datafusion() -> Import:
    datafusion = HTTPRuntime("https://datafusion.googleapis.com/")

    renames = {
        "ErrorResponse": "_datafusion_1_ErrorResponse",
        "CancelOperationRequestIn": "_datafusion_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datafusion_3_CancelOperationRequestOut",
        "TestIamPermissionsResponseIn": "_datafusion_4_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datafusion_5_TestIamPermissionsResponseOut",
        "EmptyIn": "_datafusion_6_EmptyIn",
        "EmptyOut": "_datafusion_7_EmptyOut",
        "LocationIn": "_datafusion_8_LocationIn",
        "LocationOut": "_datafusion_9_LocationOut",
        "ListAvailableVersionsResponseIn": "_datafusion_10_ListAvailableVersionsResponseIn",
        "ListAvailableVersionsResponseOut": "_datafusion_11_ListAvailableVersionsResponseOut",
        "ListLocationsResponseIn": "_datafusion_12_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datafusion_13_ListLocationsResponseOut",
        "CryptoKeyConfigIn": "_datafusion_14_CryptoKeyConfigIn",
        "CryptoKeyConfigOut": "_datafusion_15_CryptoKeyConfigOut",
        "AuditConfigIn": "_datafusion_16_AuditConfigIn",
        "AuditConfigOut": "_datafusion_17_AuditConfigOut",
        "EventPublishConfigIn": "_datafusion_18_EventPublishConfigIn",
        "EventPublishConfigOut": "_datafusion_19_EventPublishConfigOut",
        "TestIamPermissionsRequestIn": "_datafusion_20_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datafusion_21_TestIamPermissionsRequestOut",
        "NetworkConfigIn": "_datafusion_22_NetworkConfigIn",
        "NetworkConfigOut": "_datafusion_23_NetworkConfigOut",
        "OperationMetadataIn": "_datafusion_24_OperationMetadataIn",
        "OperationMetadataOut": "_datafusion_25_OperationMetadataOut",
        "ExprIn": "_datafusion_26_ExprIn",
        "ExprOut": "_datafusion_27_ExprOut",
        "PolicyIn": "_datafusion_28_PolicyIn",
        "PolicyOut": "_datafusion_29_PolicyOut",
        "ListDnsPeeringsResponseIn": "_datafusion_30_ListDnsPeeringsResponseIn",
        "ListDnsPeeringsResponseOut": "_datafusion_31_ListDnsPeeringsResponseOut",
        "VersionIn": "_datafusion_32_VersionIn",
        "VersionOut": "_datafusion_33_VersionOut",
        "RestartInstanceRequestIn": "_datafusion_34_RestartInstanceRequestIn",
        "RestartInstanceRequestOut": "_datafusion_35_RestartInstanceRequestOut",
        "AuditLogConfigIn": "_datafusion_36_AuditLogConfigIn",
        "AuditLogConfigOut": "_datafusion_37_AuditLogConfigOut",
        "ListOperationsResponseIn": "_datafusion_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datafusion_39_ListOperationsResponseOut",
        "SetIamPolicyRequestIn": "_datafusion_40_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datafusion_41_SetIamPolicyRequestOut",
        "OperationIn": "_datafusion_42_OperationIn",
        "OperationOut": "_datafusion_43_OperationOut",
        "StatusIn": "_datafusion_44_StatusIn",
        "StatusOut": "_datafusion_45_StatusOut",
        "AcceleratorIn": "_datafusion_46_AcceleratorIn",
        "AcceleratorOut": "_datafusion_47_AcceleratorOut",
        "InstanceIn": "_datafusion_48_InstanceIn",
        "InstanceOut": "_datafusion_49_InstanceOut",
        "BindingIn": "_datafusion_50_BindingIn",
        "BindingOut": "_datafusion_51_BindingOut",
        "DnsPeeringIn": "_datafusion_52_DnsPeeringIn",
        "DnsPeeringOut": "_datafusion_53_DnsPeeringOut",
        "ListInstancesResponseIn": "_datafusion_54_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_datafusion_55_ListInstancesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListAvailableVersionsResponseIn"] = t.struct(
        {
            "availableVersions": t.array(t.proxy(renames["VersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAvailableVersionsResponseIn"])
    types["ListAvailableVersionsResponseOut"] = t.struct(
        {
            "availableVersions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAvailableVersionsResponseOut"])
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
    types["CryptoKeyConfigIn"] = t.struct(
        {"keyReference": t.string().optional()}
    ).named(renames["CryptoKeyConfigIn"])
    types["CryptoKeyConfigOut"] = t.struct(
        {
            "keyReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyConfigOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["EventPublishConfigIn"] = t.struct(
        {"topic": t.string(), "enabled": t.boolean()}
    ).named(renames["EventPublishConfigIn"])
    types["EventPublishConfigOut"] = t.struct(
        {
            "topic": t.string(),
            "enabled": t.boolean(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventPublishConfigOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["NetworkConfigIn"] = t.struct(
        {"ipAllocation": t.string().optional(), "network": t.string().optional()}
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "ipAllocation": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListDnsPeeringsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dnsPeerings": t.array(t.proxy(renames["DnsPeeringIn"])).optional(),
        }
    ).named(renames["ListDnsPeeringsResponseIn"])
    types["ListDnsPeeringsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dnsPeerings": t.array(t.proxy(renames["DnsPeeringOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDnsPeeringsResponseOut"])
    types["VersionIn"] = t.struct(
        {
            "defaultVersion": t.boolean().optional(),
            "versionNumber": t.string().optional(),
            "availableFeatures": t.array(t.string()).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "defaultVersion": t.boolean().optional(),
            "versionNumber": t.string().optional(),
            "availableFeatures": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["RestartInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestartInstanceRequestIn"]
    )
    types["RestartInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartInstanceRequestOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AcceleratorIn"] = t.struct(
        {"state": t.string().optional(), "acceleratorType": t.string().optional()}
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "state": t.string().optional(),
            "acceleratorType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["InstanceIn"] = t.struct(
        {
            "privateInstance": t.boolean().optional(),
            "type": t.string(),
            "zone": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigIn"]).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "enableRbac": t.boolean().optional(),
            "enableZoneSeparation": t.boolean().optional(),
            "description": t.string().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "dataprocServiceAccount": t.string().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "version": t.string().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "privateInstance": t.boolean().optional(),
            "tenantProjectId": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "type": t.string(),
            "serviceEndpoint": t.string().optional(),
            "zone": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigOut"]).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "enableRbac": t.boolean().optional(),
            "enableZoneSeparation": t.boolean().optional(),
            "description": t.string().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "dataprocServiceAccount": t.string().optional(),
            "state": t.string().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "stateMessage": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "displayName": t.string().optional(),
            "disabledReason": t.array(t.string()).optional(),
            "availableVersion": t.array(t.proxy(renames["VersionOut"])).optional(),
            "apiEndpoint": t.string().optional(),
            "p4ServiceAccount": t.string().optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "gcsBucket": t.string().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["DnsPeeringIn"] = t.struct(
        {
            "targetNetwork": t.string().optional(),
            "targetProject": t.string().optional(),
            "domain": t.string(),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["DnsPeeringIn"])
    types["DnsPeeringOut"] = t.struct(
        {
            "targetNetwork": t.string().optional(),
            "targetProject": t.string().optional(),
            "domain": t.string(),
            "description": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsPeeringOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])

    functions = {}
    functions["projectsLocationsList"] = datafusion.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = datafusion.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVersionsList"] = datafusion.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "latestPatchOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesTestIamPermissions"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRestart"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetIamPolicy"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSetIamPolicy"] = datafusion.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsCreate"] = datafusion.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsList"] = datafusion.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsDelete"] = datafusion.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datafusion.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datafusion.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datafusion.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datafusion.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datafusion", renames=renames, types=types, functions=functions
    )
