from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_datafusion() -> Import:
    datafusion = HTTPRuntime("https://datafusion.googleapis.com/")

    renames = {
        "ErrorResponse": "_datafusion_1_ErrorResponse",
        "VersionIn": "_datafusion_2_VersionIn",
        "VersionOut": "_datafusion_3_VersionOut",
        "ListOperationsResponseIn": "_datafusion_4_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datafusion_5_ListOperationsResponseOut",
        "SetIamPolicyRequestIn": "_datafusion_6_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datafusion_7_SetIamPolicyRequestOut",
        "EventPublishConfigIn": "_datafusion_8_EventPublishConfigIn",
        "EventPublishConfigOut": "_datafusion_9_EventPublishConfigOut",
        "TestIamPermissionsResponseIn": "_datafusion_10_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datafusion_11_TestIamPermissionsResponseOut",
        "DnsPeeringIn": "_datafusion_12_DnsPeeringIn",
        "DnsPeeringOut": "_datafusion_13_DnsPeeringOut",
        "AuditConfigIn": "_datafusion_14_AuditConfigIn",
        "AuditConfigOut": "_datafusion_15_AuditConfigOut",
        "ExprIn": "_datafusion_16_ExprIn",
        "ExprOut": "_datafusion_17_ExprOut",
        "RestartInstanceRequestIn": "_datafusion_18_RestartInstanceRequestIn",
        "RestartInstanceRequestOut": "_datafusion_19_RestartInstanceRequestOut",
        "StatusIn": "_datafusion_20_StatusIn",
        "StatusOut": "_datafusion_21_StatusOut",
        "OperationIn": "_datafusion_22_OperationIn",
        "OperationOut": "_datafusion_23_OperationOut",
        "ListInstancesResponseIn": "_datafusion_24_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_datafusion_25_ListInstancesResponseOut",
        "CryptoKeyConfigIn": "_datafusion_26_CryptoKeyConfigIn",
        "CryptoKeyConfigOut": "_datafusion_27_CryptoKeyConfigOut",
        "ListLocationsResponseIn": "_datafusion_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datafusion_29_ListLocationsResponseOut",
        "CancelOperationRequestIn": "_datafusion_30_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datafusion_31_CancelOperationRequestOut",
        "TestIamPermissionsRequestIn": "_datafusion_32_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datafusion_33_TestIamPermissionsRequestOut",
        "EmptyIn": "_datafusion_34_EmptyIn",
        "EmptyOut": "_datafusion_35_EmptyOut",
        "PolicyIn": "_datafusion_36_PolicyIn",
        "PolicyOut": "_datafusion_37_PolicyOut",
        "AcceleratorIn": "_datafusion_38_AcceleratorIn",
        "AcceleratorOut": "_datafusion_39_AcceleratorOut",
        "OperationMetadataIn": "_datafusion_40_OperationMetadataIn",
        "OperationMetadataOut": "_datafusion_41_OperationMetadataOut",
        "ListAvailableVersionsResponseIn": "_datafusion_42_ListAvailableVersionsResponseIn",
        "ListAvailableVersionsResponseOut": "_datafusion_43_ListAvailableVersionsResponseOut",
        "LocationIn": "_datafusion_44_LocationIn",
        "LocationOut": "_datafusion_45_LocationOut",
        "BindingIn": "_datafusion_46_BindingIn",
        "BindingOut": "_datafusion_47_BindingOut",
        "AuditLogConfigIn": "_datafusion_48_AuditLogConfigIn",
        "AuditLogConfigOut": "_datafusion_49_AuditLogConfigOut",
        "InstanceIn": "_datafusion_50_InstanceIn",
        "InstanceOut": "_datafusion_51_InstanceOut",
        "ListDnsPeeringsResponseIn": "_datafusion_52_ListDnsPeeringsResponseIn",
        "ListDnsPeeringsResponseOut": "_datafusion_53_ListDnsPeeringsResponseOut",
        "NetworkConfigIn": "_datafusion_54_NetworkConfigIn",
        "NetworkConfigOut": "_datafusion_55_NetworkConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VersionIn"] = t.struct(
        {
            "availableFeatures": t.array(t.string()).optional(),
            "defaultVersion": t.boolean().optional(),
            "type": t.string().optional(),
            "versionNumber": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "availableFeatures": t.array(t.string()).optional(),
            "defaultVersion": t.boolean().optional(),
            "type": t.string().optional(),
            "versionNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["DnsPeeringIn"] = t.struct(
        {
            "targetNetwork": t.string().optional(),
            "targetProject": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "domain": t.string(),
        }
    ).named(renames["DnsPeeringIn"])
    types["DnsPeeringOut"] = t.struct(
        {
            "targetNetwork": t.string().optional(),
            "targetProject": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "domain": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsPeeringOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["RestartInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestartInstanceRequestIn"]
    )
    types["RestartInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartInstanceRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["CryptoKeyConfigIn"] = t.struct(
        {"keyReference": t.string().optional()}
    ).named(renames["CryptoKeyConfigIn"])
    types["CryptoKeyConfigOut"] = t.struct(
        {
            "keyReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyConfigOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "createTime": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListAvailableVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "availableVersions": t.array(t.proxy(renames["VersionIn"])).optional(),
        }
    ).named(renames["ListAvailableVersionsResponseIn"])
    types["ListAvailableVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "availableVersions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAvailableVersionsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["InstanceIn"] = t.struct(
        {
            "enableStackdriverMonitoring": t.boolean().optional(),
            "enableRbac": t.boolean().optional(),
            "dataprocServiceAccount": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigIn"]).optional(),
            "zone": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "type": t.string(),
            "enableZoneSeparation": t.boolean().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "privateInstance": t.boolean().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "enableStackdriverMonitoring": t.boolean().optional(),
            "enableRbac": t.boolean().optional(),
            "tenantProjectId": t.string().optional(),
            "dataprocServiceAccount": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "apiEndpoint": t.string().optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigOut"]).optional(),
            "serviceEndpoint": t.string().optional(),
            "availableVersion": t.array(t.proxy(renames["VersionOut"])).optional(),
            "zone": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "disabledReason": t.array(t.string()).optional(),
            "version": t.string().optional(),
            "type": t.string(),
            "enableZoneSeparation": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "p4ServiceAccount": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "gcsBucket": t.string().optional(),
            "privateInstance": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["ListDnsPeeringsResponseIn"] = t.struct(
        {
            "dnsPeerings": t.array(t.proxy(renames["DnsPeeringIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDnsPeeringsResponseIn"])
    types["ListDnsPeeringsResponseOut"] = t.struct(
        {
            "dnsPeerings": t.array(t.proxy(renames["DnsPeeringOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDnsPeeringsResponseOut"])
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
    functions["projectsLocationsOperationsCancel"] = datafusion.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datafusion.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datafusion.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datafusion.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVersionsList"] = datafusion.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "latestPatchOnly": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesTestIamPermissions"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSetIamPolicy"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRestart"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetIamPolicy"] = datafusion.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
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
    functions["projectsLocationsInstancesDnsPeeringsCreate"] = datafusion.delete(
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

    return Import(
        importer="datafusion",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
