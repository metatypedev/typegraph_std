from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_secretmanager() -> Import:
    secretmanager = HTTPRuntime("https://secretmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_secretmanager_1_ErrorResponse",
        "EnableSecretVersionRequestIn": "_secretmanager_2_EnableSecretVersionRequestIn",
        "EnableSecretVersionRequestOut": "_secretmanager_3_EnableSecretVersionRequestOut",
        "SetIamPolicyRequestIn": "_secretmanager_4_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_secretmanager_5_SetIamPolicyRequestOut",
        "AutomaticIn": "_secretmanager_6_AutomaticIn",
        "AutomaticOut": "_secretmanager_7_AutomaticOut",
        "DestroySecretVersionRequestIn": "_secretmanager_8_DestroySecretVersionRequestIn",
        "DestroySecretVersionRequestOut": "_secretmanager_9_DestroySecretVersionRequestOut",
        "UserManagedStatusIn": "_secretmanager_10_UserManagedStatusIn",
        "UserManagedStatusOut": "_secretmanager_11_UserManagedStatusOut",
        "EmptyIn": "_secretmanager_12_EmptyIn",
        "EmptyOut": "_secretmanager_13_EmptyOut",
        "SecretVersionIn": "_secretmanager_14_SecretVersionIn",
        "SecretVersionOut": "_secretmanager_15_SecretVersionOut",
        "ExprIn": "_secretmanager_16_ExprIn",
        "ExprOut": "_secretmanager_17_ExprOut",
        "AutomaticStatusIn": "_secretmanager_18_AutomaticStatusIn",
        "AutomaticStatusOut": "_secretmanager_19_AutomaticStatusOut",
        "AuditLogConfigIn": "_secretmanager_20_AuditLogConfigIn",
        "AuditLogConfigOut": "_secretmanager_21_AuditLogConfigOut",
        "AddSecretVersionRequestIn": "_secretmanager_22_AddSecretVersionRequestIn",
        "AddSecretVersionRequestOut": "_secretmanager_23_AddSecretVersionRequestOut",
        "ListSecretVersionsResponseIn": "_secretmanager_24_ListSecretVersionsResponseIn",
        "ListSecretVersionsResponseOut": "_secretmanager_25_ListSecretVersionsResponseOut",
        "DisableSecretVersionRequestIn": "_secretmanager_26_DisableSecretVersionRequestIn",
        "DisableSecretVersionRequestOut": "_secretmanager_27_DisableSecretVersionRequestOut",
        "ListLocationsResponseIn": "_secretmanager_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_secretmanager_29_ListLocationsResponseOut",
        "SecretIn": "_secretmanager_30_SecretIn",
        "SecretOut": "_secretmanager_31_SecretOut",
        "CustomerManagedEncryptionIn": "_secretmanager_32_CustomerManagedEncryptionIn",
        "CustomerManagedEncryptionOut": "_secretmanager_33_CustomerManagedEncryptionOut",
        "UserManagedIn": "_secretmanager_34_UserManagedIn",
        "UserManagedOut": "_secretmanager_35_UserManagedOut",
        "CustomerManagedEncryptionStatusIn": "_secretmanager_36_CustomerManagedEncryptionStatusIn",
        "CustomerManagedEncryptionStatusOut": "_secretmanager_37_CustomerManagedEncryptionStatusOut",
        "PolicyIn": "_secretmanager_38_PolicyIn",
        "PolicyOut": "_secretmanager_39_PolicyOut",
        "BindingIn": "_secretmanager_40_BindingIn",
        "BindingOut": "_secretmanager_41_BindingOut",
        "ReplicaIn": "_secretmanager_42_ReplicaIn",
        "ReplicaOut": "_secretmanager_43_ReplicaOut",
        "SecretPayloadIn": "_secretmanager_44_SecretPayloadIn",
        "SecretPayloadOut": "_secretmanager_45_SecretPayloadOut",
        "ReplicationStatusIn": "_secretmanager_46_ReplicationStatusIn",
        "ReplicationStatusOut": "_secretmanager_47_ReplicationStatusOut",
        "TopicIn": "_secretmanager_48_TopicIn",
        "TopicOut": "_secretmanager_49_TopicOut",
        "TestIamPermissionsRequestIn": "_secretmanager_50_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_secretmanager_51_TestIamPermissionsRequestOut",
        "ListSecretsResponseIn": "_secretmanager_52_ListSecretsResponseIn",
        "ListSecretsResponseOut": "_secretmanager_53_ListSecretsResponseOut",
        "AccessSecretVersionResponseIn": "_secretmanager_54_AccessSecretVersionResponseIn",
        "AccessSecretVersionResponseOut": "_secretmanager_55_AccessSecretVersionResponseOut",
        "ReplicationIn": "_secretmanager_56_ReplicationIn",
        "ReplicationOut": "_secretmanager_57_ReplicationOut",
        "AuditConfigIn": "_secretmanager_58_AuditConfigIn",
        "AuditConfigOut": "_secretmanager_59_AuditConfigOut",
        "TestIamPermissionsResponseIn": "_secretmanager_60_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_secretmanager_61_TestIamPermissionsResponseOut",
        "LocationIn": "_secretmanager_62_LocationIn",
        "LocationOut": "_secretmanager_63_LocationOut",
        "ReplicaStatusIn": "_secretmanager_64_ReplicaStatusIn",
        "ReplicaStatusOut": "_secretmanager_65_ReplicaStatusOut",
        "RotationIn": "_secretmanager_66_RotationIn",
        "RotationOut": "_secretmanager_67_RotationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EnableSecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["EnableSecretVersionRequestIn"])
    types["EnableSecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableSecretVersionRequestOut"])
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
    types["DestroySecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["DestroySecretVersionRequestIn"])
    types["DestroySecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestroySecretVersionRequestOut"])
    types["UserManagedStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UserManagedStatusIn"]
    )
    types["UserManagedStatusOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedStatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SecretVersionIn"] = t.struct(
        {"replicationStatus": t.proxy(renames["ReplicationStatusIn"]).optional()}
    ).named(renames["SecretVersionIn"])
    types["SecretVersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "replicationStatus": t.proxy(renames["ReplicationStatusOut"]).optional(),
            "destroyTime": t.string().optional(),
            "etag": t.string().optional(),
            "clientSpecifiedPayloadChecksum": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVersionOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["AddSecretVersionRequestIn"] = t.struct(
        {"payload": t.proxy(renames["SecretPayloadIn"])}
    ).named(renames["AddSecretVersionRequestIn"])
    types["AddSecretVersionRequestOut"] = t.struct(
        {
            "payload": t.proxy(renames["SecretPayloadOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSecretVersionRequestOut"])
    types["ListSecretVersionsResponseIn"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["SecretVersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListSecretVersionsResponseIn"])
    types["ListSecretVersionsResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["SecretVersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSecretVersionsResponseOut"])
    types["DisableSecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["DisableSecretVersionRequestIn"])
    types["DisableSecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableSecretVersionRequestOut"])
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
    types["SecretIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "ttl": t.string().optional(),
            "rotation": t.proxy(renames["RotationIn"]).optional(),
            "expireTime": t.string().optional(),
            "topics": t.array(t.proxy(renames["TopicIn"])).optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "replication": t.proxy(renames["ReplicationIn"]),
        }
    ).named(renames["SecretIn"])
    types["SecretOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "ttl": t.string().optional(),
            "rotation": t.proxy(renames["RotationOut"]).optional(),
            "expireTime": t.string().optional(),
            "topics": t.array(t.proxy(renames["TopicOut"])).optional(),
            "etag": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "replication": t.proxy(renames["ReplicationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["CustomerManagedEncryptionIn"] = t.struct({"kmsKeyName": t.string()}).named(
        renames["CustomerManagedEncryptionIn"]
    )
    types["CustomerManagedEncryptionOut"] = t.struct(
        {
            "kmsKeyName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerManagedEncryptionOut"])
    types["UserManagedIn"] = t.struct(
        {"replicas": t.array(t.proxy(renames["ReplicaIn"]))}
    ).named(renames["UserManagedIn"])
    types["UserManagedOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedOut"])
    types["CustomerManagedEncryptionStatusIn"] = t.struct(
        {"kmsKeyVersionName": t.string()}
    ).named(renames["CustomerManagedEncryptionStatusIn"])
    types["CustomerManagedEncryptionStatusOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerManagedEncryptionStatusOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["TopicIn"] = t.struct({"name": t.string()}).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TopicOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListSecretsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
        }
    ).named(renames["ListSecretsResponseIn"])
    types["ListSecretsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "secrets": t.array(t.proxy(renames["SecretOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSecretsResponseOut"])
    types["AccessSecretVersionResponseIn"] = t.struct(
        {
            "payload": t.proxy(renames["SecretPayloadIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccessSecretVersionResponseIn"])
    types["AccessSecretVersionResponseOut"] = t.struct(
        {
            "payload": t.proxy(renames["SecretPayloadOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessSecretVersionResponseOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ReplicaStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReplicaStatusIn"]
    )
    types["ReplicaStatusOut"] = t.struct(
        {
            "location": t.string().optional(),
            "customerManagedEncryption": t.proxy(
                renames["CustomerManagedEncryptionStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicaStatusOut"])
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

    functions = {}
    functions["projectsLocationsList"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = secretmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsGetIamPolicy"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsCreate"] = secretmanager.get(
        "v1/{parent}/secrets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
    functions["projectsSecretsVersionsAccess"] = secretmanager.get(
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
