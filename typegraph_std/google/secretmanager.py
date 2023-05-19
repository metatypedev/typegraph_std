from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_secretmanager() -> Import:
    secretmanager = HTTPRuntime("https://secretmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_secretmanager_1_ErrorResponse",
        "LocationIn": "_secretmanager_2_LocationIn",
        "LocationOut": "_secretmanager_3_LocationOut",
        "RotationIn": "_secretmanager_4_RotationIn",
        "RotationOut": "_secretmanager_5_RotationOut",
        "SecretVersionIn": "_secretmanager_6_SecretVersionIn",
        "SecretVersionOut": "_secretmanager_7_SecretVersionOut",
        "ReplicationIn": "_secretmanager_8_ReplicationIn",
        "ReplicationOut": "_secretmanager_9_ReplicationOut",
        "SecretPayloadIn": "_secretmanager_10_SecretPayloadIn",
        "SecretPayloadOut": "_secretmanager_11_SecretPayloadOut",
        "AddSecretVersionRequestIn": "_secretmanager_12_AddSecretVersionRequestIn",
        "AddSecretVersionRequestOut": "_secretmanager_13_AddSecretVersionRequestOut",
        "ListSecretVersionsResponseIn": "_secretmanager_14_ListSecretVersionsResponseIn",
        "ListSecretVersionsResponseOut": "_secretmanager_15_ListSecretVersionsResponseOut",
        "ReplicationStatusIn": "_secretmanager_16_ReplicationStatusIn",
        "ReplicationStatusOut": "_secretmanager_17_ReplicationStatusOut",
        "AutomaticIn": "_secretmanager_18_AutomaticIn",
        "AutomaticOut": "_secretmanager_19_AutomaticOut",
        "DisableSecretVersionRequestIn": "_secretmanager_20_DisableSecretVersionRequestIn",
        "DisableSecretVersionRequestOut": "_secretmanager_21_DisableSecretVersionRequestOut",
        "ReplicaStatusIn": "_secretmanager_22_ReplicaStatusIn",
        "ReplicaStatusOut": "_secretmanager_23_ReplicaStatusOut",
        "EnableSecretVersionRequestIn": "_secretmanager_24_EnableSecretVersionRequestIn",
        "EnableSecretVersionRequestOut": "_secretmanager_25_EnableSecretVersionRequestOut",
        "PolicyIn": "_secretmanager_26_PolicyIn",
        "PolicyOut": "_secretmanager_27_PolicyOut",
        "ExprIn": "_secretmanager_28_ExprIn",
        "ExprOut": "_secretmanager_29_ExprOut",
        "UserManagedStatusIn": "_secretmanager_30_UserManagedStatusIn",
        "UserManagedStatusOut": "_secretmanager_31_UserManagedStatusOut",
        "SetIamPolicyRequestIn": "_secretmanager_32_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_secretmanager_33_SetIamPolicyRequestOut",
        "ListLocationsResponseIn": "_secretmanager_34_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_secretmanager_35_ListLocationsResponseOut",
        "ListSecretsResponseIn": "_secretmanager_36_ListSecretsResponseIn",
        "ListSecretsResponseOut": "_secretmanager_37_ListSecretsResponseOut",
        "CustomerManagedEncryptionStatusIn": "_secretmanager_38_CustomerManagedEncryptionStatusIn",
        "CustomerManagedEncryptionStatusOut": "_secretmanager_39_CustomerManagedEncryptionStatusOut",
        "DestroySecretVersionRequestIn": "_secretmanager_40_DestroySecretVersionRequestIn",
        "DestroySecretVersionRequestOut": "_secretmanager_41_DestroySecretVersionRequestOut",
        "AuditConfigIn": "_secretmanager_42_AuditConfigIn",
        "AuditConfigOut": "_secretmanager_43_AuditConfigOut",
        "EmptyIn": "_secretmanager_44_EmptyIn",
        "EmptyOut": "_secretmanager_45_EmptyOut",
        "AccessSecretVersionResponseIn": "_secretmanager_46_AccessSecretVersionResponseIn",
        "AccessSecretVersionResponseOut": "_secretmanager_47_AccessSecretVersionResponseOut",
        "ReplicaIn": "_secretmanager_48_ReplicaIn",
        "ReplicaOut": "_secretmanager_49_ReplicaOut",
        "TopicIn": "_secretmanager_50_TopicIn",
        "TopicOut": "_secretmanager_51_TopicOut",
        "TestIamPermissionsRequestIn": "_secretmanager_52_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_secretmanager_53_TestIamPermissionsRequestOut",
        "AuditLogConfigIn": "_secretmanager_54_AuditLogConfigIn",
        "AuditLogConfigOut": "_secretmanager_55_AuditLogConfigOut",
        "AutomaticStatusIn": "_secretmanager_56_AutomaticStatusIn",
        "AutomaticStatusOut": "_secretmanager_57_AutomaticStatusOut",
        "SecretIn": "_secretmanager_58_SecretIn",
        "SecretOut": "_secretmanager_59_SecretOut",
        "BindingIn": "_secretmanager_60_BindingIn",
        "BindingOut": "_secretmanager_61_BindingOut",
        "TestIamPermissionsResponseIn": "_secretmanager_62_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_secretmanager_63_TestIamPermissionsResponseOut",
        "UserManagedIn": "_secretmanager_64_UserManagedIn",
        "UserManagedOut": "_secretmanager_65_UserManagedOut",
        "CustomerManagedEncryptionIn": "_secretmanager_66_CustomerManagedEncryptionIn",
        "CustomerManagedEncryptionOut": "_secretmanager_67_CustomerManagedEncryptionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["SecretVersionIn"] = t.struct(
        {"replicationStatus": t.proxy(renames["ReplicationStatusIn"]).optional()}
    ).named(renames["SecretVersionIn"])
    types["SecretVersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "clientSpecifiedPayloadChecksum": t.boolean().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "destroyTime": t.string().optional(),
            "state": t.string().optional(),
            "replicationStatus": t.proxy(renames["ReplicationStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVersionOut"])
    types["ReplicationIn"] = t.struct(
        {
            "automatic": t.proxy(renames["AutomaticIn"]).optional(),
            "userManaged": t.proxy(renames["UserManagedIn"]).optional(),
        }
    ).named(renames["ReplicationIn"])
    types["ReplicationOut"] = t.struct(
        {
            "automatic": t.proxy(renames["AutomaticOut"]).optional(),
            "userManaged": t.proxy(renames["UserManagedOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationOut"])
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
    types["DisableSecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["DisableSecretVersionRequestIn"])
    types["DisableSecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableSecretVersionRequestOut"])
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
    types["EnableSecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["EnableSecretVersionRequestIn"])
    types["EnableSecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableSecretVersionRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["UserManagedStatusIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UserManagedStatusIn"]
    )
    types["UserManagedStatusOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedStatusOut"])
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
    types["CustomerManagedEncryptionStatusIn"] = t.struct(
        {"kmsKeyVersionName": t.string()}
    ).named(renames["CustomerManagedEncryptionStatusIn"])
    types["CustomerManagedEncryptionStatusOut"] = t.struct(
        {
            "kmsKeyVersionName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerManagedEncryptionStatusOut"])
    types["DestroySecretVersionRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["DestroySecretVersionRequestIn"])
    types["DestroySecretVersionRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DestroySecretVersionRequestOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["SecretIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "replication": t.proxy(renames["ReplicationIn"]),
            "expireTime": t.string().optional(),
            "topics": t.array(t.proxy(renames["TopicIn"])).optional(),
            "rotation": t.proxy(renames["RotationIn"]).optional(),
            "ttl": t.string().optional(),
        }
    ).named(renames["SecretIn"])
    types["SecretOut"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "versionAliases": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "replication": t.proxy(renames["ReplicationOut"]),
            "expireTime": t.string().optional(),
            "topics": t.array(t.proxy(renames["TopicOut"])).optional(),
            "createTime": t.string().optional(),
            "rotation": t.proxy(renames["RotationOut"]).optional(),
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["UserManagedIn"] = t.struct(
        {"replicas": t.array(t.proxy(renames["ReplicaIn"]))}
    ).named(renames["UserManagedIn"])
    types["UserManagedOut"] = t.struct(
        {
            "replicas": t.array(t.proxy(renames["ReplicaOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserManagedOut"])
    types["CustomerManagedEncryptionIn"] = t.struct({"kmsKeyName": t.string()}).named(
        renames["CustomerManagedEncryptionIn"]
    )
    types["CustomerManagedEncryptionOut"] = t.struct(
        {
            "kmsKeyName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerManagedEncryptionOut"])

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
    functions["projectsSecretsCreate"] = secretmanager.post(
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
    functions["projectsSecretsPatch"] = secretmanager.post(
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
    functions["projectsSecretsAddVersion"] = secretmanager.post(
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
    functions["projectsSecretsTestIamPermissions"] = secretmanager.post(
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
    functions["projectsSecretsGet"] = secretmanager.post(
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
    functions["projectsSecretsDelete"] = secretmanager.post(
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
    functions["projectsSecretsList"] = secretmanager.post(
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
    functions["projectsSecretsGetIamPolicy"] = secretmanager.post(
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
    functions["projectsSecretsSetIamPolicy"] = secretmanager.post(
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
    functions["projectsSecretsVersionsDisable"] = secretmanager.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsEnable"] = secretmanager.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsAccess"] = secretmanager.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsGet"] = secretmanager.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsDestroy"] = secretmanager.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSecretsVersionsList"] = secretmanager.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSecretVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="secretmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
