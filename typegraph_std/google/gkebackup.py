from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_gkebackup():
    gkebackup = HTTPRuntime("https://gkebackup.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkebackup_1_ErrorResponse",
        "VolumeRestoreIn": "_gkebackup_2_VolumeRestoreIn",
        "VolumeRestoreOut": "_gkebackup_3_VolumeRestoreOut",
        "SubstitutionRuleIn": "_gkebackup_4_SubstitutionRuleIn",
        "SubstitutionRuleOut": "_gkebackup_5_SubstitutionRuleOut",
        "GroupKindIn": "_gkebackup_6_GroupKindIn",
        "GroupKindOut": "_gkebackup_7_GroupKindOut",
        "BackupConfigIn": "_gkebackup_8_BackupConfigIn",
        "BackupConfigOut": "_gkebackup_9_BackupConfigOut",
        "RestoreConfigIn": "_gkebackup_10_RestoreConfigIn",
        "RestoreConfigOut": "_gkebackup_11_RestoreConfigOut",
        "ListLocationsResponseIn": "_gkebackup_12_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkebackup_13_ListLocationsResponseOut",
        "ExprIn": "_gkebackup_14_ExprIn",
        "ExprOut": "_gkebackup_15_ExprOut",
        "ResourceFilterIn": "_gkebackup_16_ResourceFilterIn",
        "ResourceFilterOut": "_gkebackup_17_ResourceFilterOut",
        "BindingIn": "_gkebackup_18_BindingIn",
        "BindingOut": "_gkebackup_19_BindingOut",
        "VolumeBackupIn": "_gkebackup_20_VolumeBackupIn",
        "VolumeBackupOut": "_gkebackup_21_VolumeBackupOut",
        "RestorePlanIn": "_gkebackup_22_RestorePlanIn",
        "RestorePlanOut": "_gkebackup_23_RestorePlanOut",
        "RetentionPolicyIn": "_gkebackup_24_RetentionPolicyIn",
        "RetentionPolicyOut": "_gkebackup_25_RetentionPolicyOut",
        "BackupPlanIn": "_gkebackup_26_BackupPlanIn",
        "BackupPlanOut": "_gkebackup_27_BackupPlanOut",
        "NamespacedNamesIn": "_gkebackup_28_NamespacedNamesIn",
        "NamespacedNamesOut": "_gkebackup_29_NamespacedNamesOut",
        "TransformationRuleIn": "_gkebackup_30_TransformationRuleIn",
        "TransformationRuleOut": "_gkebackup_31_TransformationRuleOut",
        "GoogleLongrunningListOperationsResponseIn": "_gkebackup_32_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_gkebackup_33_GoogleLongrunningListOperationsResponseOut",
        "AuditLogConfigIn": "_gkebackup_34_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkebackup_35_AuditLogConfigOut",
        "ListRestorePlansResponseIn": "_gkebackup_36_ListRestorePlansResponseIn",
        "ListRestorePlansResponseOut": "_gkebackup_37_ListRestorePlansResponseOut",
        "GoogleLongrunningCancelOperationRequestIn": "_gkebackup_38_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_gkebackup_39_GoogleLongrunningCancelOperationRequestOut",
        "SetIamPolicyRequestIn": "_gkebackup_40_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkebackup_41_SetIamPolicyRequestOut",
        "ClusterMetadataIn": "_gkebackup_42_ClusterMetadataIn",
        "ClusterMetadataOut": "_gkebackup_43_ClusterMetadataOut",
        "EmptyIn": "_gkebackup_44_EmptyIn",
        "EmptyOut": "_gkebackup_45_EmptyOut",
        "RestoreIn": "_gkebackup_46_RestoreIn",
        "RestoreOut": "_gkebackup_47_RestoreOut",
        "PolicyIn": "_gkebackup_48_PolicyIn",
        "PolicyOut": "_gkebackup_49_PolicyOut",
        "ListVolumeRestoresResponseIn": "_gkebackup_50_ListVolumeRestoresResponseIn",
        "ListVolumeRestoresResponseOut": "_gkebackup_51_ListVolumeRestoresResponseOut",
        "BackupIn": "_gkebackup_52_BackupIn",
        "BackupOut": "_gkebackup_53_BackupOut",
        "ListRestoresResponseIn": "_gkebackup_54_ListRestoresResponseIn",
        "ListRestoresResponseOut": "_gkebackup_55_ListRestoresResponseOut",
        "TestIamPermissionsResponseIn": "_gkebackup_56_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkebackup_57_TestIamPermissionsResponseOut",
        "ListBackupPlansResponseIn": "_gkebackup_58_ListBackupPlansResponseIn",
        "ListBackupPlansResponseOut": "_gkebackup_59_ListBackupPlansResponseOut",
        "OperationMetadataIn": "_gkebackup_60_OperationMetadataIn",
        "OperationMetadataOut": "_gkebackup_61_OperationMetadataOut",
        "GoogleRpcStatusIn": "_gkebackup_62_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkebackup_63_GoogleRpcStatusOut",
        "TestIamPermissionsRequestIn": "_gkebackup_64_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkebackup_65_TestIamPermissionsRequestOut",
        "ScheduleIn": "_gkebackup_66_ScheduleIn",
        "ScheduleOut": "_gkebackup_67_ScheduleOut",
        "NamespacedNameIn": "_gkebackup_68_NamespacedNameIn",
        "NamespacedNameOut": "_gkebackup_69_NamespacedNameOut",
        "NamespacesIn": "_gkebackup_70_NamespacesIn",
        "NamespacesOut": "_gkebackup_71_NamespacesOut",
        "GoogleLongrunningOperationIn": "_gkebackup_72_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_gkebackup_73_GoogleLongrunningOperationOut",
        "ListVolumeBackupsResponseIn": "_gkebackup_74_ListVolumeBackupsResponseIn",
        "ListVolumeBackupsResponseOut": "_gkebackup_75_ListVolumeBackupsResponseOut",
        "ClusterResourceRestoreScopeIn": "_gkebackup_76_ClusterResourceRestoreScopeIn",
        "ClusterResourceRestoreScopeOut": "_gkebackup_77_ClusterResourceRestoreScopeOut",
        "AuditConfigIn": "_gkebackup_78_AuditConfigIn",
        "AuditConfigOut": "_gkebackup_79_AuditConfigOut",
        "TransformationRuleActionIn": "_gkebackup_80_TransformationRuleActionIn",
        "TransformationRuleActionOut": "_gkebackup_81_TransformationRuleActionOut",
        "EncryptionKeyIn": "_gkebackup_82_EncryptionKeyIn",
        "EncryptionKeyOut": "_gkebackup_83_EncryptionKeyOut",
        "LocationIn": "_gkebackup_84_LocationIn",
        "LocationOut": "_gkebackup_85_LocationOut",
        "ListBackupsResponseIn": "_gkebackup_86_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_gkebackup_87_ListBackupsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VolumeRestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeRestoreIn"]
    )
    types["VolumeRestoreOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "volumeType": t.string().optional(),
            "volumeHandle": t.string().optional(),
            "targetPvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "stateMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "volumeBackup": t.string().optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeRestoreOut"])
    types["SubstitutionRuleIn"] = t.struct(
        {
            "targetNamespaces": t.array(t.string()).optional(),
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional(),
            "newValue": t.string().optional(),
            "targetJsonPath": t.string(),
            "originalValuePattern": t.string().optional(),
        }
    ).named(renames["SubstitutionRuleIn"])
    types["SubstitutionRuleOut"] = t.struct(
        {
            "targetNamespaces": t.array(t.string()).optional(),
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "newValue": t.string().optional(),
            "targetJsonPath": t.string(),
            "originalValuePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubstitutionRuleOut"])
    types["GroupKindIn"] = t.struct(
        {"resourceGroup": t.string().optional(), "resourceKind": t.string().optional()}
    ).named(renames["GroupKindIn"])
    types["GroupKindOut"] = t.struct(
        {
            "resourceGroup": t.string().optional(),
            "resourceKind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupKindOut"])
    types["BackupConfigIn"] = t.struct(
        {
            "includeVolumeData": t.boolean().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyIn"]).optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
        }
    ).named(renames["BackupConfigIn"])
    types["BackupConfigOut"] = t.struct(
        {
            "includeVolumeData": t.boolean().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigOut"])
    types["RestoreConfigIn"] = t.struct(
        {
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleIn"])
            ).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "excludedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeIn"]
            ).optional(),
            "noNamespaces": t.boolean().optional(),
            "allNamespaces": t.boolean().optional(),
            "transformationRules": t.array(
                t.proxy(renames["TransformationRuleIn"])
            ).optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
        }
    ).named(renames["RestoreConfigIn"])
    types["RestoreConfigOut"] = t.struct(
        {
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleOut"])
            ).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "excludedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeOut"]
            ).optional(),
            "noNamespaces": t.boolean().optional(),
            "allNamespaces": t.boolean().optional(),
            "transformationRules": t.array(
                t.proxy(renames["TransformationRuleOut"])
            ).optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreConfigOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ResourceFilterIn"] = t.struct(
        {
            "groupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional(),
            "jsonPath": t.string().optional(),
            "namespaces": t.array(t.string()).optional(),
        }
    ).named(renames["ResourceFilterIn"])
    types["ResourceFilterOut"] = t.struct(
        {
            "groupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "jsonPath": t.string().optional(),
            "namespaces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceFilterOut"])
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
    types["VolumeBackupIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeBackupIn"]
    )
    types["VolumeBackupOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "volumeBackupHandle": t.string().optional(),
            "uid": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "format": t.string().optional(),
            "state": t.string().optional(),
            "storageBytes": t.string().optional(),
            "name": t.string().optional(),
            "sourcePvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "completeTime": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeBackupOut"])
    types["RestorePlanIn"] = t.struct(
        {
            "description": t.string().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
            "backupPlan": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cluster": t.string(),
        }
    ).named(renames["RestorePlanIn"])
    types["RestorePlanOut"] = t.struct(
        {
            "name": t.string().optional(),
            "stateReason": t.string().optional(),
            "description": t.string().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]),
            "backupPlan": t.string(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "cluster": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestorePlanOut"])
    types["RetentionPolicyIn"] = t.struct(
        {
            "locked": t.boolean().optional(),
            "backupDeleteLockDays": t.integer().optional(),
            "backupRetainDays": t.integer().optional(),
        }
    ).named(renames["RetentionPolicyIn"])
    types["RetentionPolicyOut"] = t.struct(
        {
            "locked": t.boolean().optional(),
            "backupDeleteLockDays": t.integer().optional(),
            "backupRetainDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetentionPolicyOut"])
    types["BackupPlanIn"] = t.struct(
        {
            "backupConfig": t.proxy(renames["BackupConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "deactivated": t.boolean().optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyIn"]).optional(),
            "backupSchedule": t.proxy(renames["ScheduleIn"]).optional(),
            "cluster": t.string(),
        }
    ).named(renames["BackupPlanIn"])
    types["BackupPlanOut"] = t.struct(
        {
            "backupConfig": t.proxy(renames["BackupConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "protectedPodCount": t.integer().optional(),
            "description": t.string().optional(),
            "deactivated": t.boolean().optional(),
            "stateReason": t.string().optional(),
            "updateTime": t.string().optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyOut"]).optional(),
            "backupSchedule": t.proxy(renames["ScheduleOut"]).optional(),
            "cluster": t.string(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupPlanOut"])
    types["NamespacedNamesIn"] = t.struct(
        {"namespacedNames": t.array(t.proxy(renames["NamespacedNameIn"])).optional()}
    ).named(renames["NamespacedNamesIn"])
    types["NamespacedNamesOut"] = t.struct(
        {
            "namespacedNames": t.array(
                t.proxy(renames["NamespacedNameOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacedNamesOut"])
    types["TransformationRuleIn"] = t.struct(
        {
            "resourceFilter": t.proxy(renames["ResourceFilterIn"]).optional(),
            "description": t.string().optional(),
            "fieldActions": t.array(t.proxy(renames["TransformationRuleActionIn"])),
        }
    ).named(renames["TransformationRuleIn"])
    types["TransformationRuleOut"] = t.struct(
        {
            "resourceFilter": t.proxy(renames["ResourceFilterOut"]).optional(),
            "description": t.string().optional(),
            "fieldActions": t.array(t.proxy(renames["TransformationRuleActionOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransformationRuleOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
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
    types["ListRestorePlansResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "restorePlans": t.array(t.proxy(renames["RestorePlanIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRestorePlansResponseIn"])
    types["ListRestorePlansResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "restorePlans": t.array(t.proxy(renames["RestorePlanOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRestorePlansResponseOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
    types["ClusterMetadataIn"] = t.struct(
        {
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
            "anthosVersion": t.string().optional(),
            "gkeVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "cluster": t.string().optional(),
        }
    ).named(renames["ClusterMetadataIn"])
    types["ClusterMetadataOut"] = t.struct(
        {
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
            "anthosVersion": t.string().optional(),
            "gkeVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "cluster": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["RestoreIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "backup": t.string(),
        }
    ).named(renames["RestoreIn"])
    types["RestoreOut"] = t.struct(
        {
            "volumesRestoredCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "description": t.string().optional(),
            "resourcesRestoredCount": t.integer().optional(),
            "cluster": t.string().optional(),
            "etag": t.string().optional(),
            "backup": t.string(),
            "resourcesExcludedCount": t.integer().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateReason": t.string().optional(),
            "completeTime": t.string().optional(),
            "createTime": t.string().optional(),
            "resourcesFailedCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListVolumeRestoresResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "volumeRestores": t.array(t.proxy(renames["VolumeRestoreIn"])).optional(),
        }
    ).named(renames["ListVolumeRestoresResponseIn"])
    types["ListVolumeRestoresResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "volumeRestores": t.array(t.proxy(renames["VolumeRestoreOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVolumeRestoresResponseOut"])
    types["BackupIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "deleteLockDays": t.integer().optional(),
            "retainDays": t.integer().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "resourceCount": t.integer().optional(),
            "completeTime": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "manual": t.boolean().optional(),
            "allNamespaces": t.boolean().optional(),
            "etag": t.string().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "configBackupSizeBytes": t.string().optional(),
            "retainExpireTime": t.string().optional(),
            "clusterMetadata": t.proxy(renames["ClusterMetadataOut"]).optional(),
            "updateTime": t.string().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "containsSecrets": t.boolean().optional(),
            "description": t.string().optional(),
            "deleteLockDays": t.integer().optional(),
            "containsVolumeData": t.boolean().optional(),
            "createTime": t.string().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "retainDays": t.integer().optional(),
            "deleteLockExpireTime": t.string().optional(),
            "uid": t.string().optional(),
            "stateReason": t.string().optional(),
            "volumeCount": t.integer().optional(),
            "state": t.string().optional(),
            "podCount": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
    types["ListRestoresResponseIn"] = t.struct(
        {
            "restores": t.array(t.proxy(renames["RestoreIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRestoresResponseIn"])
    types["ListRestoresResponseOut"] = t.struct(
        {
            "restores": t.array(t.proxy(renames["RestoreOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRestoresResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListBackupPlansResponseIn"] = t.struct(
        {
            "backupPlans": t.array(t.proxy(renames["BackupPlanIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBackupPlansResponseIn"])
    types["ListBackupPlansResponseOut"] = t.struct(
        {
            "backupPlans": t.array(t.proxy(renames["BackupPlanOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupPlansResponseOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ScheduleIn"] = t.struct(
        {"paused": t.boolean().optional(), "cronSchedule": t.string().optional()}
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "paused": t.boolean().optional(),
            "cronSchedule": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["NamespacedNameIn"] = t.struct(
        {"namespace": t.string().optional(), "name": t.string().optional()}
    ).named(renames["NamespacedNameIn"])
    types["NamespacedNameOut"] = t.struct(
        {
            "namespace": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacedNameOut"])
    types["NamespacesIn"] = t.struct(
        {"namespaces": t.array(t.string()).optional()}
    ).named(renames["NamespacesIn"])
    types["NamespacesOut"] = t.struct(
        {
            "namespaces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacesOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["ListVolumeBackupsResponseIn"] = t.struct(
        {
            "volumeBackups": t.array(t.proxy(renames["VolumeBackupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVolumeBackupsResponseIn"])
    types["ListVolumeBackupsResponseOut"] = t.struct(
        {
            "volumeBackups": t.array(t.proxy(renames["VolumeBackupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVolumeBackupsResponseOut"])
    types["ClusterResourceRestoreScopeIn"] = t.struct(
        {
            "noGroupKinds": t.boolean().optional(),
            "allGroupKinds": t.boolean().optional(),
            "selectedGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional(),
            "excludedGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional(),
        }
    ).named(renames["ClusterResourceRestoreScopeIn"])
    types["ClusterResourceRestoreScopeOut"] = t.struct(
        {
            "noGroupKinds": t.boolean().optional(),
            "allGroupKinds": t.boolean().optional(),
            "selectedGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "excludedGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterResourceRestoreScopeOut"])
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
    types["TransformationRuleActionIn"] = t.struct(
        {
            "fromPath": t.string().optional(),
            "op": t.string(),
            "value": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["TransformationRuleActionIn"])
    types["TransformationRuleActionOut"] = t.struct(
        {
            "fromPath": t.string().optional(),
            "op": t.string(),
            "value": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransformationRuleActionOut"])
    types["EncryptionKeyIn"] = t.struct(
        {"gcpKmsEncryptionKey": t.string().optional()}
    ).named(renames["EncryptionKeyIn"])
    types["EncryptionKeyOut"] = t.struct(
        {
            "gcpKmsEncryptionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionKeyOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = gkebackup.delete(
        "v1/{name}/operations",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = gkebackup.delete(
        "v1/{name}/operations",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeleteOperations"] = gkebackup.delete(
        "v1/{name}/operations",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = gkebackup.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = gkebackup.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = gkebackup.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansTestIamPermissions"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansCreate"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansList"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansGetIamPolicy"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansGet"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansSetIamPolicy"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansPatch"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansDelete"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsSetIamPolicy"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsList"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsGetIamPolicy"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsGet"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsTestIamPermissions"
    ] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsCreate"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsPatch"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsDelete"] = gkebackup.delete(
        "v1/{name}",
        t.struct(
            {
                "etag": t.string().optional(),
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsVolumeBackupsGet"] = gkebackup.get(
        "v1/{parent}/volumeBackups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVolumeBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsSetIamPolicy"
    ] = gkebackup.get(
        "v1/{parent}/volumeBackups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVolumeBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsTestIamPermissions"
    ] = gkebackup.get(
        "v1/{parent}/volumeBackups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVolumeBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsGetIamPolicy"
    ] = gkebackup.get(
        "v1/{parent}/volumeBackups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVolumeBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsVolumeBackupsList"] = gkebackup.get(
        "v1/{parent}/volumeBackups",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVolumeBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansCreate"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansDelete"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansGet"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansGetIamPolicy"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansList"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansPatch"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansTestIamPermissions"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansSetIamPolicy"] = gkebackup.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresDelete"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresGetIamPolicy"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresList"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresCreate"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRestorePlansRestoresTestIamPermissions"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresPatch"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresSetIamPolicy"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresGet"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["RestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRestorePlansRestoresVolumeRestoresTestIamPermissions"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeRestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRestorePlansRestoresVolumeRestoresList"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeRestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRestorePlansRestoresVolumeRestoresSetIamPolicy"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeRestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRestorePlansRestoresVolumeRestoresGetIamPolicy"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeRestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresVolumeRestoresGet"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeRestoreOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkebackup",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
