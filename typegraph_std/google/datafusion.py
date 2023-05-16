from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_datafusion() -> Import:
    datafusion = HTTPRuntime("https://datafusion.googleapis.com/")

    renames = {
        "ErrorResponse": "_datafusion_1_ErrorResponse",
        "DnsPeeringIn": "_datafusion_2_DnsPeeringIn",
        "DnsPeeringOut": "_datafusion_3_DnsPeeringOut",
        "InstanceIn": "_datafusion_4_InstanceIn",
        "InstanceOut": "_datafusion_5_InstanceOut",
        "ExprIn": "_datafusion_6_ExprIn",
        "ExprOut": "_datafusion_7_ExprOut",
        "EmptyIn": "_datafusion_8_EmptyIn",
        "EmptyOut": "_datafusion_9_EmptyOut",
        "ListAvailableVersionsResponseIn": "_datafusion_10_ListAvailableVersionsResponseIn",
        "ListAvailableVersionsResponseOut": "_datafusion_11_ListAvailableVersionsResponseOut",
        "ListDnsPeeringsResponseIn": "_datafusion_12_ListDnsPeeringsResponseIn",
        "ListDnsPeeringsResponseOut": "_datafusion_13_ListDnsPeeringsResponseOut",
        "BindingIn": "_datafusion_14_BindingIn",
        "BindingOut": "_datafusion_15_BindingOut",
        "StatusIn": "_datafusion_16_StatusIn",
        "StatusOut": "_datafusion_17_StatusOut",
        "CancelOperationRequestIn": "_datafusion_18_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datafusion_19_CancelOperationRequestOut",
        "VersionIn": "_datafusion_20_VersionIn",
        "VersionOut": "_datafusion_21_VersionOut",
        "ListInstancesResponseIn": "_datafusion_22_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_datafusion_23_ListInstancesResponseOut",
        "SetIamPolicyRequestIn": "_datafusion_24_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datafusion_25_SetIamPolicyRequestOut",
        "OperationIn": "_datafusion_26_OperationIn",
        "OperationOut": "_datafusion_27_OperationOut",
        "NetworkConfigIn": "_datafusion_28_NetworkConfigIn",
        "NetworkConfigOut": "_datafusion_29_NetworkConfigOut",
        "PolicyIn": "_datafusion_30_PolicyIn",
        "PolicyOut": "_datafusion_31_PolicyOut",
        "TestIamPermissionsRequestIn": "_datafusion_32_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datafusion_33_TestIamPermissionsRequestOut",
        "AuditConfigIn": "_datafusion_34_AuditConfigIn",
        "AuditConfigOut": "_datafusion_35_AuditConfigOut",
        "CryptoKeyConfigIn": "_datafusion_36_CryptoKeyConfigIn",
        "CryptoKeyConfigOut": "_datafusion_37_CryptoKeyConfigOut",
        "LocationIn": "_datafusion_38_LocationIn",
        "LocationOut": "_datafusion_39_LocationOut",
        "AcceleratorIn": "_datafusion_40_AcceleratorIn",
        "AcceleratorOut": "_datafusion_41_AcceleratorOut",
        "ListOperationsResponseIn": "_datafusion_42_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datafusion_43_ListOperationsResponseOut",
        "RestartInstanceRequestIn": "_datafusion_44_RestartInstanceRequestIn",
        "RestartInstanceRequestOut": "_datafusion_45_RestartInstanceRequestOut",
        "ListLocationsResponseIn": "_datafusion_46_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datafusion_47_ListLocationsResponseOut",
        "OperationMetadataIn": "_datafusion_48_OperationMetadataIn",
        "OperationMetadataOut": "_datafusion_49_OperationMetadataOut",
        "AuditLogConfigIn": "_datafusion_50_AuditLogConfigIn",
        "AuditLogConfigOut": "_datafusion_51_AuditLogConfigOut",
        "EventPublishConfigIn": "_datafusion_52_EventPublishConfigIn",
        "EventPublishConfigOut": "_datafusion_53_EventPublishConfigOut",
        "TestIamPermissionsResponseIn": "_datafusion_54_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datafusion_55_TestIamPermissionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DnsPeeringIn"] = t.struct(
        {
            "targetNetwork": t.string().optional(),
            "description": t.string().optional(),
            "domain": t.string(),
            "targetProject": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["DnsPeeringIn"])
    types["DnsPeeringOut"] = t.struct(
        {
            "targetNetwork": t.string().optional(),
            "description": t.string().optional(),
            "domain": t.string(),
            "targetProject": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsPeeringOut"])
    types["InstanceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "enableRbac": t.boolean().optional(),
            "type": t.string(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "version": t.string().optional(),
            "zone": t.string().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigIn"]).optional(),
            "enableZoneSeparation": t.boolean().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "dataprocServiceAccount": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "privateInstance": t.boolean().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "stateMessage": t.string().optional(),
            "description": t.string().optional(),
            "enableRbac": t.boolean().optional(),
            "type": t.string(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "serviceEndpoint": t.string().optional(),
            "version": t.string().optional(),
            "apiEndpoint": t.string().optional(),
            "zone": t.string().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigOut"]).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "disabledReason": t.array(t.string()).optional(),
            "enableZoneSeparation": t.boolean().optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "dataprocServiceAccount": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gcsBucket": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "p4ServiceAccount": t.string().optional(),
            "availableVersion": t.array(t.proxy(renames["VersionOut"])).optional(),
            "displayName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "name": t.string().optional(),
            "privateInstance": t.boolean().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigOut"]).optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["VersionIn"] = t.struct(
        {
            "versionNumber": t.string().optional(),
            "defaultVersion": t.boolean().optional(),
            "type": t.string().optional(),
            "availableFeatures": t.array(t.string()).optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "versionNumber": t.string().optional(),
            "defaultVersion": t.boolean().optional(),
            "type": t.string().optional(),
            "availableFeatures": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
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
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["CryptoKeyConfigIn"] = t.struct(
        {"keyReference": t.string().optional()}
    ).named(renames["CryptoKeyConfigIn"])
    types["CryptoKeyConfigOut"] = t.struct(
        {
            "keyReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyConfigOut"])
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
    types["AcceleratorIn"] = t.struct(
        {"acceleratorType": t.string().optional(), "state": t.string().optional()}
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "acceleratorType": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
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
    types["RestartInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestartInstanceRequestIn"]
    )
    types["RestartInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartInstanceRequestOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "requestedCancellation": t.boolean().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["EventPublishConfigIn"] = t.struct(
        {"enabled": t.boolean(), "topic": t.string()}
    ).named(renames["EventPublishConfigIn"])
    types["EventPublishConfigOut"] = t.struct(
        {
            "enabled": t.boolean(),
            "topic": t.string(),
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
    functions["projectsLocationsOperationsCancel"] = datafusion.delete(
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "latestPatchOnly": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetIamPolicy"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRestart"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSetIamPolicy"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesTestIamPermissions"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = datafusion.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "enableRbac": t.boolean().optional(),
                "type": t.string(),
                "enableStackdriverMonitoring": t.boolean().optional(),
                "version": t.string().optional(),
                "zone": t.string().optional(),
                "options": t.struct({"_": t.string().optional()}).optional(),
                "eventPublishConfig": t.proxy(
                    renames["EventPublishConfigIn"]
                ).optional(),
                "enableZoneSeparation": t.boolean().optional(),
                "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
                "dataprocServiceAccount": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "privateInstance": t.boolean().optional(),
                "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
                "enableStackdriverLogging": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsCreate"] = datafusion.get(
        "v1/{parent}/dnsPeerings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDnsPeeringsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsDelete"] = datafusion.get(
        "v1/{parent}/dnsPeerings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDnsPeeringsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsList"] = datafusion.get(
        "v1/{parent}/dnsPeerings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDnsPeeringsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datafusion",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
