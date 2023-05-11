from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_secretmanager() -> Import:
    secretmanager = HTTPRuntime("https://secretmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_secretmanager_1_ErrorResponse",
        "ReplicationStatusIn": "_secretmanager_2_ReplicationStatusIn",
        "ReplicationStatusOut": "_secretmanager_3_ReplicationStatusOut",
        "UserManagedStatusIn": "_secretmanager_4_UserManagedStatusIn",
        "UserManagedStatusOut": "_secretmanager_5_UserManagedStatusOut",
        "TestIamPermissionsResponseIn": "_secretmanager_6_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_secretmanager_7_TestIamPermissionsResponseOut",
        "PolicyIn": "_secretmanager_8_PolicyIn",
        "PolicyOut": "_secretmanager_9_PolicyOut",
        "ListSecretVersionsResponseIn": "_secretmanager_10_ListSecretVersionsResponseIn",
        "ListSecretVersionsResponseOut": "_secretmanager_11_ListSecretVersionsResponseOut",
        "LocationIn": "_secretmanager_12_LocationIn",
        "LocationOut": "_secretmanager_13_LocationOut",
        "ReplicationIn": "_secretmanager_14_ReplicationIn",
        "ReplicationOut": "_secretmanager_15_ReplicationOut",
        "AuditLogConfigIn": "_secretmanager_16_AuditLogConfigIn",
        "AuditLogConfigOut": "_secretmanager_17_AuditLogConfigOut",
        "ReplicaIn": "_secretmanager_18_ReplicaIn",
        "ReplicaOut": "_secretmanager_19_ReplicaOut",
        "AddSecretVersionRequestIn": "_secretmanager_20_AddSecretVersionRequestIn",
        "AddSecretVersionRequestOut": "_secretmanager_21_AddSecretVersionRequestOut",
        "ReplicaStatusIn": "_secretmanager_22_ReplicaStatusIn",
        "ReplicaStatusOut": "_secretmanager_23_ReplicaStatusOut",
        "RotationIn": "_secretmanager_24_RotationIn",
        "RotationOut": "_secretmanager_25_RotationOut",
        "CustomerManagedEncryptionIn": "_secretmanager_26_CustomerManagedEncryptionIn",
        "CustomerManagedEncryptionOut": "_secretmanager_27_CustomerManagedEncryptionOut",
        "TestIamPermissionsRequestIn": "_secretmanager_28_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_secretmanager_29_TestIamPermissionsRequestOut",
        "ListLocationsResponseIn": "_secretmanager_30_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_secretmanager_31_ListLocationsResponseOut",
        "TopicIn": "_secretmanager_32_TopicIn",
        "TopicOut": "_secretmanager_33_TopicOut",
        "BindingIn": "_secretmanager_34_BindingIn",
        "BindingOut": "_secretmanager_35_BindingOut",
        "ExprIn": "_secretmanager_36_ExprIn",
        "ExprOut": "_secretmanager_37_ExprOut",
        "ListSecretsResponseIn": "_secretmanager_38_ListSecretsResponseIn",
        "ListSecretsResponseOut": "_secretmanager_39_ListSecretsResponseOut",
        "EnableSecretVersionRequestIn": "_secretmanager_40_EnableSecretVersionRequestIn",
        "EnableSecretVersionRequestOut": "_secretmanager_41_EnableSecretVersionRequestOut",
        "AccessSecretVersionResponseIn": "_secretmanager_42_AccessSecretVersionResponseIn",
        "AccessSecretVersionResponseOut": "_secretmanager_43_AccessSecretVersionResponseOut",
        "SecretVersionIn": "_secretmanager_44_SecretVersionIn",
        "SecretVersionOut": "_secretmanager_45_SecretVersionOut",
        "AuditConfigIn": "_secretmanager_46_AuditConfigIn",
        "AuditConfigOut": "_secretmanager_47_AuditConfigOut",
        "SecretPayloadIn": "_secretmanager_48_SecretPayloadIn",
        "SecretPayloadOut": "_secretmanager_49_SecretPayloadOut",
        "CustomerManagedEncryptionStatusIn": "_secretmanager_50_CustomerManagedEncryptionStatusIn",
        "CustomerManagedEncryptionStatusOut": "_secretmanager_51_CustomerManagedEncryptionStatusOut",
        "EmptyIn": "_secretmanager_52_EmptyIn",
        "EmptyOut": "_secretmanager_53_EmptyOut",
        "DisableSecretVersionRequestIn": "_secretmanager_54_DisableSecretVersionRequestIn",
        "DisableSecretVersionRequestOut": "_secretmanager_55_DisableSecretVersionRequestOut",
        "SecretIn": "_secretmanager_56_SecretIn",
        "SecretOut": "_secretmanager_57_SecretOut",
        "UserManagedIn": "_secretmanager_58_UserManagedIn",
        "UserManagedOut": "_secretmanager_59_UserManagedOut",
        "SetIamPolicyRequestIn": "_secretmanager_60_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_secretmanager_61_SetIamPolicyRequestOut",
        "AutomaticIn": "_secretmanager_62_AutomaticIn",
        "AutomaticOut": "_secretmanager_63_AutomaticOut",
        "AutomaticStatusIn": "_secretmanager_64_AutomaticStatusIn",
        "AutomaticStatusOut": "_secretmanager_65_AutomaticStatusOut",
        "DestroySecretVersionRequestIn": "_secretmanager_66_DestroySecretVersionRequestIn",
        "DestroySecretVersionRequestOut": "_secretmanager_67_DestroySecretVersionRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ReplicationStatusIn"] = t.struct(
        {
            "userManaged": t.proxy(renames["UserManagedStatusIn"]).optional(),
            "automatic": t.proxy(renames["AutomaticStatusIn"]).optional(),
        }
    ).named(renames["ReplicationStatusIn"])
    types["ReplicationStatusOut"] = t.struct(
        {
            "userManaged": t.proxy(renames["UserManagedStatusOut"]).optional(),
            "automatic": t.proxy(renames["AutomaticStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationStatusOut"])
    types["UserManagedStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UserManagedStatusIn"]
    )
    types["UserManagedStatusOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedStatusOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["AddSecretVersionRequestIn"] = t.struct(
        {"payload": t.proxy(renames["SecretPayloadIn"])}
    ).named(renames["AddSecretVersionRequestIn"])
    types["AddSecretVersionRequestOut"] = t.struct(
        {
            "payload": t.proxy(renames["SecretPayloadOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSecretVersionRequestOut"])
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
    types["RotationIn"] = t.struct(
        {
            "nextRotationTime": t.string().optional(),
            "rotationPeriod": t.string().optional(),
        }
    ).named(renames["RotationIn"])
    types["RotationOut"] = t.struct(
        {
            "nextRotationTime": t.string().optional(),
            "rotationPeriod": t.string().optional(),
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["TopicIn"] = t.struct({"name": t.string()}).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {"name": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TopicOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ListSecretsResponseIn"] = t.struct(
        {
            "secrets": t.array(t.proxy(renames["SecretIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListSecretsResponseIn"])
    types["ListSecretsResponseOut"] = t.struct(
        {
            "secrets": t.array(t.proxy(renames["SecretOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSecretsResponseOut"])
    types["EnableSecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["EnableSecretVersionRequestIn"])
    types["EnableSecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableSecretVersionRequestOut"])
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
    types["SecretVersionIn"] = t.struct(
        {"replicationStatus": t.proxy(renames["ReplicationStatusIn"]).optional()}
    ).named(renames["SecretVersionIn"])
    types["SecretVersionOut"] = t.struct(
        {
            "destroyTime": t.string().optional(),
            "name": t.string().optional(),
            "clientSpecifiedPayloadChecksum": t.boolean().optional(),
            "etag": t.string().optional(),
            "replicationStatus": t.proxy(renames["ReplicationStatusOut"]).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVersionOut"])
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
    types["SecretPayloadIn"] = t.struct(
        {"data": t.string().optional(), "dataCrc32c": t.string().optional()}
    ).named(renames["SecretPayloadIn"])
    types["SecretPayloadOut"] = t.struct(
        {
            "data": t.string().optional(),
            "dataCrc32c": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretPayloadOut"])
    types["CustomerManagedEncryptionStatusIn"] = t.struct(
        {"kmsKeyVersionName": t.string()}
    ).named(renames["CustomerManagedEncryptionStatusIn"])
    types["CustomerManagedEncryptionStatusOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerManagedEncryptionStatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
            "ttl": t.string().optional(),
            "replication": t.proxy(renames["ReplicationIn"]),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "topics": t.array(t.proxy(renames["TopicIn"])).optional(),
            "expireTime": t.string().optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "rotation": t.proxy(renames["RotationIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SecretIn"])
    types["SecretOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "replication": t.proxy(renames["ReplicationOut"]),
            "createTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "topics": t.array(t.proxy(renames["TopicOut"])).optional(),
            "expireTime": t.string().optional(),
            "name": t.string().optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "rotation": t.proxy(renames["RotationOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
    types["UserManagedIn"] = t.struct(
        {"replicas": t.array(t.proxy(renames["ReplicaIn"]))}
    ).named(renames["UserManagedIn"])
    types["UserManagedOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedOut"])
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
    types["DestroySecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["DestroySecretVersionRequestIn"])
    types["DestroySecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestroySecretVersionRequestOut"])

    functions = {}
    functions["projectsSecretsAddVersion"] = secretmanager.post(
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
    functions["projectsSecretsPatch"] = secretmanager.post(
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
    functions["projectsSecretsCreate"] = secretmanager.post(
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
    functions["projectsSecretsSetIamPolicy"] = secretmanager.post(
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
    functions["projectsSecretsList"] = secretmanager.post(
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
    functions["projectsSecretsDelete"] = secretmanager.post(
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
    functions["projectsSecretsGet"] = secretmanager.post(
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
    functions["projectsSecretsGetIamPolicy"] = secretmanager.post(
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
    functions["projectsSecretsTestIamPermissions"] = secretmanager.post(
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
    functions["projectsSecretsVersionsList"] = secretmanager.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsGet"] = secretmanager.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsDestroy"] = secretmanager.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsDisable"] = secretmanager.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsAccess"] = secretmanager.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsEnable"] = secretmanager.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SecretVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="secretmanager", renames=renames, types=types, functions=functions
    )
