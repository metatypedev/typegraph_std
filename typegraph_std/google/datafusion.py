from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_datafusion():
    datafusion = HTTPRuntime("https://datafusion.googleapis.com/")

    renames = {
        "ErrorResponse": "_datafusion_1_ErrorResponse",
        "AuditLogConfigIn": "_datafusion_2_AuditLogConfigIn",
        "AuditLogConfigOut": "_datafusion_3_AuditLogConfigOut",
        "VersionIn": "_datafusion_4_VersionIn",
        "VersionOut": "_datafusion_5_VersionOut",
        "DnsPeeringIn": "_datafusion_6_DnsPeeringIn",
        "DnsPeeringOut": "_datafusion_7_DnsPeeringOut",
        "CancelOperationRequestIn": "_datafusion_8_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_datafusion_9_CancelOperationRequestOut",
        "ListLocationsResponseIn": "_datafusion_10_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_datafusion_11_ListLocationsResponseOut",
        "SetIamPolicyRequestIn": "_datafusion_12_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_datafusion_13_SetIamPolicyRequestOut",
        "OperationIn": "_datafusion_14_OperationIn",
        "OperationOut": "_datafusion_15_OperationOut",
        "ExprIn": "_datafusion_16_ExprIn",
        "ExprOut": "_datafusion_17_ExprOut",
        "CryptoKeyConfigIn": "_datafusion_18_CryptoKeyConfigIn",
        "CryptoKeyConfigOut": "_datafusion_19_CryptoKeyConfigOut",
        "ListOperationsResponseIn": "_datafusion_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_datafusion_21_ListOperationsResponseOut",
        "LocationIn": "_datafusion_22_LocationIn",
        "LocationOut": "_datafusion_23_LocationOut",
        "NetworkConfigIn": "_datafusion_24_NetworkConfigIn",
        "NetworkConfigOut": "_datafusion_25_NetworkConfigOut",
        "PolicyIn": "_datafusion_26_PolicyIn",
        "PolicyOut": "_datafusion_27_PolicyOut",
        "TestIamPermissionsRequestIn": "_datafusion_28_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_datafusion_29_TestIamPermissionsRequestOut",
        "OperationMetadataIn": "_datafusion_30_OperationMetadataIn",
        "OperationMetadataOut": "_datafusion_31_OperationMetadataOut",
        "ListInstancesResponseIn": "_datafusion_32_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_datafusion_33_ListInstancesResponseOut",
        "AcceleratorIn": "_datafusion_34_AcceleratorIn",
        "AcceleratorOut": "_datafusion_35_AcceleratorOut",
        "InstanceIn": "_datafusion_36_InstanceIn",
        "InstanceOut": "_datafusion_37_InstanceOut",
        "StatusIn": "_datafusion_38_StatusIn",
        "StatusOut": "_datafusion_39_StatusOut",
        "EmptyIn": "_datafusion_40_EmptyIn",
        "EmptyOut": "_datafusion_41_EmptyOut",
        "RestartInstanceRequestIn": "_datafusion_42_RestartInstanceRequestIn",
        "RestartInstanceRequestOut": "_datafusion_43_RestartInstanceRequestOut",
        "ListDnsPeeringsResponseIn": "_datafusion_44_ListDnsPeeringsResponseIn",
        "ListDnsPeeringsResponseOut": "_datafusion_45_ListDnsPeeringsResponseOut",
        "ListAvailableVersionsResponseIn": "_datafusion_46_ListAvailableVersionsResponseIn",
        "ListAvailableVersionsResponseOut": "_datafusion_47_ListAvailableVersionsResponseOut",
        "TestIamPermissionsResponseIn": "_datafusion_48_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_datafusion_49_TestIamPermissionsResponseOut",
        "EventPublishConfigIn": "_datafusion_50_EventPublishConfigIn",
        "EventPublishConfigOut": "_datafusion_51_EventPublishConfigOut",
        "AuditConfigIn": "_datafusion_52_AuditConfigIn",
        "AuditConfigOut": "_datafusion_53_AuditConfigOut",
        "BindingIn": "_datafusion_54_BindingIn",
        "BindingOut": "_datafusion_55_BindingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["VersionIn"] = t.struct(
        {
            "defaultVersion": t.boolean().optional(),
            "availableFeatures": t.array(t.string()).optional(),
            "versionNumber": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "defaultVersion": t.boolean().optional(),
            "availableFeatures": t.array(t.string()).optional(),
            "versionNumber": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["DnsPeeringIn"] = t.struct(
        {
            "domain": t.string(),
            "targetNetwork": t.string().optional(),
            "targetProject": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["DnsPeeringIn"])
    types["DnsPeeringOut"] = t.struct(
        {
            "domain": t.string(),
            "targetNetwork": t.string().optional(),
            "targetProject": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsPeeringOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["CryptoKeyConfigIn"] = t.struct(
        {"keyReference": t.string().optional()}
    ).named(renames["CryptoKeyConfigIn"])
    types["CryptoKeyConfigOut"] = t.struct(
        {
            "keyReference": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoKeyConfigOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
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
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "additionalStatus": t.struct({"_": t.string().optional()}).optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
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
    types["InstanceIn"] = t.struct(
        {
            "type": t.string(),
            "description": t.string().optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "enableRbac": t.boolean().optional(),
            "displayName": t.string().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigIn"]).optional(),
            "privateInstance": t.boolean().optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigIn"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigIn"]).optional(),
            "dataprocServiceAccount": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "version": t.string().optional(),
            "zone": t.string().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "enableZoneSeparation": t.boolean().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "type": t.string(),
            "description": t.string().optional(),
            "stateMessage": t.string().optional(),
            "enableStackdriverLogging": t.boolean().optional(),
            "enableStackdriverMonitoring": t.boolean().optional(),
            "enableRbac": t.boolean().optional(),
            "displayName": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "gcsBucket": t.string().optional(),
            "cryptoKeyConfig": t.proxy(renames["CryptoKeyConfigOut"]).optional(),
            "name": t.string().optional(),
            "privateInstance": t.boolean().optional(),
            "eventPublishConfig": t.proxy(renames["EventPublishConfigOut"]).optional(),
            "networkConfig": t.proxy(renames["NetworkConfigOut"]).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "serviceEndpoint": t.string().optional(),
            "p4ServiceAccount": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "dataprocServiceAccount": t.string().optional(),
            "availableVersion": t.array(t.proxy(renames["VersionOut"])).optional(),
            "disabledReason": t.array(t.string()).optional(),
            "satisfiesPzs": t.boolean().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "apiEndpoint": t.string().optional(),
            "version": t.string().optional(),
            "createTime": t.string().optional(),
            "zone": t.string().optional(),
            "options": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "enableZoneSeparation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RestartInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RestartInstanceRequestIn"]
    )
    types["RestartInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestartInstanceRequestOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])

    functions = {}
    functions["projectsLocationsGet"] = datafusion.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = datafusion.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "includeUnrevealedLocations": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = datafusion.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = datafusion.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = datafusion.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = datafusion.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsInstancesDnsPeeringsList"] = datafusion.post(
        "v1/{parent}/dnsPeerings",
        t.struct(
            {
                "parent": t.string(),
                "dnsPeeringId": t.string(),
                "domain": t.string(),
                "targetNetwork": t.string().optional(),
                "targetProject": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DnsPeeringOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsDelete"] = datafusion.post(
        "v1/{parent}/dnsPeerings",
        t.struct(
            {
                "parent": t.string(),
                "dnsPeeringId": t.string(),
                "domain": t.string(),
                "targetNetwork": t.string().optional(),
                "targetProject": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DnsPeeringOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDnsPeeringsCreate"] = datafusion.post(
        "v1/{parent}/dnsPeerings",
        t.struct(
            {
                "parent": t.string(),
                "dnsPeeringId": t.string(),
                "domain": t.string(),
                "targetNetwork": t.string().optional(),
                "targetProject": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DnsPeeringOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVersionsList"] = datafusion.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "latestPatchOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="datafusion",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
