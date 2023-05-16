from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_gkebackup() -> Import:
    gkebackup = HTTPRuntime("https://gkebackup.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkebackup_1_ErrorResponse",
        "RestorePlanIn": "_gkebackup_2_RestorePlanIn",
        "RestorePlanOut": "_gkebackup_3_RestorePlanOut",
        "PolicyIn": "_gkebackup_4_PolicyIn",
        "PolicyOut": "_gkebackup_5_PolicyOut",
        "ListBackupPlansResponseIn": "_gkebackup_6_ListBackupPlansResponseIn",
        "ListBackupPlansResponseOut": "_gkebackup_7_ListBackupPlansResponseOut",
        "ListRestorePlansResponseIn": "_gkebackup_8_ListRestorePlansResponseIn",
        "ListRestorePlansResponseOut": "_gkebackup_9_ListRestorePlansResponseOut",
        "AuditLogConfigIn": "_gkebackup_10_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkebackup_11_AuditLogConfigOut",
        "ClusterMetadataIn": "_gkebackup_12_ClusterMetadataIn",
        "ClusterMetadataOut": "_gkebackup_13_ClusterMetadataOut",
        "NamespacedNamesIn": "_gkebackup_14_NamespacedNamesIn",
        "NamespacedNamesOut": "_gkebackup_15_NamespacedNamesOut",
        "EmptyIn": "_gkebackup_16_EmptyIn",
        "EmptyOut": "_gkebackup_17_EmptyOut",
        "ListVolumeBackupsResponseIn": "_gkebackup_18_ListVolumeBackupsResponseIn",
        "ListVolumeBackupsResponseOut": "_gkebackup_19_ListVolumeBackupsResponseOut",
        "ExprIn": "_gkebackup_20_ExprIn",
        "ExprOut": "_gkebackup_21_ExprOut",
        "SubstitutionRuleIn": "_gkebackup_22_SubstitutionRuleIn",
        "SubstitutionRuleOut": "_gkebackup_23_SubstitutionRuleOut",
        "RetentionPolicyIn": "_gkebackup_24_RetentionPolicyIn",
        "RetentionPolicyOut": "_gkebackup_25_RetentionPolicyOut",
        "ListBackupsResponseIn": "_gkebackup_26_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_gkebackup_27_ListBackupsResponseOut",
        "BindingIn": "_gkebackup_28_BindingIn",
        "BindingOut": "_gkebackup_29_BindingOut",
        "ClusterResourceRestoreScopeIn": "_gkebackup_30_ClusterResourceRestoreScopeIn",
        "ClusterResourceRestoreScopeOut": "_gkebackup_31_ClusterResourceRestoreScopeOut",
        "NamespacesIn": "_gkebackup_32_NamespacesIn",
        "NamespacesOut": "_gkebackup_33_NamespacesOut",
        "VolumeBackupIn": "_gkebackup_34_VolumeBackupIn",
        "VolumeBackupOut": "_gkebackup_35_VolumeBackupOut",
        "TestIamPermissionsResponseIn": "_gkebackup_36_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkebackup_37_TestIamPermissionsResponseOut",
        "ListRestoresResponseIn": "_gkebackup_38_ListRestoresResponseIn",
        "ListRestoresResponseOut": "_gkebackup_39_ListRestoresResponseOut",
        "BackupPlanIn": "_gkebackup_40_BackupPlanIn",
        "BackupPlanOut": "_gkebackup_41_BackupPlanOut",
        "RestoreIn": "_gkebackup_42_RestoreIn",
        "RestoreOut": "_gkebackup_43_RestoreOut",
        "LocationIn": "_gkebackup_44_LocationIn",
        "LocationOut": "_gkebackup_45_LocationOut",
        "VolumeRestoreIn": "_gkebackup_46_VolumeRestoreIn",
        "VolumeRestoreOut": "_gkebackup_47_VolumeRestoreOut",
        "TestIamPermissionsRequestIn": "_gkebackup_48_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkebackup_49_TestIamPermissionsRequestOut",
        "BackupConfigIn": "_gkebackup_50_BackupConfigIn",
        "BackupConfigOut": "_gkebackup_51_BackupConfigOut",
        "BackupIn": "_gkebackup_52_BackupIn",
        "BackupOut": "_gkebackup_53_BackupOut",
        "SetIamPolicyRequestIn": "_gkebackup_54_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkebackup_55_SetIamPolicyRequestOut",
        "ScheduleIn": "_gkebackup_56_ScheduleIn",
        "ScheduleOut": "_gkebackup_57_ScheduleOut",
        "NamespacedNameIn": "_gkebackup_58_NamespacedNameIn",
        "NamespacedNameOut": "_gkebackup_59_NamespacedNameOut",
        "GoogleLongrunningOperationIn": "_gkebackup_60_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_gkebackup_61_GoogleLongrunningOperationOut",
        "EncryptionKeyIn": "_gkebackup_62_EncryptionKeyIn",
        "EncryptionKeyOut": "_gkebackup_63_EncryptionKeyOut",
        "ListLocationsResponseIn": "_gkebackup_64_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkebackup_65_ListLocationsResponseOut",
        "ListVolumeRestoresResponseIn": "_gkebackup_66_ListVolumeRestoresResponseIn",
        "ListVolumeRestoresResponseOut": "_gkebackup_67_ListVolumeRestoresResponseOut",
        "RestoreConfigIn": "_gkebackup_68_RestoreConfigIn",
        "RestoreConfigOut": "_gkebackup_69_RestoreConfigOut",
        "GroupKindIn": "_gkebackup_70_GroupKindIn",
        "GroupKindOut": "_gkebackup_71_GroupKindOut",
        "OperationMetadataIn": "_gkebackup_72_OperationMetadataIn",
        "OperationMetadataOut": "_gkebackup_73_OperationMetadataOut",
        "AuditConfigIn": "_gkebackup_74_AuditConfigIn",
        "AuditConfigOut": "_gkebackup_75_AuditConfigOut",
        "GoogleLongrunningListOperationsResponseIn": "_gkebackup_76_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_gkebackup_77_GoogleLongrunningListOperationsResponseOut",
        "GoogleRpcStatusIn": "_gkebackup_78_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkebackup_79_GoogleRpcStatusOut",
        "GoogleLongrunningCancelOperationRequestIn": "_gkebackup_80_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_gkebackup_81_GoogleLongrunningCancelOperationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RestorePlanIn"] = t.struct(
        {
            "cluster": t.string(),
            "backupPlan": t.string(),
            "description": t.string().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RestorePlanIn"])
    types["RestorePlanOut"] = t.struct(
        {
            "cluster": t.string(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "backupPlan": t.string(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestorePlanOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListBackupPlansResponseIn"] = t.struct(
        {
            "backupPlans": t.array(t.proxy(renames["BackupPlanIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListBackupPlansResponseIn"])
    types["ListBackupPlansResponseOut"] = t.struct(
        {
            "backupPlans": t.array(t.proxy(renames["BackupPlanOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupPlansResponseOut"])
    types["ListRestorePlansResponseIn"] = t.struct(
        {
            "restorePlans": t.array(t.proxy(renames["RestorePlanIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListRestorePlansResponseIn"])
    types["ListRestorePlansResponseOut"] = t.struct(
        {
            "restorePlans": t.array(t.proxy(renames["RestorePlanOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRestorePlansResponseOut"])
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
    types["ClusterMetadataIn"] = t.struct(
        {
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
            "anthosVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "cluster": t.string().optional(),
            "gkeVersion": t.string().optional(),
        }
    ).named(renames["ClusterMetadataIn"])
    types["ClusterMetadataOut"] = t.struct(
        {
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
            "anthosVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "cluster": t.string().optional(),
            "gkeVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterMetadataOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["SubstitutionRuleIn"] = t.struct(
        {
            "newValue": t.string().optional(),
            "targetJsonPath": t.string(),
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional(),
            "originalValuePattern": t.string().optional(),
            "targetNamespaces": t.array(t.string()).optional(),
        }
    ).named(renames["SubstitutionRuleIn"])
    types["SubstitutionRuleOut"] = t.struct(
        {
            "newValue": t.string().optional(),
            "targetJsonPath": t.string(),
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "originalValuePattern": t.string().optional(),
            "targetNamespaces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubstitutionRuleOut"])
    types["RetentionPolicyIn"] = t.struct(
        {
            "backupRetainDays": t.integer().optional(),
            "locked": t.boolean().optional(),
            "backupDeleteLockDays": t.integer().optional(),
        }
    ).named(renames["RetentionPolicyIn"])
    types["RetentionPolicyOut"] = t.struct(
        {
            "backupRetainDays": t.integer().optional(),
            "locked": t.boolean().optional(),
            "backupDeleteLockDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetentionPolicyOut"])
    types["ListBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupIn"])).optional(),
        }
    ).named(renames["ListBackupsResponseIn"])
    types["ListBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "backups": t.array(t.proxy(renames["BackupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupsResponseOut"])
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
    types["ClusterResourceRestoreScopeIn"] = t.struct(
        {"selectedGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional()}
    ).named(renames["ClusterResourceRestoreScopeIn"])
    types["ClusterResourceRestoreScopeOut"] = t.struct(
        {
            "selectedGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterResourceRestoreScopeOut"])
    types["NamespacesIn"] = t.struct(
        {"namespaces": t.array(t.string()).optional()}
    ).named(renames["NamespacesIn"])
    types["NamespacesOut"] = t.struct(
        {
            "namespaces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacesOut"])
    types["VolumeBackupIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeBackupIn"]
    )
    types["VolumeBackupOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "storageBytes": t.string().optional(),
            "stateMessage": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "completeTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "format": t.string().optional(),
            "etag": t.string().optional(),
            "sourcePvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "volumeBackupHandle": t.string().optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeBackupOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["BackupPlanIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyIn"]).optional(),
            "deactivated": t.boolean().optional(),
            "backupSchedule": t.proxy(renames["ScheduleIn"]).optional(),
            "cluster": t.string(),
            "backupConfig": t.proxy(renames["BackupConfigIn"]).optional(),
        }
    ).named(renames["BackupPlanIn"])
    types["BackupPlanOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "protectedPodCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyOut"]).optional(),
            "deactivated": t.boolean().optional(),
            "backupSchedule": t.proxy(renames["ScheduleOut"]).optional(),
            "cluster": t.string(),
            "etag": t.string().optional(),
            "backupConfig": t.proxy(renames["BackupConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupPlanOut"])
    types["RestoreIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "backup": t.string(),
        }
    ).named(renames["RestoreIn"])
    types["RestoreOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "resourcesFailedCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "volumesRestoredCount": t.integer().optional(),
            "description": t.string().optional(),
            "uid": t.string().optional(),
            "backup": t.string(),
            "resourcesRestoredCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]).optional(),
            "cluster": t.string().optional(),
            "state": t.string().optional(),
            "resourcesExcludedCount": t.integer().optional(),
            "etag": t.string().optional(),
            "stateReason": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["VolumeRestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeRestoreIn"]
    )
    types["VolumeRestoreOut"] = t.struct(
        {
            "volumeBackup": t.string().optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "volumeHandle": t.string().optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "volumeType": t.string().optional(),
            "targetPvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeRestoreOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["BackupConfigIn"] = t.struct(
        {
            "includeVolumeData": t.boolean().optional(),
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyIn"]).optional(),
        }
    ).named(renames["BackupConfigIn"])
    types["BackupConfigOut"] = t.struct(
        {
            "includeVolumeData": t.boolean().optional(),
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigOut"])
    types["BackupIn"] = t.struct(
        {
            "retainDays": t.integer().optional(),
            "deleteLockDays": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "podCount": t.integer().optional(),
            "retainDays": t.integer().optional(),
            "resourceCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "retainExpireTime": t.string().optional(),
            "deleteLockDays": t.integer().optional(),
            "state": t.string().optional(),
            "allNamespaces": t.boolean().optional(),
            "containsSecrets": t.boolean().optional(),
            "deleteLockExpireTime": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "createTime": t.string().optional(),
            "clusterMetadata": t.proxy(renames["ClusterMetadataOut"]).optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "uid": t.string().optional(),
            "volumeCount": t.integer().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "configBackupSizeBytes": t.string().optional(),
            "name": t.string().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "manual": t.boolean().optional(),
            "stateReason": t.string().optional(),
            "description": t.string().optional(),
            "containsVolumeData": t.boolean().optional(),
            "etag": t.string().optional(),
            "completeTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    types["ScheduleIn"] = t.struct(
        {"cronSchedule": t.string().optional(), "paused": t.boolean().optional()}
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "cronSchedule": t.string().optional(),
            "paused": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["NamespacedNameIn"] = t.struct(
        {"name": t.string().optional(), "namespace": t.string().optional()}
    ).named(renames["NamespacedNameIn"])
    types["NamespacedNameOut"] = t.struct(
        {
            "name": t.string().optional(),
            "namespace": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacedNameOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["EncryptionKeyIn"] = t.struct(
        {"gcpKmsEncryptionKey": t.string().optional()}
    ).named(renames["EncryptionKeyIn"])
    types["EncryptionKeyOut"] = t.struct(
        {
            "gcpKmsEncryptionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionKeyOut"])
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
    types["RestoreConfigIn"] = t.struct(
        {
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeIn"]
            ).optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleIn"])
            ).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
            "allNamespaces": t.boolean().optional(),
        }
    ).named(renames["RestoreConfigIn"])
    types["RestoreConfigOut"] = t.struct(
        {
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeOut"]
            ).optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleOut"])
            ).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "allNamespaces": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreConfigOut"])
    types["GroupKindIn"] = t.struct(
        {"resourceKind": t.string().optional(), "resourceGroup": t.string().optional()}
    ).named(renames["GroupKindIn"])
    types["GroupKindOut"] = t.struct(
        {
            "resourceKind": t.string().optional(),
            "resourceGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupKindOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = gkebackup.delete(
        "v1/{name}/operations",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = gkebackup.delete(
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
    functions["projectsLocationsOperationsGet"] = gkebackup.post(
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
    functions["projectsLocationsOperationsList"] = gkebackup.post(
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
    functions["projectsLocationsOperationsCancel"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansCreate"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansList"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansGet"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansGetIamPolicy"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansSetIamPolicy"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansDelete"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansTestIamPermissions"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansPatch"] = gkebackup.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "cluster": t.string(),
                "backupPlan": t.string(),
                "description": t.string().optional(),
                "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
    functions["projectsLocationsRestorePlansRestoresGetIamPolicy"] = gkebackup.get(
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
    functions["projectsLocationsRestorePlansRestoresDelete"] = gkebackup.get(
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresGet"
    ] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresGetIamPolicy"
    ] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresList"
    ] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresSetIamPolicy"
    ] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresTestIamPermissions"
    ] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansList"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansPatch"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansGet"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansGetIamPolicy"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansDelete"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansCreate"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansSetIamPolicy"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansTestIamPermissions"] = gkebackup.post(
        "v1/{resource}:testIamPermissions",
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
    functions["projectsLocationsBackupPlansBackupsTestIamPermissions"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsDelete"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsSetIamPolicy"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsPatch"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsGetIamPolicy"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsList"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsGet"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsCreate"] = gkebackup.post(
        "v1/{parent}/backups",
        t.struct(
            {
                "backupId": t.string().optional(),
                "parent": t.string(),
                "retainDays": t.integer().optional(),
                "deleteLockDays": t.integer().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsGetIamPolicy"
    ] = gkebackup.get(
        "v1/{parent}/volumeBackups",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVolumeBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsVolumeBackupsGet"] = gkebackup.get(
        "v1/{parent}/volumeBackups",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVolumeBackupsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="gkebackup",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
