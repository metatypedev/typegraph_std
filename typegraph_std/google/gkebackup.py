from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_gkebackup() -> Import:
    gkebackup = HTTPRuntime("https://gkebackup.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkebackup_1_ErrorResponse",
        "BindingIn": "_gkebackup_2_BindingIn",
        "BindingOut": "_gkebackup_3_BindingOut",
        "SubstitutionRuleIn": "_gkebackup_4_SubstitutionRuleIn",
        "SubstitutionRuleOut": "_gkebackup_5_SubstitutionRuleOut",
        "OperationMetadataIn": "_gkebackup_6_OperationMetadataIn",
        "OperationMetadataOut": "_gkebackup_7_OperationMetadataOut",
        "ListRestorePlansResponseIn": "_gkebackup_8_ListRestorePlansResponseIn",
        "ListRestorePlansResponseOut": "_gkebackup_9_ListRestorePlansResponseOut",
        "RestorePlanIn": "_gkebackup_10_RestorePlanIn",
        "RestorePlanOut": "_gkebackup_11_RestorePlanOut",
        "PolicyIn": "_gkebackup_12_PolicyIn",
        "PolicyOut": "_gkebackup_13_PolicyOut",
        "AuditLogConfigIn": "_gkebackup_14_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkebackup_15_AuditLogConfigOut",
        "ListLocationsResponseIn": "_gkebackup_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkebackup_17_ListLocationsResponseOut",
        "ClusterResourceRestoreScopeIn": "_gkebackup_18_ClusterResourceRestoreScopeIn",
        "ClusterResourceRestoreScopeOut": "_gkebackup_19_ClusterResourceRestoreScopeOut",
        "BackupPlanIn": "_gkebackup_20_BackupPlanIn",
        "BackupPlanOut": "_gkebackup_21_BackupPlanOut",
        "LocationIn": "_gkebackup_22_LocationIn",
        "LocationOut": "_gkebackup_23_LocationOut",
        "RestoreIn": "_gkebackup_24_RestoreIn",
        "RestoreOut": "_gkebackup_25_RestoreOut",
        "ListVolumeRestoresResponseIn": "_gkebackup_26_ListVolumeRestoresResponseIn",
        "ListVolumeRestoresResponseOut": "_gkebackup_27_ListVolumeRestoresResponseOut",
        "AuditConfigIn": "_gkebackup_28_AuditConfigIn",
        "AuditConfigOut": "_gkebackup_29_AuditConfigOut",
        "ListRestoresResponseIn": "_gkebackup_30_ListRestoresResponseIn",
        "ListRestoresResponseOut": "_gkebackup_31_ListRestoresResponseOut",
        "ScheduleIn": "_gkebackup_32_ScheduleIn",
        "ScheduleOut": "_gkebackup_33_ScheduleOut",
        "ListBackupPlansResponseIn": "_gkebackup_34_ListBackupPlansResponseIn",
        "ListBackupPlansResponseOut": "_gkebackup_35_ListBackupPlansResponseOut",
        "NamespacesIn": "_gkebackup_36_NamespacesIn",
        "NamespacesOut": "_gkebackup_37_NamespacesOut",
        "NamespacedNamesIn": "_gkebackup_38_NamespacedNamesIn",
        "NamespacedNamesOut": "_gkebackup_39_NamespacedNamesOut",
        "ListVolumeBackupsResponseIn": "_gkebackup_40_ListVolumeBackupsResponseIn",
        "ListVolumeBackupsResponseOut": "_gkebackup_41_ListVolumeBackupsResponseOut",
        "ExprIn": "_gkebackup_42_ExprIn",
        "ExprOut": "_gkebackup_43_ExprOut",
        "BackupConfigIn": "_gkebackup_44_BackupConfigIn",
        "BackupConfigOut": "_gkebackup_45_BackupConfigOut",
        "BackupIn": "_gkebackup_46_BackupIn",
        "BackupOut": "_gkebackup_47_BackupOut",
        "ListBackupsResponseIn": "_gkebackup_48_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_gkebackup_49_ListBackupsResponseOut",
        "TestIamPermissionsResponseIn": "_gkebackup_50_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkebackup_51_TestIamPermissionsResponseOut",
        "NamespacedNameIn": "_gkebackup_52_NamespacedNameIn",
        "NamespacedNameOut": "_gkebackup_53_NamespacedNameOut",
        "RestoreConfigIn": "_gkebackup_54_RestoreConfigIn",
        "RestoreConfigOut": "_gkebackup_55_RestoreConfigOut",
        "GoogleRpcStatusIn": "_gkebackup_56_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkebackup_57_GoogleRpcStatusOut",
        "EmptyIn": "_gkebackup_58_EmptyIn",
        "EmptyOut": "_gkebackup_59_EmptyOut",
        "GoogleLongrunningOperationIn": "_gkebackup_60_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_gkebackup_61_GoogleLongrunningOperationOut",
        "GroupKindIn": "_gkebackup_62_GroupKindIn",
        "GroupKindOut": "_gkebackup_63_GroupKindOut",
        "TestIamPermissionsRequestIn": "_gkebackup_64_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkebackup_65_TestIamPermissionsRequestOut",
        "SetIamPolicyRequestIn": "_gkebackup_66_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkebackup_67_SetIamPolicyRequestOut",
        "ClusterMetadataIn": "_gkebackup_68_ClusterMetadataIn",
        "ClusterMetadataOut": "_gkebackup_69_ClusterMetadataOut",
        "GoogleLongrunningListOperationsResponseIn": "_gkebackup_70_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_gkebackup_71_GoogleLongrunningListOperationsResponseOut",
        "VolumeRestoreIn": "_gkebackup_72_VolumeRestoreIn",
        "VolumeRestoreOut": "_gkebackup_73_VolumeRestoreOut",
        "VolumeBackupIn": "_gkebackup_74_VolumeBackupIn",
        "VolumeBackupOut": "_gkebackup_75_VolumeBackupOut",
        "GoogleLongrunningCancelOperationRequestIn": "_gkebackup_76_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_gkebackup_77_GoogleLongrunningCancelOperationRequestOut",
        "EncryptionKeyIn": "_gkebackup_78_EncryptionKeyIn",
        "EncryptionKeyOut": "_gkebackup_79_EncryptionKeyOut",
        "RetentionPolicyIn": "_gkebackup_80_RetentionPolicyIn",
        "RetentionPolicyOut": "_gkebackup_81_RetentionPolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["SubstitutionRuleIn"] = t.struct(
        {
            "originalValuePattern": t.string().optional(),
            "newValue": t.string().optional(),
            "targetNamespaces": t.array(t.string()).optional(),
            "targetJsonPath": t.string(),
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional(),
        }
    ).named(renames["SubstitutionRuleIn"])
    types["SubstitutionRuleOut"] = t.struct(
        {
            "originalValuePattern": t.string().optional(),
            "newValue": t.string().optional(),
            "targetNamespaces": t.array(t.string()).optional(),
            "targetJsonPath": t.string(),
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubstitutionRuleOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListRestorePlansResponseIn"] = t.struct(
        {
            "restorePlans": t.array(t.proxy(renames["RestorePlanIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRestorePlansResponseIn"])
    types["ListRestorePlansResponseOut"] = t.struct(
        {
            "restorePlans": t.array(t.proxy(renames["RestorePlanOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRestorePlansResponseOut"])
    types["RestorePlanIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cluster": t.string(),
            "description": t.string().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
            "backupPlan": t.string(),
        }
    ).named(renames["RestorePlanIn"])
    types["RestorePlanOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cluster": t.string(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]),
            "backupPlan": t.string(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestorePlanOut"])
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
    types["ClusterResourceRestoreScopeIn"] = t.struct(
        {"selectedGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional()}
    ).named(renames["ClusterResourceRestoreScopeIn"])
    types["ClusterResourceRestoreScopeOut"] = t.struct(
        {
            "selectedGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterResourceRestoreScopeOut"])
    types["BackupPlanIn"] = t.struct(
        {
            "deactivated": t.boolean().optional(),
            "backupSchedule": t.proxy(renames["ScheduleIn"]).optional(),
            "cluster": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "backupConfig": t.proxy(renames["BackupConfigIn"]).optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["BackupPlanIn"])
    types["BackupPlanOut"] = t.struct(
        {
            "deactivated": t.boolean().optional(),
            "name": t.string().optional(),
            "backupSchedule": t.proxy(renames["ScheduleOut"]).optional(),
            "cluster": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "backupConfig": t.proxy(renames["BackupConfigOut"]).optional(),
            "uid": t.string().optional(),
            "protectedPodCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyOut"]).optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupPlanOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RestoreIn"] = t.struct(
        {
            "backup": t.string(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RestoreIn"])
    types["RestoreOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "resourcesFailedCount": t.integer().optional(),
            "etag": t.string().optional(),
            "resourcesExcludedCount": t.integer().optional(),
            "completeTime": t.string().optional(),
            "backup": t.string(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]).optional(),
            "stateReason": t.string().optional(),
            "resourcesRestoredCount": t.integer().optional(),
            "volumesRestoredCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cluster": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
    types["ListVolumeRestoresResponseIn"] = t.struct(
        {
            "volumeRestores": t.array(t.proxy(renames["VolumeRestoreIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVolumeRestoresResponseIn"])
    types["ListVolumeRestoresResponseOut"] = t.struct(
        {
            "volumeRestores": t.array(t.proxy(renames["VolumeRestoreOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVolumeRestoresResponseOut"])
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
    types["ListBackupPlansResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "backupPlans": t.array(t.proxy(renames["BackupPlanIn"])).optional(),
        }
    ).named(renames["ListBackupPlansResponseIn"])
    types["ListBackupPlansResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "backupPlans": t.array(t.proxy(renames["BackupPlanOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupPlansResponseOut"])
    types["NamespacesIn"] = t.struct(
        {"namespaces": t.array(t.string()).optional()}
    ).named(renames["NamespacesIn"])
    types["NamespacesOut"] = t.struct(
        {
            "namespaces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacesOut"])
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
    types["ListVolumeBackupsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "volumeBackups": t.array(t.proxy(renames["VolumeBackupIn"])).optional(),
        }
    ).named(renames["ListVolumeBackupsResponseIn"])
    types["ListVolumeBackupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "volumeBackups": t.array(t.proxy(renames["VolumeBackupOut"])).optional(),
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
    types["BackupConfigIn"] = t.struct(
        {
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyIn"]).optional(),
            "includeVolumeData": t.boolean().optional(),
        }
    ).named(renames["BackupConfigIn"])
    types["BackupConfigOut"] = t.struct(
        {
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "includeVolumeData": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigOut"])
    types["BackupIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retainDays": t.integer().optional(),
            "deleteLockDays": t.integer().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "resourceCount": t.integer().optional(),
            "sizeBytes": t.string().optional(),
            "manual": t.boolean().optional(),
            "retainExpireTime": t.string().optional(),
            "completeTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "podCount": t.integer().optional(),
            "volumeCount": t.integer().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "updateTime": t.string().optional(),
            "retainDays": t.integer().optional(),
            "deleteLockExpireTime": t.string().optional(),
            "containsVolumeData": t.boolean().optional(),
            "containsSecrets": t.boolean().optional(),
            "configBackupSizeBytes": t.string().optional(),
            "stateReason": t.string().optional(),
            "clusterMetadata": t.proxy(renames["ClusterMetadataOut"]).optional(),
            "allNamespaces": t.boolean().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "state": t.string().optional(),
            "deleteLockDays": t.integer().optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["RestoreConfigIn"] = t.struct(
        {
            "allNamespaces": t.boolean().optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeIn"]
            ).optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleIn"])
            ).optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
        }
    ).named(renames["RestoreConfigIn"])
    types["RestoreConfigOut"] = t.struct(
        {
            "allNamespaces": t.boolean().optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeOut"]
            ).optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleOut"])
            ).optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreConfigOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["ClusterMetadataIn"] = t.struct(
        {
            "anthosVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "cluster": t.string().optional(),
            "gkeVersion": t.string().optional(),
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ClusterMetadataIn"])
    types["ClusterMetadataOut"] = t.struct(
        {
            "anthosVersion": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "cluster": t.string().optional(),
            "gkeVersion": t.string().optional(),
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterMetadataOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["VolumeRestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeRestoreIn"]
    )
    types["VolumeRestoreOut"] = t.struct(
        {
            "completeTime": t.string().optional(),
            "volumeBackup": t.string().optional(),
            "volumeType": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "volumeHandle": t.string().optional(),
            "stateMessage": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "targetPvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeRestoreOut"])
    types["VolumeBackupIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeBackupIn"]
    )
    types["VolumeBackupOut"] = t.struct(
        {
            "stateMessage": t.string().optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "format": t.string().optional(),
            "storageBytes": t.string().optional(),
            "name": t.string().optional(),
            "volumeBackupHandle": t.string().optional(),
            "completeTime": t.string().optional(),
            "sourcePvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "diskSizeBytes": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeBackupOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["EncryptionKeyIn"] = t.struct(
        {"gcpKmsEncryptionKey": t.string().optional()}
    ).named(renames["EncryptionKeyIn"])
    types["EncryptionKeyOut"] = t.struct(
        {
            "gcpKmsEncryptionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionKeyOut"])
    types["RetentionPolicyIn"] = t.struct(
        {
            "backupRetainDays": t.integer().optional(),
            "backupDeleteLockDays": t.integer().optional(),
            "locked": t.boolean().optional(),
        }
    ).named(renames["RetentionPolicyIn"])
    types["RetentionPolicyOut"] = t.struct(
        {
            "backupRetainDays": t.integer().optional(),
            "backupDeleteLockDays": t.integer().optional(),
            "locked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetentionPolicyOut"])

    functions = {}
    functions["projectsLocationsGet"] = gkebackup.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDeleteOperations"] = gkebackup.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = gkebackup.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsBackupPlansSetIamPolicy"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansCreate"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansGetIamPolicy"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansTestIamPermissions"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansDelete"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansPatch"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansGet"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansList"] = gkebackup.get(
        "v1/{parent}/backupPlans",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBackupPlansResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsDelete"] = gkebackup.get(
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
    functions["projectsLocationsBackupPlansBackupsGet"] = gkebackup.get(
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
    functions["projectsLocationsBackupPlansBackupsCreate"] = gkebackup.get(
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
    functions["projectsLocationsBackupPlansBackupsPatch"] = gkebackup.get(
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
    functions["projectsLocationsBackupPlansBackupsSetIamPolicy"] = gkebackup.get(
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
    functions["projectsLocationsBackupPlansBackupsTestIamPermissions"] = gkebackup.get(
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
    functions["projectsLocationsBackupPlansBackupsList"] = gkebackup.get(
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
    functions["projectsLocationsBackupPlansBackupsGetIamPolicy"] = gkebackup.get(
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
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsGetIamPolicy"
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
    functions["projectsLocationsBackupPlansBackupsVolumeBackupsList"] = gkebackup.post(
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
        "projectsLocationsBackupPlansBackupsVolumeBackupsSetIamPolicy"
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
    functions["projectsLocationsBackupPlansBackupsVolumeBackupsGet"] = gkebackup.post(
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
        "projectsLocationsBackupPlansBackupsVolumeBackupsTestIamPermissions"
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
    functions["projectsLocationsRestorePlansCreate"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansPatch"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansGet"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansList"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansTestIamPermissions"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansGetIamPolicy"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansDelete"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansSetIamPolicy"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresPatch"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresGetIamPolicy"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresGet"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresDelete"] = gkebackup.post(
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
    functions[
        "projectsLocationsRestorePlansRestoresTestIamPermissions"
    ] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresCreate"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresList"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresSetIamPolicy"] = gkebackup.post(
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
    functions[
        "projectsLocationsRestorePlansRestoresVolumeRestoresSetIamPolicy"
    ] = gkebackup.get(
        "v1/{resource}:getIamPolicy",
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresList"
    ] = gkebackup.get(
        "v1/{resource}:getIamPolicy",
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresTestIamPermissions"
    ] = gkebackup.get(
        "v1/{resource}:getIamPolicy",
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
    functions["projectsLocationsRestorePlansRestoresVolumeRestoresGet"] = gkebackup.get(
        "v1/{resource}:getIamPolicy",
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
        "projectsLocationsRestorePlansRestoresVolumeRestoresGetIamPolicy"
    ] = gkebackup.get(
        "v1/{resource}:getIamPolicy",
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

    return Import(
        importer="gkebackup", renames=renames, types=types, functions=functions
    )
