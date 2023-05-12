from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_gkebackup() -> Import:
    gkebackup = HTTPRuntime("https://gkebackup.googleapis.com/")

    renames = {
        "ErrorResponse": "_gkebackup_1_ErrorResponse",
        "BackupPlanIn": "_gkebackup_2_BackupPlanIn",
        "BackupPlanOut": "_gkebackup_3_BackupPlanOut",
        "VolumeBackupIn": "_gkebackup_4_VolumeBackupIn",
        "VolumeBackupOut": "_gkebackup_5_VolumeBackupOut",
        "LocationIn": "_gkebackup_6_LocationIn",
        "LocationOut": "_gkebackup_7_LocationOut",
        "GoogleRpcStatusIn": "_gkebackup_8_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_gkebackup_9_GoogleRpcStatusOut",
        "NamespacesIn": "_gkebackup_10_NamespacesIn",
        "NamespacesOut": "_gkebackup_11_NamespacesOut",
        "SetIamPolicyRequestIn": "_gkebackup_12_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_gkebackup_13_SetIamPolicyRequestOut",
        "ClusterResourceRestoreScopeIn": "_gkebackup_14_ClusterResourceRestoreScopeIn",
        "ClusterResourceRestoreScopeOut": "_gkebackup_15_ClusterResourceRestoreScopeOut",
        "ExprIn": "_gkebackup_16_ExprIn",
        "ExprOut": "_gkebackup_17_ExprOut",
        "RetentionPolicyIn": "_gkebackup_18_RetentionPolicyIn",
        "RetentionPolicyOut": "_gkebackup_19_RetentionPolicyOut",
        "OperationMetadataIn": "_gkebackup_20_OperationMetadataIn",
        "OperationMetadataOut": "_gkebackup_21_OperationMetadataOut",
        "NamespacedNameIn": "_gkebackup_22_NamespacedNameIn",
        "NamespacedNameOut": "_gkebackup_23_NamespacedNameOut",
        "EncryptionKeyIn": "_gkebackup_24_EncryptionKeyIn",
        "EncryptionKeyOut": "_gkebackup_25_EncryptionKeyOut",
        "NamespacedNamesIn": "_gkebackup_26_NamespacedNamesIn",
        "NamespacedNamesOut": "_gkebackup_27_NamespacedNamesOut",
        "VolumeRestoreIn": "_gkebackup_28_VolumeRestoreIn",
        "VolumeRestoreOut": "_gkebackup_29_VolumeRestoreOut",
        "SubstitutionRuleIn": "_gkebackup_30_SubstitutionRuleIn",
        "SubstitutionRuleOut": "_gkebackup_31_SubstitutionRuleOut",
        "GoogleLongrunningCancelOperationRequestIn": "_gkebackup_32_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_gkebackup_33_GoogleLongrunningCancelOperationRequestOut",
        "GroupKindIn": "_gkebackup_34_GroupKindIn",
        "GroupKindOut": "_gkebackup_35_GroupKindOut",
        "PolicyIn": "_gkebackup_36_PolicyIn",
        "PolicyOut": "_gkebackup_37_PolicyOut",
        "RestoreIn": "_gkebackup_38_RestoreIn",
        "RestoreOut": "_gkebackup_39_RestoreOut",
        "ListRestorePlansResponseIn": "_gkebackup_40_ListRestorePlansResponseIn",
        "ListRestorePlansResponseOut": "_gkebackup_41_ListRestorePlansResponseOut",
        "AuditConfigIn": "_gkebackup_42_AuditConfigIn",
        "AuditConfigOut": "_gkebackup_43_AuditConfigOut",
        "RestorePlanIn": "_gkebackup_44_RestorePlanIn",
        "RestorePlanOut": "_gkebackup_45_RestorePlanOut",
        "TestIamPermissionsRequestIn": "_gkebackup_46_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_gkebackup_47_TestIamPermissionsRequestOut",
        "ListRestoresResponseIn": "_gkebackup_48_ListRestoresResponseIn",
        "ListRestoresResponseOut": "_gkebackup_49_ListRestoresResponseOut",
        "ListVolumeRestoresResponseIn": "_gkebackup_50_ListVolumeRestoresResponseIn",
        "ListVolumeRestoresResponseOut": "_gkebackup_51_ListVolumeRestoresResponseOut",
        "ListVolumeBackupsResponseIn": "_gkebackup_52_ListVolumeBackupsResponseIn",
        "ListVolumeBackupsResponseOut": "_gkebackup_53_ListVolumeBackupsResponseOut",
        "BackupConfigIn": "_gkebackup_54_BackupConfigIn",
        "BackupConfigOut": "_gkebackup_55_BackupConfigOut",
        "GoogleLongrunningListOperationsResponseIn": "_gkebackup_56_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_gkebackup_57_GoogleLongrunningListOperationsResponseOut",
        "AuditLogConfigIn": "_gkebackup_58_AuditLogConfigIn",
        "AuditLogConfigOut": "_gkebackup_59_AuditLogConfigOut",
        "EmptyIn": "_gkebackup_60_EmptyIn",
        "EmptyOut": "_gkebackup_61_EmptyOut",
        "TestIamPermissionsResponseIn": "_gkebackup_62_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_gkebackup_63_TestIamPermissionsResponseOut",
        "ClusterMetadataIn": "_gkebackup_64_ClusterMetadataIn",
        "ClusterMetadataOut": "_gkebackup_65_ClusterMetadataOut",
        "ListBackupsResponseIn": "_gkebackup_66_ListBackupsResponseIn",
        "ListBackupsResponseOut": "_gkebackup_67_ListBackupsResponseOut",
        "ScheduleIn": "_gkebackup_68_ScheduleIn",
        "ScheduleOut": "_gkebackup_69_ScheduleOut",
        "RestoreConfigIn": "_gkebackup_70_RestoreConfigIn",
        "RestoreConfigOut": "_gkebackup_71_RestoreConfigOut",
        "ListBackupPlansResponseIn": "_gkebackup_72_ListBackupPlansResponseIn",
        "ListBackupPlansResponseOut": "_gkebackup_73_ListBackupPlansResponseOut",
        "ListLocationsResponseIn": "_gkebackup_74_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_gkebackup_75_ListLocationsResponseOut",
        "GoogleLongrunningOperationIn": "_gkebackup_76_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_gkebackup_77_GoogleLongrunningOperationOut",
        "BackupIn": "_gkebackup_78_BackupIn",
        "BackupOut": "_gkebackup_79_BackupOut",
        "BindingIn": "_gkebackup_80_BindingIn",
        "BindingOut": "_gkebackup_81_BindingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BackupPlanIn"] = t.struct(
        {
            "backupConfig": t.proxy(renames["BackupConfigIn"]).optional(),
            "description": t.string().optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyIn"]).optional(),
            "deactivated": t.boolean().optional(),
            "cluster": t.string(),
            "backupSchedule": t.proxy(renames["ScheduleIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BackupPlanIn"])
    types["BackupPlanOut"] = t.struct(
        {
            "backupConfig": t.proxy(renames["BackupConfigOut"]).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "uid": t.string().optional(),
            "protectedPodCount": t.integer().optional(),
            "retentionPolicy": t.proxy(renames["RetentionPolicyOut"]).optional(),
            "deactivated": t.boolean().optional(),
            "etag": t.string().optional(),
            "cluster": t.string(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "backupSchedule": t.proxy(renames["ScheduleOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupPlanOut"])
    types["VolumeBackupIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeBackupIn"]
    )
    types["VolumeBackupOut"] = t.struct(
        {
            "diskSizeBytes": t.string().optional(),
            "uid": t.string().optional(),
            "storageBytes": t.string().optional(),
            "completeTime": t.string().optional(),
            "etag": t.string().optional(),
            "stateMessage": t.string().optional(),
            "sourcePvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "name": t.string().optional(),
            "volumeBackupHandle": t.string().optional(),
            "updateTime": t.string().optional(),
            "format": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeBackupOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["NamespacesIn"] = t.struct(
        {"namespaces": t.array(t.string()).optional()}
    ).named(renames["NamespacesIn"])
    types["NamespacesOut"] = t.struct(
        {
            "namespaces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NamespacesOut"])
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
    types["ClusterResourceRestoreScopeIn"] = t.struct(
        {"selectedGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional()}
    ).named(renames["ClusterResourceRestoreScopeIn"])
    types["ClusterResourceRestoreScopeOut"] = t.struct(
        {
            "selectedGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterResourceRestoreScopeOut"])
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
    types["RetentionPolicyIn"] = t.struct(
        {
            "backupDeleteLockDays": t.integer().optional(),
            "backupRetainDays": t.integer().optional(),
            "locked": t.boolean().optional(),
        }
    ).named(renames["RetentionPolicyIn"])
    types["RetentionPolicyOut"] = t.struct(
        {
            "backupDeleteLockDays": t.integer().optional(),
            "backupRetainDays": t.integer().optional(),
            "locked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetentionPolicyOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["EncryptionKeyIn"] = t.struct(
        {"gcpKmsEncryptionKey": t.string().optional()}
    ).named(renames["EncryptionKeyIn"])
    types["EncryptionKeyOut"] = t.struct(
        {
            "gcpKmsEncryptionKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EncryptionKeyOut"])
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
    types["VolumeRestoreIn"] = t.struct({"_": t.string().optional()}).named(
        renames["VolumeRestoreIn"]
    )
    types["VolumeRestoreOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "name": t.string().optional(),
            "volumeBackup": t.string().optional(),
            "volumeHandle": t.string().optional(),
            "volumeType": t.string().optional(),
            "etag": t.string().optional(),
            "state": t.string().optional(),
            "targetPvc": t.proxy(renames["NamespacedNameOut"]).optional(),
            "completeTime": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeRestoreOut"])
    types["SubstitutionRuleIn"] = t.struct(
        {
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindIn"])).optional(),
            "targetNamespaces": t.array(t.string()).optional(),
            "originalValuePattern": t.string().optional(),
            "targetJsonPath": t.string(),
            "newValue": t.string().optional(),
        }
    ).named(renames["SubstitutionRuleIn"])
    types["SubstitutionRuleOut"] = t.struct(
        {
            "targetGroupKinds": t.array(t.proxy(renames["GroupKindOut"])).optional(),
            "targetNamespaces": t.array(t.string()).optional(),
            "originalValuePattern": t.string().optional(),
            "targetJsonPath": t.string(),
            "newValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubstitutionRuleOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["RestoreIn"] = t.struct(
        {
            "backup": t.string(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RestoreIn"])
    types["RestoreOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "resourcesRestoredCount": t.integer().optional(),
            "backup": t.string(),
            "volumesRestoredCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "cluster": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourcesExcludedCount": t.integer().optional(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]).optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "completeTime": t.string().optional(),
            "resourcesFailedCount": t.integer().optional(),
            "stateReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreOut"])
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
    types["RestorePlanIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cluster": t.string(),
            "restoreConfig": t.proxy(renames["RestoreConfigIn"]),
            "backupPlan": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["RestorePlanIn"])
    types["RestorePlanOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cluster": t.string(),
            "restoreConfig": t.proxy(renames["RestoreConfigOut"]),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "backupPlan": t.string(),
            "description": t.string().optional(),
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestorePlanOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListRestoresResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "restores": t.array(t.proxy(renames["RestoreIn"])).optional(),
        }
    ).named(renames["ListRestoresResponseIn"])
    types["ListRestoresResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "restores": t.array(t.proxy(renames["RestoreOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRestoresResponseOut"])
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
    types["BackupConfigIn"] = t.struct(
        {
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "includeVolumeData": t.boolean().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyIn"]).optional(),
        }
    ).named(renames["BackupConfigIn"])
    types["BackupConfigOut"] = t.struct(
        {
            "allNamespaces": t.boolean().optional(),
            "includeSecrets": t.boolean().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "includeVolumeData": t.boolean().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupConfigOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ClusterMetadataIn"] = t.struct(
        {
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
            "anthosVersion": t.string().optional(),
            "gkeVersion": t.string().optional(),
            "cluster": t.string().optional(),
            "k8sVersion": t.string().optional(),
        }
    ).named(renames["ClusterMetadataIn"])
    types["ClusterMetadataOut"] = t.struct(
        {
            "backupCrdVersions": t.struct({"_": t.string().optional()}).optional(),
            "anthosVersion": t.string().optional(),
            "gkeVersion": t.string().optional(),
            "cluster": t.string().optional(),
            "k8sVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClusterMetadataOut"])
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
    types["RestoreConfigIn"] = t.struct(
        {
            "selectedNamespaces": t.proxy(renames["NamespacesIn"]).optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeIn"]
            ).optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesIn"]).optional(),
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleIn"])
            ).optional(),
            "allNamespaces": t.boolean().optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
        }
    ).named(renames["RestoreConfigIn"])
    types["RestoreConfigOut"] = t.struct(
        {
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "clusterResourceRestoreScope": t.proxy(
                renames["ClusterResourceRestoreScopeOut"]
            ).optional(),
            "clusterResourceConflictPolicy": t.string().optional(),
            "volumeDataRestorePolicy": t.string().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "substitutionRules": t.array(
                t.proxy(renames["SubstitutionRuleOut"])
            ).optional(),
            "allNamespaces": t.boolean().optional(),
            "namespacedResourceRestoreMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RestoreConfigOut"])
    types["ListBackupPlansResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "backupPlans": t.array(t.proxy(renames["BackupPlanIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBackupPlansResponseIn"])
    types["ListBackupPlansResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "backupPlans": t.array(t.proxy(renames["BackupPlanOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBackupPlansResponseOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["BackupIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retainDays": t.integer().optional(),
            "deleteLockDays": t.integer().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["BackupIn"])
    types["BackupOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "deleteLockExpireTime": t.string().optional(),
            "retainDays": t.integer().optional(),
            "encryptionKey": t.proxy(renames["EncryptionKeyOut"]).optional(),
            "stateReason": t.string().optional(),
            "allNamespaces": t.boolean().optional(),
            "podCount": t.integer().optional(),
            "configBackupSizeBytes": t.string().optional(),
            "sizeBytes": t.string().optional(),
            "deleteLockDays": t.integer().optional(),
            "clusterMetadata": t.proxy(renames["ClusterMetadataOut"]).optional(),
            "retainExpireTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "selectedApplications": t.proxy(renames["NamespacedNamesOut"]).optional(),
            "selectedNamespaces": t.proxy(renames["NamespacesOut"]).optional(),
            "uid": t.string().optional(),
            "containsSecrets": t.boolean().optional(),
            "completeTime": t.string().optional(),
            "resourceCount": t.integer().optional(),
            "manual": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "volumeCount": t.integer().optional(),
            "containsVolumeData": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackupOut"])
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
    functions["projectsLocationsBackupPlansBackupsDelete"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsList"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsPatch"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsTestIamPermissions"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsGetIamPolicy"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsSetIamPolicy"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsCreate"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsGet"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsSetIamPolicy"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeBackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsGetIamPolicy"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeBackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsVolumeBackupsList"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeBackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsBackupPlansBackupsVolumeBackupsTestIamPermissions"
    ] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeBackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsBackupPlansBackupsVolumeBackupsGet"] = gkebackup.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeBackupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansGetIamPolicy"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansGet"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansPatch"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansDelete"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansSetIamPolicy"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansList"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansTestIamPermissions"] = gkebackup.post(
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
    functions["projectsLocationsRestorePlansRestoresGet"] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRestorePlansRestoresTestIamPermissions"
    ] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresSetIamPolicy"] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresCreate"] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresPatch"] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresDelete"] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresGetIamPolicy"] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRestorePlansRestoresList"] = gkebackup.get(
        "v1/{parent}/restores",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRestoresResponseOut"]),
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

    return Import(
        importer="gkebackup",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
