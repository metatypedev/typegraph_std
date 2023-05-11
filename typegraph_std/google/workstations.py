from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_workstations() -> Import:
    workstations = HTTPRuntime("https://workstations.googleapis.com/")

    renames = {
        "ErrorResponse": "_workstations_1_ErrorResponse",
        "SetIamPolicyRequestIn": "_workstations_2_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_workstations_3_SetIamPolicyRequestOut",
        "StatusIn": "_workstations_4_StatusIn",
        "StatusOut": "_workstations_5_StatusOut",
        "PersistentDirectoryIn": "_workstations_6_PersistentDirectoryIn",
        "PersistentDirectoryOut": "_workstations_7_PersistentDirectoryOut",
        "ReadinessCheckIn": "_workstations_8_ReadinessCheckIn",
        "ReadinessCheckOut": "_workstations_9_ReadinessCheckOut",
        "GceRegionalPersistentDiskIn": "_workstations_10_GceRegionalPersistentDiskIn",
        "GceRegionalPersistentDiskOut": "_workstations_11_GceRegionalPersistentDiskOut",
        "GenerateAccessTokenResponseIn": "_workstations_12_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_workstations_13_GenerateAccessTokenResponseOut",
        "StartWorkstationRequestIn": "_workstations_14_StartWorkstationRequestIn",
        "StartWorkstationRequestOut": "_workstations_15_StartWorkstationRequestOut",
        "WorkstationClusterIn": "_workstations_16_WorkstationClusterIn",
        "WorkstationClusterOut": "_workstations_17_WorkstationClusterOut",
        "PolicyIn": "_workstations_18_PolicyIn",
        "PolicyOut": "_workstations_19_PolicyOut",
        "AuditConfigIn": "_workstations_20_AuditConfigIn",
        "AuditConfigOut": "_workstations_21_AuditConfigOut",
        "CancelOperationRequestIn": "_workstations_22_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workstations_23_CancelOperationRequestOut",
        "ExprIn": "_workstations_24_ExprIn",
        "ExprOut": "_workstations_25_ExprOut",
        "TestIamPermissionsResponseIn": "_workstations_26_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_workstations_27_TestIamPermissionsResponseOut",
        "WorkstationConfigIn": "_workstations_28_WorkstationConfigIn",
        "WorkstationConfigOut": "_workstations_29_WorkstationConfigOut",
        "ListUsableWorkstationConfigsResponseIn": "_workstations_30_ListUsableWorkstationConfigsResponseIn",
        "ListUsableWorkstationConfigsResponseOut": "_workstations_31_ListUsableWorkstationConfigsResponseOut",
        "OperationMetadataIn": "_workstations_32_OperationMetadataIn",
        "OperationMetadataOut": "_workstations_33_OperationMetadataOut",
        "GceShieldedInstanceConfigIn": "_workstations_34_GceShieldedInstanceConfigIn",
        "GceShieldedInstanceConfigOut": "_workstations_35_GceShieldedInstanceConfigOut",
        "ContainerIn": "_workstations_36_ContainerIn",
        "ContainerOut": "_workstations_37_ContainerOut",
        "GceConfidentialInstanceConfigIn": "_workstations_38_GceConfidentialInstanceConfigIn",
        "GceConfidentialInstanceConfigOut": "_workstations_39_GceConfidentialInstanceConfigOut",
        "OperationIn": "_workstations_40_OperationIn",
        "OperationOut": "_workstations_41_OperationOut",
        "TestIamPermissionsRequestIn": "_workstations_42_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_workstations_43_TestIamPermissionsRequestOut",
        "StopWorkstationRequestIn": "_workstations_44_StopWorkstationRequestIn",
        "StopWorkstationRequestOut": "_workstations_45_StopWorkstationRequestOut",
        "AuditLogConfigIn": "_workstations_46_AuditLogConfigIn",
        "AuditLogConfigOut": "_workstations_47_AuditLogConfigOut",
        "ListOperationsResponseIn": "_workstations_48_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workstations_49_ListOperationsResponseOut",
        "ListWorkstationConfigsResponseIn": "_workstations_50_ListWorkstationConfigsResponseIn",
        "ListWorkstationConfigsResponseOut": "_workstations_51_ListWorkstationConfigsResponseOut",
        "BindingIn": "_workstations_52_BindingIn",
        "BindingOut": "_workstations_53_BindingOut",
        "HostIn": "_workstations_54_HostIn",
        "HostOut": "_workstations_55_HostOut",
        "AcceleratorIn": "_workstations_56_AcceleratorIn",
        "AcceleratorOut": "_workstations_57_AcceleratorOut",
        "ListWorkstationClustersResponseIn": "_workstations_58_ListWorkstationClustersResponseIn",
        "ListWorkstationClustersResponseOut": "_workstations_59_ListWorkstationClustersResponseOut",
        "ListWorkstationsResponseIn": "_workstations_60_ListWorkstationsResponseIn",
        "ListWorkstationsResponseOut": "_workstations_61_ListWorkstationsResponseOut",
        "PrivateClusterConfigIn": "_workstations_62_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_workstations_63_PrivateClusterConfigOut",
        "GenerateAccessTokenRequestIn": "_workstations_64_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_workstations_65_GenerateAccessTokenRequestOut",
        "WorkstationIn": "_workstations_66_WorkstationIn",
        "WorkstationOut": "_workstations_67_WorkstationOut",
        "GceInstanceIn": "_workstations_68_GceInstanceIn",
        "GceInstanceOut": "_workstations_69_GceInstanceOut",
        "ListUsableWorkstationsResponseIn": "_workstations_70_ListUsableWorkstationsResponseIn",
        "ListUsableWorkstationsResponseOut": "_workstations_71_ListUsableWorkstationsResponseOut",
        "GoogleProtobufEmptyIn": "_workstations_72_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_workstations_73_GoogleProtobufEmptyOut",
        "CustomerEncryptionKeyIn": "_workstations_74_CustomerEncryptionKeyIn",
        "CustomerEncryptionKeyOut": "_workstations_75_CustomerEncryptionKeyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["PersistentDirectoryIn"] = t.struct(
        {
            "mountPath": t.string().optional(),
            "gcePd": t.proxy(renames["GceRegionalPersistentDiskIn"]).optional(),
        }
    ).named(renames["PersistentDirectoryIn"])
    types["PersistentDirectoryOut"] = t.struct(
        {
            "mountPath": t.string().optional(),
            "gcePd": t.proxy(renames["GceRegionalPersistentDiskOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistentDirectoryOut"])
    types["ReadinessCheckIn"] = t.struct(
        {"path": t.string().optional(), "port": t.integer().optional()}
    ).named(renames["ReadinessCheckIn"])
    types["ReadinessCheckOut"] = t.struct(
        {
            "path": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadinessCheckOut"])
    types["GceRegionalPersistentDiskIn"] = t.struct(
        {
            "diskType": t.string().optional(),
            "fsType": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "reclaimPolicy": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
        }
    ).named(renames["GceRegionalPersistentDiskIn"])
    types["GceRegionalPersistentDiskOut"] = t.struct(
        {
            "diskType": t.string().optional(),
            "fsType": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "reclaimPolicy": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceRegionalPersistentDiskOut"])
    types["GenerateAccessTokenResponseIn"] = t.struct(
        {"accessToken": t.string().optional(), "expireTime": t.string().optional()}
    ).named(renames["GenerateAccessTokenResponseIn"])
    types["GenerateAccessTokenResponseOut"] = t.struct(
        {
            "accessToken": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenResponseOut"])
    types["StartWorkstationRequestIn"] = t.struct(
        {"etag": t.string().optional(), "validateOnly": t.boolean().optional()}
    ).named(renames["StartWorkstationRequestIn"])
    types["StartWorkstationRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartWorkstationRequestOut"])
    types["WorkstationClusterIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkstationClusterIn"])
    types["WorkstationClusterOut"] = t.struct(
        {
            "degraded": t.boolean().optional(),
            "controlPlaneIp": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "subnetwork": t.string().optional(),
            "deleteTime": t.string().optional(),
            "network": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "reconciling": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationClusterOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["WorkstationConfigIn"] = t.struct(
        {
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "runningTimeout": t.string().optional(),
            "etag": t.string().optional(),
            "readinessChecks": t.array(t.proxy(renames["ReadinessCheckIn"])).optional(),
            "enableAuditAgent": t.boolean().optional(),
            "idleTimeout": t.string().optional(),
            "host": t.proxy(renames["HostIn"]).optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkstationConfigIn"])
    types["WorkstationConfigOut"] = t.struct(
        {
            "deleteTime": t.string().optional(),
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryOut"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "degraded": t.boolean().optional(),
            "runningTimeout": t.string().optional(),
            "etag": t.string().optional(),
            "readinessChecks": t.array(
                t.proxy(renames["ReadinessCheckOut"])
            ).optional(),
            "enableAuditAgent": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "idleTimeout": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "host": t.proxy(renames["HostOut"]).optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationConfigOut"])
    types["ListUsableWorkstationConfigsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigIn"])
            ).optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseIn"])
    types["ListUsableWorkstationConfigsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GceShieldedInstanceConfigIn"] = t.struct(
        {
            "enableVtpm": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
        }
    ).named(renames["GceShieldedInstanceConfigIn"])
    types["GceShieldedInstanceConfigOut"] = t.struct(
        {
            "enableVtpm": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceShieldedInstanceConfigOut"])
    types["ContainerIn"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "runAsUser": t.integer().optional(),
            "image": t.string().optional(),
            "workingDir": t.string().optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "command": t.array(t.string()).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "args": t.array(t.string()).optional(),
            "runAsUser": t.integer().optional(),
            "image": t.string().optional(),
            "workingDir": t.string().optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "command": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["GceConfidentialInstanceConfigIn"] = t.struct(
        {"enableConfidentialCompute": t.boolean().optional()}
    ).named(renames["GceConfidentialInstanceConfigIn"])
    types["GceConfidentialInstanceConfigOut"] = t.struct(
        {
            "enableConfidentialCompute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceConfidentialInstanceConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["StopWorkstationRequestIn"] = t.struct(
        {"validateOnly": t.boolean().optional(), "etag": t.string().optional()}
    ).named(renames["StopWorkstationRequestIn"])
    types["StopWorkstationRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopWorkstationRequestOut"])
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
    types["ListWorkstationConfigsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigIn"])
            ).optional(),
        }
    ).named(renames["ListWorkstationConfigsResponseIn"])
    types["ListWorkstationConfigsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationConfigsResponseOut"])
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
    types["HostIn"] = t.struct(
        {"gceInstance": t.proxy(renames["GceInstanceIn"]).optional()}
    ).named(renames["HostIn"])
    types["HostOut"] = t.struct(
        {
            "gceInstance": t.proxy(renames["GceInstanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostOut"])
    types["AcceleratorIn"] = t.struct(
        {"count": t.integer().optional(), "type": t.string().optional()}
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "count": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["ListWorkstationClustersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstationClusters": t.array(
                t.proxy(renames["WorkstationClusterIn"])
            ).optional(),
        }
    ).named(renames["ListWorkstationClustersResponseIn"])
    types["ListWorkstationClustersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstationClusters": t.array(
                t.proxy(renames["WorkstationClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationClustersResponseOut"])
    types["ListWorkstationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstations": t.array(t.proxy(renames["WorkstationIn"])).optional(),
        }
    ).named(renames["ListWorkstationsResponseIn"])
    types["ListWorkstationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "workstations": t.array(t.proxy(renames["WorkstationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationsResponseOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "allowedProjects": t.array(t.string()).optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "serviceAttachmentUri": t.string().optional(),
            "allowedProjects": t.array(t.string()).optional(),
            "clusterHostname": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["GenerateAccessTokenRequestIn"] = t.struct(
        {"ttl": t.string().optional(), "expireTime": t.string().optional()}
    ).named(renames["GenerateAccessTokenRequestIn"])
    types["GenerateAccessTokenRequestOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenRequestOut"])
    types["WorkstationIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkstationIn"])
    types["WorkstationOut"] = t.struct(
        {
            "state": t.string().optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "host": t.string().optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationOut"])
    types["GceInstanceIn"] = t.struct(
        {
            "bootDiskSizeGb": t.integer().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigIn"]
            ).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigIn"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "serviceAccount": t.string().optional(),
            "poolSize": t.integer().optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["GceInstanceIn"])
    types["GceInstanceOut"] = t.struct(
        {
            "bootDiskSizeGb": t.integer().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigOut"]
            ).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigOut"]
            ).optional(),
            "tags": t.array(t.string()).optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "serviceAccount": t.string().optional(),
            "pooledInstances": t.integer().optional(),
            "poolSize": t.integer().optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceOut"])
    types["ListUsableWorkstationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workstations": t.array(t.proxy(renames["WorkstationIn"])).optional(),
        }
    ).named(renames["ListUsableWorkstationsResponseIn"])
    types["ListUsableWorkstationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workstations": t.array(t.proxy(renames["WorkstationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableWorkstationsResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["CustomerEncryptionKeyIn"] = t.struct(
        {"kmsKeyServiceAccount": t.string().optional(), "kmsKey": t.string().optional()}
    ).named(renames["CustomerEncryptionKeyIn"])
    types["CustomerEncryptionKeyOut"] = t.struct(
        {
            "kmsKeyServiceAccount": t.string().optional(),
            "kmsKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerEncryptionKeyOut"])

    functions = {}
    functions["projectsLocationsOperationsCancel"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersList"] = workstations.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersGet"] = workstations.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersCreate"] = workstations.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersDelete"] = workstations.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersPatch"] = workstations.patch(
        "v1beta/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsListUsable"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsSetIamPolicy"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsPatch"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGet"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsList"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsCreate"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsDelete"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsTestIamPermissions"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGetIamPolicy"
    ] = workstations.get(
        "v1beta/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsSetIamPolicy"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsListUsable"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStart"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsTestIamPermissions"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsPatch"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStop"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGenerateAccessToken"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGetIamPolicy"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsList"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGet"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsCreate"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsDelete"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workstations", renames=renames, types=types, functions=functions
    )
