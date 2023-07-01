from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_workstations():
    workstations = HTTPRuntime("https://workstations.googleapis.com/")

    renames = {
        "ErrorResponse": "_workstations_1_ErrorResponse",
        "StopWorkstationRequestIn": "_workstations_2_StopWorkstationRequestIn",
        "StopWorkstationRequestOut": "_workstations_3_StopWorkstationRequestOut",
        "ListWorkstationsResponseIn": "_workstations_4_ListWorkstationsResponseIn",
        "ListWorkstationsResponseOut": "_workstations_5_ListWorkstationsResponseOut",
        "GceInstanceIn": "_workstations_6_GceInstanceIn",
        "GceInstanceOut": "_workstations_7_GceInstanceOut",
        "ListWorkstationClustersResponseIn": "_workstations_8_ListWorkstationClustersResponseIn",
        "ListWorkstationClustersResponseOut": "_workstations_9_ListWorkstationClustersResponseOut",
        "ExprIn": "_workstations_10_ExprIn",
        "ExprOut": "_workstations_11_ExprOut",
        "WorkstationClusterIn": "_workstations_12_WorkstationClusterIn",
        "WorkstationClusterOut": "_workstations_13_WorkstationClusterOut",
        "WorkstationConfigIn": "_workstations_14_WorkstationConfigIn",
        "WorkstationConfigOut": "_workstations_15_WorkstationConfigOut",
        "StatusIn": "_workstations_16_StatusIn",
        "StatusOut": "_workstations_17_StatusOut",
        "CustomerEncryptionKeyIn": "_workstations_18_CustomerEncryptionKeyIn",
        "CustomerEncryptionKeyOut": "_workstations_19_CustomerEncryptionKeyOut",
        "ListUsableWorkstationConfigsResponseIn": "_workstations_20_ListUsableWorkstationConfigsResponseIn",
        "ListUsableWorkstationConfigsResponseOut": "_workstations_21_ListUsableWorkstationConfigsResponseOut",
        "GceConfidentialInstanceConfigIn": "_workstations_22_GceConfidentialInstanceConfigIn",
        "GceConfidentialInstanceConfigOut": "_workstations_23_GceConfidentialInstanceConfigOut",
        "PrivateClusterConfigIn": "_workstations_24_PrivateClusterConfigIn",
        "PrivateClusterConfigOut": "_workstations_25_PrivateClusterConfigOut",
        "AuditConfigIn": "_workstations_26_AuditConfigIn",
        "AuditConfigOut": "_workstations_27_AuditConfigOut",
        "ListUsableWorkstationsResponseIn": "_workstations_28_ListUsableWorkstationsResponseIn",
        "ListUsableWorkstationsResponseOut": "_workstations_29_ListUsableWorkstationsResponseOut",
        "BindingIn": "_workstations_30_BindingIn",
        "BindingOut": "_workstations_31_BindingOut",
        "ContainerIn": "_workstations_32_ContainerIn",
        "ContainerOut": "_workstations_33_ContainerOut",
        "GoogleProtobufEmptyIn": "_workstations_34_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_workstations_35_GoogleProtobufEmptyOut",
        "ListOperationsResponseIn": "_workstations_36_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_workstations_37_ListOperationsResponseOut",
        "GceRegionalPersistentDiskIn": "_workstations_38_GceRegionalPersistentDiskIn",
        "GceRegionalPersistentDiskOut": "_workstations_39_GceRegionalPersistentDiskOut",
        "WorkstationIn": "_workstations_40_WorkstationIn",
        "WorkstationOut": "_workstations_41_WorkstationOut",
        "TestIamPermissionsResponseIn": "_workstations_42_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_workstations_43_TestIamPermissionsResponseOut",
        "OperationMetadataIn": "_workstations_44_OperationMetadataIn",
        "OperationMetadataOut": "_workstations_45_OperationMetadataOut",
        "AuditLogConfigIn": "_workstations_46_AuditLogConfigIn",
        "AuditLogConfigOut": "_workstations_47_AuditLogConfigOut",
        "ListWorkstationConfigsResponseIn": "_workstations_48_ListWorkstationConfigsResponseIn",
        "ListWorkstationConfigsResponseOut": "_workstations_49_ListWorkstationConfigsResponseOut",
        "GenerateAccessTokenRequestIn": "_workstations_50_GenerateAccessTokenRequestIn",
        "GenerateAccessTokenRequestOut": "_workstations_51_GenerateAccessTokenRequestOut",
        "OperationIn": "_workstations_52_OperationIn",
        "OperationOut": "_workstations_53_OperationOut",
        "StartWorkstationRequestIn": "_workstations_54_StartWorkstationRequestIn",
        "StartWorkstationRequestOut": "_workstations_55_StartWorkstationRequestOut",
        "HostIn": "_workstations_56_HostIn",
        "HostOut": "_workstations_57_HostOut",
        "GceShieldedInstanceConfigIn": "_workstations_58_GceShieldedInstanceConfigIn",
        "GceShieldedInstanceConfigOut": "_workstations_59_GceShieldedInstanceConfigOut",
        "PersistentDirectoryIn": "_workstations_60_PersistentDirectoryIn",
        "PersistentDirectoryOut": "_workstations_61_PersistentDirectoryOut",
        "SetIamPolicyRequestIn": "_workstations_62_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_workstations_63_SetIamPolicyRequestOut",
        "CancelOperationRequestIn": "_workstations_64_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_workstations_65_CancelOperationRequestOut",
        "ReadinessCheckIn": "_workstations_66_ReadinessCheckIn",
        "ReadinessCheckOut": "_workstations_67_ReadinessCheckOut",
        "GenerateAccessTokenResponseIn": "_workstations_68_GenerateAccessTokenResponseIn",
        "GenerateAccessTokenResponseOut": "_workstations_69_GenerateAccessTokenResponseOut",
        "AcceleratorIn": "_workstations_70_AcceleratorIn",
        "AcceleratorOut": "_workstations_71_AcceleratorOut",
        "PolicyIn": "_workstations_72_PolicyIn",
        "PolicyOut": "_workstations_73_PolicyOut",
        "TestIamPermissionsRequestIn": "_workstations_74_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_workstations_75_TestIamPermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StopWorkstationRequestIn"] = t.struct(
        {"etag": t.string().optional(), "validateOnly": t.boolean().optional()}
    ).named(renames["StopWorkstationRequestIn"])
    types["StopWorkstationRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StopWorkstationRequestOut"])
    types["ListWorkstationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workstations": t.array(t.proxy(renames["WorkstationIn"])).optional(),
        }
    ).named(renames["ListWorkstationsResponseIn"])
    types["ListWorkstationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "workstations": t.array(t.proxy(renames["WorkstationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationsResponseOut"])
    types["GceInstanceIn"] = t.struct(
        {
            "enableNestedVirtualization": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorIn"])).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigIn"]
            ).optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "poolSize": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigIn"]
            ).optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["GceInstanceIn"])
    types["GceInstanceOut"] = t.struct(
        {
            "enableNestedVirtualization": t.boolean().optional(),
            "serviceAccount": t.string().optional(),
            "accelerators": t.array(t.proxy(renames["AcceleratorOut"])).optional(),
            "confidentialInstanceConfig": t.proxy(
                renames["GceConfidentialInstanceConfigOut"]
            ).optional(),
            "disablePublicIpAddresses": t.boolean().optional(),
            "pooledInstances": t.integer().optional(),
            "poolSize": t.integer().optional(),
            "tags": t.array(t.string()).optional(),
            "bootDiskSizeGb": t.integer().optional(),
            "shieldedInstanceConfig": t.proxy(
                renames["GceShieldedInstanceConfigOut"]
            ).optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceInstanceOut"])
    types["ListWorkstationClustersResponseIn"] = t.struct(
        {
            "workstationClusters": t.array(
                t.proxy(renames["WorkstationClusterIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListWorkstationClustersResponseIn"])
    types["ListWorkstationClustersResponseOut"] = t.struct(
        {
            "workstationClusters": t.array(
                t.proxy(renames["WorkstationClusterOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkstationClustersResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["WorkstationClusterIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigIn"]
            ).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["WorkstationClusterIn"])
    types["WorkstationClusterOut"] = t.struct(
        {
            "degraded": t.boolean().optional(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "privateClusterConfig": t.proxy(
                renames["PrivateClusterConfigOut"]
            ).optional(),
            "controlPlaneIp": t.string().optional(),
            "name": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "updateTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationClusterOut"])
    types["WorkstationConfigIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "container": t.proxy(renames["ContainerIn"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "enableAuditAgent": t.boolean().optional(),
            "idleTimeout": t.string().optional(),
            "runningTimeout": t.string().optional(),
            "host": t.proxy(renames["HostIn"]).optional(),
            "readinessChecks": t.array(t.proxy(renames["ReadinessCheckIn"])).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyIn"]).optional(),
        }
    ).named(renames["WorkstationConfigIn"])
    types["WorkstationConfigOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "container": t.proxy(renames["ContainerOut"]).optional(),
            "degraded": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "enableAuditAgent": t.boolean().optional(),
            "conditions": t.array(t.proxy(renames["StatusOut"])).optional(),
            "idleTimeout": t.string().optional(),
            "runningTimeout": t.string().optional(),
            "host": t.proxy(renames["HostOut"]).optional(),
            "readinessChecks": t.array(
                t.proxy(renames["ReadinessCheckOut"])
            ).optional(),
            "reconciling": t.boolean().optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "persistentDirectories": t.array(
                t.proxy(renames["PersistentDirectoryOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "encryptionKey": t.proxy(renames["CustomerEncryptionKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationConfigOut"])
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
    types["ListUsableWorkstationConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseIn"])
    types["ListUsableWorkstationConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workstationConfigs": t.array(
                t.proxy(renames["WorkstationConfigOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableWorkstationConfigsResponseOut"])
    types["GceConfidentialInstanceConfigIn"] = t.struct(
        {"enableConfidentialCompute": t.boolean().optional()}
    ).named(renames["GceConfidentialInstanceConfigIn"])
    types["GceConfidentialInstanceConfigOut"] = t.struct(
        {
            "enableConfidentialCompute": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceConfidentialInstanceConfigOut"])
    types["PrivateClusterConfigIn"] = t.struct(
        {
            "allowedProjects": t.array(t.string()).optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
        }
    ).named(renames["PrivateClusterConfigIn"])
    types["PrivateClusterConfigOut"] = t.struct(
        {
            "allowedProjects": t.array(t.string()).optional(),
            "clusterHostname": t.string().optional(),
            "serviceAttachmentUri": t.string().optional(),
            "enablePrivateEndpoint": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PrivateClusterConfigOut"])
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
    types["ListUsableWorkstationsResponseIn"] = t.struct(
        {
            "workstations": t.array(t.proxy(renames["WorkstationIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListUsableWorkstationsResponseIn"])
    types["ListUsableWorkstationsResponseOut"] = t.struct(
        {
            "workstations": t.array(t.proxy(renames["WorkstationOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUsableWorkstationsResponseOut"])
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
            "command": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "image": t.string().optional(),
            "runAsUser": t.integer().optional(),
            "workingDir": t.string().optional(),
        }
    ).named(renames["ContainerIn"])
    types["ContainerOut"] = t.struct(
        {
            "env": t.struct({"_": t.string().optional()}).optional(),
            "command": t.array(t.string()).optional(),
            "args": t.array(t.string()).optional(),
            "image": t.string().optional(),
            "runAsUser": t.integer().optional(),
            "workingDir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
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
    types["GceRegionalPersistentDiskIn"] = t.struct(
        {
            "reclaimPolicy": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "diskType": t.string().optional(),
            "fsType": t.string().optional(),
        }
    ).named(renames["GceRegionalPersistentDiskIn"])
    types["GceRegionalPersistentDiskOut"] = t.struct(
        {
            "reclaimPolicy": t.string().optional(),
            "sourceSnapshot": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "diskType": t.string().optional(),
            "fsType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceRegionalPersistentDiskOut"])
    types["WorkstationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["WorkstationIn"])
    types["WorkstationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "host": t.string().optional(),
            "updateTime": t.string().optional(),
            "reconciling": t.boolean().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "env": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkstationOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["GenerateAccessTokenRequestIn"] = t.struct(
        {"expireTime": t.string().optional(), "ttl": t.string().optional()}
    ).named(renames["GenerateAccessTokenRequestIn"])
    types["GenerateAccessTokenRequestOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateAccessTokenRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["HostIn"] = t.struct(
        {"gceInstance": t.proxy(renames["GceInstanceIn"]).optional()}
    ).named(renames["HostIn"])
    types["HostOut"] = t.struct(
        {
            "gceInstance": t.proxy(renames["GceInstanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HostOut"])
    types["GceShieldedInstanceConfigIn"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
        }
    ).named(renames["GceShieldedInstanceConfigIn"])
    types["GceShieldedInstanceConfigOut"] = t.struct(
        {
            "enableSecureBoot": t.boolean().optional(),
            "enableIntegrityMonitoring": t.boolean().optional(),
            "enableVtpm": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GceShieldedInstanceConfigOut"])
    types["PersistentDirectoryIn"] = t.struct(
        {
            "gcePd": t.proxy(renames["GceRegionalPersistentDiskIn"]).optional(),
            "mountPath": t.string().optional(),
        }
    ).named(renames["PersistentDirectoryIn"])
    types["PersistentDirectoryOut"] = t.struct(
        {
            "gcePd": t.proxy(renames["GceRegionalPersistentDiskOut"]).optional(),
            "mountPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistentDirectoryOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
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

    functions = {}
    functions["projectsLocationsWorkstationClustersGet"] = workstations.post(
        "v1beta/{parent}/workstationClusters",
        t.struct(
            {
                "parent": t.string(),
                "workstationClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "parent": t.string(),
                "workstationClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "parent": t.string(),
                "workstationClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "parent": t.string(),
                "workstationClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "parent": t.string(),
                "workstationClusterId": t.string(),
                "validateOnly": t.boolean().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "privateClusterConfig": t.proxy(
                    renames["PrivateClusterConfigIn"]
                ).optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "subnetwork": t.string().optional(),
                "network": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsCreate"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsSetIamPolicy"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsPatch"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsList"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsDelete"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGet"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsListUsable"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsGetIamPolicy"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsTestIamPermissions"
    ] = workstations.post(
        "v1beta/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsSetIamPolicy"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGenerateAccessToken"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsTestIamPermissions"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsListUsable"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStop"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsCreate"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsList"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGetIamPolicy"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsPatch"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsDelete"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsStart"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsWorkstationClustersWorkstationConfigsWorkstationsGet"
    ] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkstationOut"]),
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
    functions["projectsLocationsOperationsList"] = workstations.get(
        "v1beta/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = workstations.get(
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

    return Import(
        importer="workstations",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
