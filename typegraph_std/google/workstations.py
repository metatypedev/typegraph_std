from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_workstations() -> Import:
    workstations = HTTPRuntime("https://workstations.googleapis.com/")

    renames = {
        "ErrorResponse": "_workstations_1_ErrorResponse",
        "StopWorkstationRequestIn": "_workstations_2_StopWorkstationRequestIn",
        "StopWorkstationRequestOut": "_workstations_3_StopWorkstationRequestOut",
        "OperationMetadataIn": "_workstations_4_OperationMetadataIn",
        "OperationMetadataOut": "_workstations_5_OperationMetadataOut",
        "ReadinessCheckIn": "_workstations_6_ReadinessCheckIn",
        "ReadinessCheckOut": "_workstations_7_ReadinessCheckOut",
        "OperationIn": "_workstations_8_OperationIn",
        "OperationOut": "_workstations_9_OperationOut",
        "ListUsableWorkstationConfigsResponseIn": "_workstations_10_ListUsableWorkstationConfigsResponseIn",
        "ListUsableWorkstationConfigsResponseOut": "_workstations_11_ListUsableWorkstationConfigsResponseOut",
        "GenerateAccessTokenResponseIn": "_workstations_12_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_workstations_13_GenerateAccessTokenResponseOut",
        "GenerateAccessTokenRequestIn": "_workstations_14_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_workstations_15_GenerateAccessTokenRequestOut",
        "CancelOperationRequestIn": "_workstations_16_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workstations_17_CancelOperationRequestOut",
        "PolicyIn": "_workstations_18_PolicyIn",
        "PolicyOut": "_workstations_19_PolicyOut",
        "SetIamPolicyRequestIn": "_workstations_20_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_workstations_21_SetIamPolicyRequestOut",
        "BindingIn": "_workstations_22_BindingIn",
        "BindingOut": "_workstations_23_BindingOut",
        "ContainerIn": "_workstations_24_ContainerIn",
        "ContainerOut": "_workstations_25_ContainerOut",
        "GceConfidentialInstanceConfigIn": "_workstations_26_GceConfidentialInstanceConfigIn",
        "GceConfidentialInstanceConfigOut": "_workstations_27_GceConfidentialInstanceConfigOut",
        "TestIamPermissionsResponseIn": "_workstations_28_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_workstations_29_TestIamPermissionsResponseOut",
        "WorkstationConfigIn": "_workstations_30_WorkstationConfigIn",
        "WorkstationConfigOut": "_workstations_31_WorkstationConfigOut",
        "StartWorkstationRequestIn": "_workstations_32_StartWorkstationRequestIn",
        "StartWorkstationRequestOut": "_workstations_33_StartWorkstationRequestOut",
        "ListWorkstationClustersResponseIn": "_workstations_34_ListWorkstationClustersResponseIn",
        "ListWorkstationClustersResponseOut": "_workstations_35_ListWorkstationClustersResponseOut",
        "WorkstationIn": "_workstations_36_WorkstationIn",
        "WorkstationOut": "_workstations_37_WorkstationOut",
        "ListWorkstationConfigsResponseIn": "_workstations_38_ListWorkstationConfigsResponseIn",
        "ListWorkstationConfigsResponseOut": "_workstations_39_ListWorkstationConfigsResponseOut",
        "PersistentDirectoryIn": "_workstations_40_PersistentDirectoryIn",
        "PersistentDirectoryOut": "_workstations_41_PersistentDirectoryOut",
        "GceInstanceIn": "_workstations_42_GceInstanceIn",
        "GceInstanceOut": "_workstations_43_GceInstanceOut",
        "AcceleratorIn": "_workstations_44_AcceleratorIn",
        "AcceleratorOut": "_workstations_45_AcceleratorOut",
        "CustomerEncryptionKeyIn": "_workstations_46_CustomerEncryptionKeyIn",
        "CustomerEncryptionKeyOut": "_workstations_47_CustomerEncryptionKeyOut",
        "ListWorkstationsResponseIn": "_workstations_48_ListWorkstationsResponseIn",
        "ListWorkstationsResponseOut": "_workstations_49_ListWorkstationsResponseOut",
        "GceRegionalPersistentDiskIn": "_workstations_50_GceRegionalPersistentDiskIn",
        "GceRegionalPersistentDiskOut": "_workstations_51_GceRegionalPersistentDiskOut",
        "WorkstationClusterIn": "_workstations_52_WorkstationClusterIn",
        "WorkstationClusterOut": "_workstations_53_WorkstationClusterOut",
        "PrivateClusterConfigIn": "_workstations_54_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_workstations_55_PrivateClusterConfigOut",
        "GceShieldedInstanceConfigIn": "_workstations_56_GceShieldedInstanceConfigIn",
        "GceShieldedInstanceConfigOut": "_workstations_57_GceShieldedInstanceConfigOut",
        "AuditLogConfigIn": "_workstations_58_AuditLogConfigIn",
        "AuditLogConfigOut": "_workstations_59_AuditLogConfigOut",
        "GoogleProtobufEmptyIn": "_workstations_60_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_workstations_61_GoogleProtobufEmptyOut",
        "ListUsableWorkstationsResponseIn": "_workstations_62_ListUsableWorkstationsResponseIn",
        "ListUsableWorkstationsResponseOut": "_workstations_63_ListUsableWorkstationsResponseOut",
        "TestIamPermissionsRequestIn": "_workstations_64_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_workstations_65_TestIamPermissionsRequestOut",
        "AuditConfigIn": "_workstations_66_AuditConfigIn",
        "AuditConfigOut": "_workstations_67_AuditConfigOut",
        "HostIn": "_workstations_68_HostIn",
        "HostOut": "_workstations_69_HostOut",
        "StatusIn": "_workstations_70_StatusIn",
        "StatusOut": "_workstations_71_StatusOut",
        "ListOperationsResponseIn": "_workstations_72_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workstations_73_ListOperationsResponseOut",
        "ExprIn": "_workstations_74_ExprIn",
        "ExprOut": "_workstations_75_ExprOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ReadinessCheckIn"] = t.struct(
        {"port": t.integer().optional(), "path": t.string().optional()}
    ).named(renames["ReadinessCheckIn"])
    types["ReadinessCheckOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadinessCheckOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListUsableWorkstationConfigsResponseIn"] = t.struct(
        {
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseIn"])
    types["ListUsableWorkstationConfigsResponseOut"] = t.struct(
        {
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseOut"])
    types["GenerateAccessTokenResponseIn"] = t.struct(
        {"expireTime": t.string().optional(), "accessToken": t.string().optional()}
    ).named(renames["GenerateAccessTokenResponseIn"])
    types["GenerateAccessTokenResponseOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "accessToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenResponseOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["ContainerIn"] = t.struct(
        {
            "env": t.struct({"_": t.string().optional()}).optional(),
            "workingDir": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "image": t.string().optional(),
            "runAsUser": t.integer().optional(),
            "command": t.array(t.string()).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "env": t.struct({"_": t.string().optional()}).optional(),
            "workingDir": t.string().optional(),
            "args": t.array(t.string()).optional(),
            "image": t.string().optional(),
            "runAsUser": t.integer().optional(),
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
            "readinessChecks": t.array(t.proxy(renames["ReadinessCheckIn"])).optional(),
            "host": t.proxy(renames["HostIn"]).optional(),
            "idleTimeout": t.string().optional(),
            "enableAuditAgent": t.boolean().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "runningTimeout": t.string().optional(),
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryIn"])
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["WorkstationConfigIn"])
    types["WorkstationConfigOut"] = t.struct(
        {
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "readinessChecks": t.array(
                t.proxy(renames["ReadinessCheckOut"])
            ).optional(),
            "reconciling": t.boolean().optional(),
            "host": t.proxy(renames["HostOut"]).optional(),
            "idleTimeout": t.string().optional(),
            "enableAuditAgent": t.boolean().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "runningTimeout": t.string().optional(),
            "createTime": t.string().optional(),
            "degraded": t.boolean().optional(),
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryOut"])
            ).optional(),
            "deleteTime": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationConfigOut"])
    types["StartWorkstationRequestIn"] = t.struct(
        {"validateOnly": t.boolean().optional(), "etag": t.string().optional()}
    ).named(renames["StartWorkstationRequestIn"])
    types["StartWorkstationRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartWorkstationRequestOut"])
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
    types["WorkstationIn"] = t.struct(
        {
            "env": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["WorkstationIn"])
    types["WorkstationOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "host": t.string().optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "deleteTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationOut"])
    types["ListWorkstationConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigIn"])
            ).optional(),
        }
    ).named(renames["ListWorkstationConfigsResponseIn"])
    types["ListWorkstationConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationConfigsResponseOut"])
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
    types["GceInstanceIn"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "machineType": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "poolSize": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigIn"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigIn"]
            ).optional(),
        }
    ).named(renames["GceInstanceIn"])
    types["GceInstanceOut"] = t.struct(
        {
            "pooledInstances": t.integer().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "machineType": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "poolSize": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigOut"]
            ).optional(),
            "serviceAccount": t.string().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceOut"])
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
    types["ListWorkstationsResponseIn"] = t.struct(
        {
            "workstations": t.array(t.proxy(renames["WorkstationIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWorkstationsResponseIn"])
    types["ListWorkstationsResponseOut"] = t.struct(
        {
            "workstations": t.array(t.proxy(renames["WorkstationOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationsResponseOut"])
    types["GceRegionalPersistentDiskIn"] = t.struct(
        {
            "diskType": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "fsType": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
            "reclaimPolicy": t.string().optional(),
        }
    ).named(renames["GceRegionalPersistentDiskIn"])
    types["GceRegionalPersistentDiskOut"] = t.struct(
        {
            "diskType": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "fsType": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
            "reclaimPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceRegionalPersistentDiskOut"])
    types["WorkstationClusterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
        }
    ).named(renames["WorkstationClusterIn"])
    types["WorkstationClusterOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "createTime": t.string().optional(),
            "controlPlaneIp": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "network": t.string().optional(),
            "degraded": t.boolean().optional(),
            "subnetwork": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationClusterOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "allowedProjects": t.array(t.string()).optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "serviceAttachmentUri": t.string().optional(),
            "clusterHostname": t.string().optional(),
            "allowedProjects": t.array(t.string()).optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
    types["GceShieldedInstanceConfigIn"] = t.struct(
        {
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
        }
    ).named(renames["GceShieldedInstanceConfigIn"])
    types["GceShieldedInstanceConfigOut"] = t.struct(
        {
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceShieldedInstanceConfigOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["ListUsableWorkstationsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "workstations": t.array(t.proxy(renames["WorkstationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUsableWorkstationsResponseIn"])
    types["ListUsableWorkstationsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "workstations": t.array(t.proxy(renames["WorkstationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableWorkstationsResponseOut"])
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
    types["HostIn"] = t.struct(
        {"gceInstance": t.proxy(renames["GceInstanceIn"]).optional()}
    ).named(renames["HostIn"])
    types["HostOut"] = t.struct(
        {
            "gceInstance": t.proxy(renames["GceInstanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])

    functions = {}
    functions["projectsLocationsWorkstationClustersGet"] = workstations.post(
        "v1beta/{parent}/workstationClusters",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "workstationClusterId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "network": t.string().optional(),
                "subnetwork": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersList"] = workstations.post(
        "v1beta/{parent}/workstationClusters",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "workstationClusterId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "network": t.string().optional(),
                "subnetwork": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersDelete"] = workstations.post(
        "v1beta/{parent}/workstationClusters",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "workstationClusterId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "network": t.string().optional(),
                "subnetwork": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersPatch"] = workstations.post(
        "v1beta/{parent}/workstationClusters",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "workstationClusterId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "network": t.string().optional(),
                "subnetwork": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersCreate"] = workstations.post(
        "v1beta/{parent}/workstationClusters",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "workstationClusterId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "network": t.string().optional(),
                "subnetwork": t.string().optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsSetIamPolicy"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsTestIamPermissions"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsListUsable"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsList"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsPatch"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGetIamPolicy"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGet"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsCreate"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsDelete"
    ] = workstations.delete(
        "v1beta/{name}",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsList"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsPatch"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsListUsable"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsSetIamPolicy"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGenerateAccessToken"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsDelete"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStart"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGet"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGetIamPolicy"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsTestIamPermissions"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStop"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsCreate"
    ] = workstations.post(
        "v1beta/{parent}/workstations",
        t.struct(
            {
                "workstationId": t.string(),
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "env": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "etag": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = workstations.post(
        "v1beta/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = workstations.post(
        "v1beta/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = workstations.post(
        "v1beta/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = workstations.post(
        "v1beta/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="workstations",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
