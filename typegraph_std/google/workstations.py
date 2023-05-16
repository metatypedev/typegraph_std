from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_workstations() -> Import:
    workstations = HTTPRuntime("https://workstations.googleapis.com/")

    renames = {
        "ErrorResponse": "_workstations_1_ErrorResponse",
        "StartWorkstationRequestIn": "_workstations_2_StartWorkstationRequestIn",
        "StartWorkstationRequestOut": "_workstations_3_StartWorkstationRequestOut",
        "GceRegionalPersistentDiskIn": "_workstations_4_GceRegionalPersistentDiskIn",
        "GceRegionalPersistentDiskOut": "_workstations_5_GceRegionalPersistentDiskOut",
        "OperationIn": "_workstations_6_OperationIn",
        "OperationOut": "_workstations_7_OperationOut",
        "AcceleratorIn": "_workstations_8_AcceleratorIn",
        "AcceleratorOut": "_workstations_9_AcceleratorOut",
        "PolicyIn": "_workstations_10_PolicyIn",
        "PolicyOut": "_workstations_11_PolicyOut",
        "ListWorkstationConfigsResponseIn": "_workstations_12_ListWorkstationConfigsResponseIn",
        "ListWorkstationConfigsResponseOut": "_workstations_13_ListWorkstationConfigsResponseOut",
        "CancelOperationRequestIn": "_workstations_14_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workstations_15_CancelOperationRequestOut",
        "WorkstationClusterIn": "_workstations_16_WorkstationClusterIn",
        "WorkstationClusterOut": "_workstations_17_WorkstationClusterOut",
        "GceConfidentialInstanceConfigIn": "_workstations_18_GceConfidentialInstanceConfigIn",
        "GceConfidentialInstanceConfigOut": "_workstations_19_GceConfidentialInstanceConfigOut",
        "ListUsableWorkstationsResponseIn": "_workstations_20_ListUsableWorkstationsResponseIn",
        "ListUsableWorkstationsResponseOut": "_workstations_21_ListUsableWorkstationsResponseOut",
        "HostIn": "_workstations_22_HostIn",
        "HostOut": "_workstations_23_HostOut",
        "WorkstationConfigIn": "_workstations_24_WorkstationConfigIn",
        "WorkstationConfigOut": "_workstations_25_WorkstationConfigOut",
        "AuditConfigIn": "_workstations_26_AuditConfigIn",
        "AuditConfigOut": "_workstations_27_AuditConfigOut",
        "OperationMetadataIn": "_workstations_28_OperationMetadataIn",
        "OperationMetadataOut": "_workstations_29_OperationMetadataOut",
        "GceInstanceIn": "_workstations_30_GceInstanceIn",
        "GceInstanceOut": "_workstations_31_GceInstanceOut",
        "SetIamPolicyRequestIn": "_workstations_32_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_workstations_33_SetIamPolicyRequestOut",
        "ListWorkstationClustersResponseIn": "_workstations_34_ListWorkstationClustersResponseIn",
        "ListWorkstationClustersResponseOut": "_workstations_35_ListWorkstationClustersResponseOut",
        "PersistentDirectoryIn": "_workstations_36_PersistentDirectoryIn",
        "PersistentDirectoryOut": "_workstations_37_PersistentDirectoryOut",
        "BindingIn": "_workstations_38_BindingIn",
        "BindingOut": "_workstations_39_BindingOut",
        "GenerateAccessTokenResponseIn": "_workstations_40_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_workstations_41_GenerateAccessTokenResponseOut",
        "StopWorkstationRequestIn": "_workstations_42_StopWorkstationRequestIn",
        "StopWorkstationRequestOut": "_workstations_43_StopWorkstationRequestOut",
        "ReadinessCheckIn": "_workstations_44_ReadinessCheckIn",
        "ReadinessCheckOut": "_workstations_45_ReadinessCheckOut",
        "StatusIn": "_workstations_46_StatusIn",
        "StatusOut": "_workstations_47_StatusOut",
        "TestIamPermissionsRequestIn": "_workstations_48_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_workstations_49_TestIamPermissionsRequestOut",
        "GoogleProtobufEmptyIn": "_workstations_50_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_workstations_51_GoogleProtobufEmptyOut",
        "ContainerIn": "_workstations_52_ContainerIn",
        "ContainerOut": "_workstations_53_ContainerOut",
        "PrivateClusterConfigIn": "_workstations_54_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_workstations_55_PrivateClusterConfigOut",
        "CustomerEncryptionKeyIn": "_workstations_56_CustomerEncryptionKeyIn",
        "CustomerEncryptionKeyOut": "_workstations_57_CustomerEncryptionKeyOut",
        "TestIamPermissionsResponseIn": "_workstations_58_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_workstations_59_TestIamPermissionsResponseOut",
        "GceShieldedInstanceConfigIn": "_workstations_60_GceShieldedInstanceConfigIn",
        "GceShieldedInstanceConfigOut": "_workstations_61_GceShieldedInstanceConfigOut",
        "ExprIn": "_workstations_62_ExprIn",
        "ExprOut": "_workstations_63_ExprOut",
        "AuditLogConfigIn": "_workstations_64_AuditLogConfigIn",
        "AuditLogConfigOut": "_workstations_65_AuditLogConfigOut",
        "GenerateAccessTokenRequestIn": "_workstations_66_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_workstations_67_GenerateAccessTokenRequestOut",
        "WorkstationIn": "_workstations_68_WorkstationIn",
        "WorkstationOut": "_workstations_69_WorkstationOut",
        "ListUsableWorkstationConfigsResponseIn": "_workstations_70_ListUsableWorkstationConfigsResponseIn",
        "ListUsableWorkstationConfigsResponseOut": "_workstations_71_ListUsableWorkstationConfigsResponseOut",
        "ListOperationsResponseIn": "_workstations_72_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workstations_73_ListOperationsResponseOut",
        "ListWorkstationsResponseIn": "_workstations_74_ListWorkstationsResponseIn",
        "ListWorkstationsResponseOut": "_workstations_75_ListWorkstationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GceRegionalPersistentDiskIn"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "diskType": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
            "fsType": t.string().optional(),
            "reclaimPolicy": t.string().optional(),
        }
    ).named(renames["GceRegionalPersistentDiskIn"])
    types["GceRegionalPersistentDiskOut"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "diskType": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
            "fsType": t.string().optional(),
            "reclaimPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceRegionalPersistentDiskOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["AcceleratorIn"] = t.struct(
        {"type": t.string().optional(), "count": t.integer().optional()}
    ).named(renames["AcceleratorIn"])
    types["AcceleratorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "count": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcceleratorOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListWorkstationConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListWorkstationConfigsResponseIn"])
    types["ListWorkstationConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationConfigsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["WorkstationClusterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
        }
    ).named(renames["WorkstationClusterIn"])
    types["WorkstationClusterOut"] = t.struct(
        {
            "degraded": t.boolean().optional(),
            "reconciling": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "controlPlaneIp": t.string().optional(),
            "deleteTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationClusterOut"])
    types["GceConfidentialInstanceConfigIn"] = t.struct(
        {"enableConfidentialCompute": t.boolean().optional()}
    ).named(renames["GceConfidentialInstanceConfigIn"])
    types["GceConfidentialInstanceConfigOut"] = t.struct(
        {
            "enableConfidentialCompute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceConfidentialInstanceConfigOut"])
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
    types["HostIn"] = t.struct(
        {"gceInstance": t.proxy(renames["GceInstanceIn"]).optional()}
    ).named(renames["HostIn"])
    types["HostOut"] = t.struct(
        {
            "gceInstance": t.proxy(renames["GceInstanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostOut"])
    types["WorkstationConfigIn"] = t.struct(
        {
            "idleTimeout": t.string().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyIn"]).optional(),
            "host": t.proxy(renames["HostIn"]).optional(),
            "readinessChecks": t.array(t.proxy(renames["ReadinessCheckIn"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "runningTimeout": t.string().optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "etag": t.string().optional(),
            "enableAuditAgent": t.boolean().optional(),
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryIn"])
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkstationConfigIn"])
    types["WorkstationConfigOut"] = t.struct(
        {
            "reconciling": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "idleTimeout": t.string().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyOut"]).optional(),
            "host": t.proxy(renames["HostOut"]).optional(),
            "deleteTime": t.string().optional(),
            "readinessChecks": t.array(
                t.proxy(renames["ReadinessCheckOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "runningTimeout": t.string().optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "degraded": t.boolean().optional(),
            "uid": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "etag": t.string().optional(),
            "enableAuditAgent": t.boolean().optional(),
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryOut"])
            ).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationConfigOut"])
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
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GceInstanceIn"] = t.struct(
        {
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigIn"]
            ).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigIn"]
            ).optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "poolSize": t.integer().optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["GceInstanceIn"])
    types["GceInstanceOut"] = t.struct(
        {
            "pooledInstances": t.integer().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigOut"]
            ).optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigOut"]
            ).optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "poolSize": t.integer().optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceOut"])
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
    types["ListWorkstationClustersResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "workstationClusters": t.array(
                t.proxy(renames["WorkstationClusterIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWorkstationClustersResponseIn"])
    types["ListWorkstationClustersResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "workstationClusters": t.array(
                t.proxy(renames["WorkstationClusterOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationClustersResponseOut"])
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
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["ContainerIn"] = t.struct(
        {
            "env": t.struct({"_": t.string().optional()}).optional(),
            "workingDir": t.string().optional(),
            "command": t.array(t.string()).optional(),
            "image": t.string().optional(),
            "runAsUser": t.integer().optional(),
            "args": t.array(t.string()).optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "env": t.struct({"_": t.string().optional()}).optional(),
            "workingDir": t.string().optional(),
            "command": t.array(t.string()).optional(),
            "image": t.string().optional(),
            "runAsUser": t.integer().optional(),
            "args": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "allowedProjects": t.array(t.string()).optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "clusterHostname": t.string().optional(),
            "allowedProjects": t.array(t.string()).optional(),
            "serviceAttachmentUri": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GceShieldedInstanceConfigIn"] = t.struct(
        {
            "enableVtpm": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
        }
    ).named(renames["GceShieldedInstanceConfigIn"])
    types["GceShieldedInstanceConfigOut"] = t.struct(
        {
            "enableVtpm": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableSecureBoot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceShieldedInstanceConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkstationIn"])
    types["WorkstationOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "host": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationOut"])
    types["ListUsableWorkstationConfigsResponseIn"] = t.struct(
        {
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseIn"])
    types["ListUsableWorkstationConfigsResponseOut"] = t.struct(
        {
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseOut"])
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
    types["ListWorkstationsResponseIn"] = t.struct(
        {
            "workstations": t.array(t.proxy(renames["WorkstationIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListWorkstationsResponseIn"])
    types["ListWorkstationsResponseOut"] = t.struct(
        {
            "workstations": t.array(t.proxy(renames["WorkstationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationsResponseOut"])

    functions = {}
    functions["projectsLocationsWorkstationClustersDelete"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersList"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersCreate"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersPatch"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsWorkstationClustersGet"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsPatch"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsCreate"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsSetIamPolicy"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsTestIamPermissions"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGetIamPolicy"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsList"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsListUsable"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsDelete"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGet"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsCreate"
    ] = workstations.post(
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
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
        "v1beta/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = workstations.get(
        "v1beta/{name}/operations",
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
    functions["projectsLocationsOperationsDelete"] = workstations.get(
        "v1beta/{name}/operations",
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
    functions["projectsLocationsOperationsCancel"] = workstations.get(
        "v1beta/{name}/operations",
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
    functions["projectsLocationsOperationsList"] = workstations.get(
        "v1beta/{name}/operations",
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

    return Import(
        importer="workstations",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
