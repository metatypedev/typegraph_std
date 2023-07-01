from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_secretmanager():
    secretmanager = HTTPRuntime("https://secretmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_secretmanager_1_ErrorResponse",
        "ExprIn": "_secretmanager_2_ExprIn",
        "ExprOut": "_secretmanager_3_ExprOut",
        "TestIamPermissionsRequestIn": "_secretmanager_4_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_secretmanager_5_TestIamPermissionsRequestOut",
        "AutomaticIn": "_secretmanager_6_AutomaticIn",
        "AutomaticOut": "_secretmanager_7_AutomaticOut",
        "LocationIn": "_secretmanager_8_LocationIn",
        "LocationOut": "_secretmanager_9_LocationOut",
        "AccessSecretVersionResponseIn": "_secretmanager_10_AccessSecretVersionResponseIn",
        "AccessSecretVersionResponseOut": "_secretmanager_11_AccessSecretVersionResponseOut",
        "TestIamPermissionsResponseIn": "_secretmanager_12_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_secretmanager_13_TestIamPermissionsResponseOut",
        "ListLocationsResponseIn": "_secretmanager_14_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_secretmanager_15_ListLocationsResponseOut",
        "UserManagedIn": "_secretmanager_16_UserManagedIn",
        "UserManagedOut": "_secretmanager_17_UserManagedOut",
        "BindingIn": "_secretmanager_18_BindingIn",
        "BindingOut": "_secretmanager_19_BindingOut",
        "SetIamPolicyRequestIn": "_secretmanager_20_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_secretmanager_21_SetIamPolicyRequestOut",
        "AutomaticStatusIn": "_secretmanager_22_AutomaticStatusIn",
        "AutomaticStatusOut": "_secretmanager_23_AutomaticStatusOut",
        "AddSecretVersionRequestIn": "_secretmanager_24_AddSecretVersionRequestIn",
        "AddSecretVersionRequestOut": "_secretmanager_25_AddSecretVersionRequestOut",
        "CustomerManagedEncryptionStatusIn": "_secretmanager_26_CustomerManagedEncryptionStatusIn",
        "CustomerManagedEncryptionStatusOut": "_secretmanager_27_CustomerManagedEncryptionStatusOut",
        "ListSecretsResponseIn": "_secretmanager_28_ListSecretsResponseIn",
        "ListSecretsResponseOut": "_secretmanager_29_ListSecretsResponseOut",
        "DestroySecretVersionRequestIn": "_secretmanager_30_DestroySecretVersionRequestIn",
        "DestroySecretVersionRequestOut": "_secretmanager_31_DestroySecretVersionRequestOut",
        "SecretPayloadIn": "_secretmanager_32_SecretPayloadIn",
        "SecretPayloadOut": "_secretmanager_33_SecretPayloadOut",
        "DisableSecretVersionRequestIn": "_secretmanager_34_DisableSecretVersionRequestIn",
        "DisableSecretVersionRequestOut": "_secretmanager_35_DisableSecretVersionRequestOut",
        "SecretIn": "_secretmanager_36_SecretIn",
        "SecretOut": "_secretmanager_37_SecretOut",
        "EmptyIn": "_secretmanager_38_EmptyIn",
        "EmptyOut": "_secretmanager_39_EmptyOut",
        "EnableSecretVersionRequestIn": "_secretmanager_40_EnableSecretVersionRequestIn",
        "EnableSecretVersionRequestOut": "_secretmanager_41_EnableSecretVersionRequestOut",
        "SecretVersionIn": "_secretmanager_42_SecretVersionIn",
        "SecretVersionOut": "_secretmanager_43_SecretVersionOut",
        "AuditLogConfigIn": "_secretmanager_44_AuditLogConfigIn",
        "AuditLogConfigOut": "_secretmanager_45_AuditLogConfigOut",
        "ReplicaStatusIn": "_secretmanager_46_ReplicaStatusIn",
        "ReplicaStatusOut": "_secretmanager_47_ReplicaStatusOut",
        "ListSecretVersionsResponseIn": "_secretmanager_48_ListSecretVersionsResponseIn",
        "ListSecretVersionsResponseOut": "_secretmanager_49_ListSecretVersionsResponseOut",
        "TopicIn": "_secretmanager_50_TopicIn",
        "TopicOut": "_secretmanager_51_TopicOut",
        "ReplicationStatusIn": "_secretmanager_52_ReplicationStatusIn",
        "ReplicationStatusOut": "_secretmanager_53_ReplicationStatusOut",
        "AuditConfigIn": "_secretmanager_54_AuditConfigIn",
        "AuditConfigOut": "_secretmanager_55_AuditConfigOut",
        "RotationIn": "_secretmanager_56_RotationIn",
        "RotationOut": "_secretmanager_57_RotationOut",
        "CustomerManagedEncryptionIn": "_secretmanager_58_CustomerManagedEncryptionIn",
        "CustomerManagedEncryptionOut": "_secretmanager_59_CustomerManagedEncryptionOut",
        "ReplicationIn": "_secretmanager_60_ReplicationIn",
        "ReplicationOut": "_secretmanager_61_ReplicationOut",
        "UserManagedStatusIn": "_secretmanager_62_UserManagedStatusIn",
        "UserManagedStatusOut": "_secretmanager_63_UserManagedStatusOut",
        "ReplicaIn": "_secretmanager_64_ReplicaIn",
        "ReplicaOut": "_secretmanager_65_ReplicaOut",
        "PolicyIn": "_secretmanager_66_PolicyIn",
        "PolicyOut": "_secretmanager_67_PolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["AutomaticIn"] = t.struct(
        {
            "customerManagedEncryption": t.proxy(
                renames["CustomerManagedEncryptionIn"]
            ).optional()
        }
    ).named(renames["AutomaticIn"])
    types["AutomaticOut"] = t.struct(
        {
            "customerManagedEncryption": t.proxy(
                renames["CustomerManagedEncryptionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutomaticOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AccessSecretVersionResponseIn"] = t.struct(
        {
            "name": t.string().optional(),
            "payload": t.proxy(renames["SecretPayloadIn"]).optional(),
        }
    ).named(renames["AccessSecretVersionResponseIn"])
    types["AccessSecretVersionResponseOut"] = t.struct(
        {
            "name": t.string().optional(),
            "payload": t.proxy(renames["SecretPayloadOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSecretVersionResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["UserManagedIn"] = t.struct(
        {"replicas": t.array(t.proxy(renames["ReplicaIn"]))}
    ).named(renames["UserManagedIn"])
    types["UserManagedOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedOut"])
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
    types["AutomaticStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AutomaticStatusIn"]
    )
    types["AutomaticStatusOut"] = t.struct(
        {
            "customerManagedEncryption": t.proxy(
                renames["CustomerManagedEncryptionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutomaticStatusOut"])
    types["AddSecretVersionRequestIn"] = t.struct(
        {"payload": t.proxy(renames["SecretPayloadIn"])}
    ).named(renames["AddSecretVersionRequestIn"])
    types["AddSecretVersionRequestOut"] = t.struct(
        {
            "payload": t.proxy(renames["SecretPayloadOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSecretVersionRequestOut"])
    types["CustomerManagedEncryptionStatusIn"] = t.struct(
        {"kmsKeyVersionName": t.string()}
    ).named(renames["CustomerManagedEncryptionStatusIn"])
    types["CustomerManagedEncryptionStatusOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerManagedEncryptionStatusOut"])
    types["ListSecretsResponseIn"] = t.struct(
        {
            "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSecretsResponseIn"])
    types["ListSecretsResponseOut"] = t.struct(
        {
            "secrets": t.array(t.proxy(renames["SecretOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSecretsResponseOut"])
    types["DestroySecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["DestroySecretVersionRequestIn"])
    types["DestroySecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestroySecretVersionRequestOut"])
    types["SecretPayloadIn"] = t.struct(
        {"dataCrc32c": t.string().optional(), "data": t.string().optional()}
    ).named(renames["SecretPayloadIn"])
    types["SecretPayloadOut"] = t.struct(
        {
            "dataCrc32c": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretPayloadOut"])
    types["DisableSecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["DisableSecretVersionRequestIn"])
    types["DisableSecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableSecretVersionRequestOut"])
    types["SecretIn"] = t.struct(
        {
            "replication": t.proxy(renames["ReplicationIn"]),
            "topics": t.array(t.proxy(renames["TopicIn"])).optional(),
            "ttl": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rotation": t.proxy(renames["RotationIn"]).optional(),
            "expireTime": t.string().optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["SecretIn"])
    types["SecretOut"] = t.struct(
        {
            "replication": t.proxy(renames["ReplicationOut"]),
            "topics": t.array(t.proxy(renames["TopicOut"])).optional(),
            "name": t.string().optional(),
            "ttl": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "rotation": t.proxy(renames["RotationOut"]).optional(),
            "createTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["EnableSecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["EnableSecretVersionRequestIn"])
    types["EnableSecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableSecretVersionRequestOut"])
    types["SecretVersionIn"] = t.struct(
        {"replicationStatus": t.proxy(renames["ReplicationStatusIn"]).optional()}
    ).named(renames["SecretVersionIn"])
    types["SecretVersionOut"] = t.struct(
        {
            "destroyTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "clientSpecifiedPayloadChecksum": t.boolean().optional(),
            "etag": t.string().optional(),
            "replicationStatus": t.proxy(renames["ReplicationStatusOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVersionOut"])
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
    types["ReplicaStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplicaStatusIn"]
    )
    types["ReplicaStatusOut"] = t.struct(
        {
            "customerManagedEncryption": t.proxy(
                renames["CustomerManagedEncryptionStatusOut"]
            ).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaStatusOut"])
    types["ListSecretVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionIn"])).optional(),
        }
    ).named(renames["ListSecretVersionsResponseIn"])
    types["ListSecretVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSecretVersionsResponseOut"])
    types["TopicIn"] = t.struct({"name": t.string()}).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TopicOut"])
    types["ReplicationStatusIn"] = t.struct(
        {
            "automatic": t.proxy(renames["AutomaticStatusIn"]).optional(),
            "userManaged": t.proxy(renames["UserManagedStatusIn"]).optional(),
        }
    ).named(renames["ReplicationStatusIn"])
    types["ReplicationStatusOut"] = t.struct(
        {
            "automatic": t.proxy(renames["AutomaticStatusOut"]).optional(),
            "userManaged": t.proxy(renames["UserManagedStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationStatusOut"])
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
    types["RotationIn"] = t.struct(
        {
            "rotationPeriod": t.string().optional(),
            "nextRotationTime": t.string().optional(),
        }
    ).named(renames["RotationIn"])
    types["RotationOut"] = t.struct(
        {
            "rotationPeriod": t.string().optional(),
            "nextRotationTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RotationOut"])
    types["CustomerManagedEncryptionIn"] = t.struct({"kmsKeyName": t.string()}).named(
        renames["CustomerManagedEncryptionIn"]
    )
    types["CustomerManagedEncryptionOut"] = t.struct(
        {
            "kmsKeyName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerManagedEncryptionOut"])
    types["ReplicationIn"] = t.struct(
        {
            "userManaged": t.proxy(renames["UserManagedIn"]).optional(),
            "automatic": t.proxy(renames["AutomaticIn"]).optional(),
        }
    ).named(renames["ReplicationIn"])
    types["ReplicationOut"] = t.struct(
        {
            "userManaged": t.proxy(renames["UserManagedOut"]).optional(),
            "automatic": t.proxy(renames["AutomaticOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationOut"])
    types["UserManagedStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UserManagedStatusIn"]
    )
    types["UserManagedStatusOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedStatusOut"])
    types["ReplicaIn"] = t.struct(
        {
            "customerManagedEncryption": t.proxy(
                renames["CustomerManagedEncryptionIn"]
            ).optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ReplicaIn"])
    types["ReplicaOut"] = t.struct(
        {
            "customerManagedEncryption": t.proxy(
                renames["CustomerManagedEncryptionOut"]
            ).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])

    functions = {}
    functions["projectsLocationsGet"] = secretmanager.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = secretmanager.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsCreate"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsGet"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsTestIamPermissions"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsPatch"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsAddVersion"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsSetIamPolicy"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsDelete"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsGetIamPolicy"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsList"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsDisable"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsEnable"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsList"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsAccess"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsDestroy"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsGet"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="secretmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
