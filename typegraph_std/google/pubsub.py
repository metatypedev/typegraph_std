from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_pubsub() -> Import:
    pubsub = HTTPRuntime("https://pubsub.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsub_1_ErrorResponse",
        "ValidateSchemaResponseIn": "_pubsub_2_ValidateSchemaResponseIn",
        "ValidateSchemaResponseOut": "_pubsub_3_ValidateSchemaResponseOut",
        "ExpirationPolicyIn": "_pubsub_4_ExpirationPolicyIn",
        "ExpirationPolicyOut": "_pubsub_5_ExpirationPolicyOut",
        "ExprIn": "_pubsub_6_ExprIn",
        "ExprOut": "_pubsub_7_ExprOut",
        "PolicyIn": "_pubsub_8_PolicyIn",
        "PolicyOut": "_pubsub_9_PolicyOut",
        "ValidateSchemaRequestIn": "_pubsub_10_ValidateSchemaRequestIn",
        "ValidateSchemaRequestOut": "_pubsub_11_ValidateSchemaRequestOut",
        "BindingIn": "_pubsub_12_BindingIn",
        "BindingOut": "_pubsub_13_BindingOut",
        "ListTopicSnapshotsResponseIn": "_pubsub_14_ListTopicSnapshotsResponseIn",
        "ListTopicSnapshotsResponseOut": "_pubsub_15_ListTopicSnapshotsResponseOut",
        "OidcTokenIn": "_pubsub_16_OidcTokenIn",
        "OidcTokenOut": "_pubsub_17_OidcTokenOut",
        "RollbackSchemaRequestIn": "_pubsub_18_RollbackSchemaRequestIn",
        "RollbackSchemaRequestOut": "_pubsub_19_RollbackSchemaRequestOut",
        "CommitSchemaRequestIn": "_pubsub_20_CommitSchemaRequestIn",
        "CommitSchemaRequestOut": "_pubsub_21_CommitSchemaRequestOut",
        "UpdateSubscriptionRequestIn": "_pubsub_22_UpdateSubscriptionRequestIn",
        "UpdateSubscriptionRequestOut": "_pubsub_23_UpdateSubscriptionRequestOut",
        "SeekResponseIn": "_pubsub_24_SeekResponseIn",
        "SeekResponseOut": "_pubsub_25_SeekResponseOut",
        "AvroConfigIn": "_pubsub_26_AvroConfigIn",
        "AvroConfigOut": "_pubsub_27_AvroConfigOut",
        "ModifyPushConfigRequestIn": "_pubsub_28_ModifyPushConfigRequestIn",
        "ModifyPushConfigRequestOut": "_pubsub_29_ModifyPushConfigRequestOut",
        "ListSchemasResponseIn": "_pubsub_30_ListSchemasResponseIn",
        "ListSchemasResponseOut": "_pubsub_31_ListSchemasResponseOut",
        "AcknowledgeRequestIn": "_pubsub_32_AcknowledgeRequestIn",
        "AcknowledgeRequestOut": "_pubsub_33_AcknowledgeRequestOut",
        "ValidateMessageResponseIn": "_pubsub_34_ValidateMessageResponseIn",
        "ValidateMessageResponseOut": "_pubsub_35_ValidateMessageResponseOut",
        "PublishResponseIn": "_pubsub_36_PublishResponseIn",
        "PublishResponseOut": "_pubsub_37_PublishResponseOut",
        "RetryPolicyIn": "_pubsub_38_RetryPolicyIn",
        "RetryPolicyOut": "_pubsub_39_RetryPolicyOut",
        "MessageStoragePolicyIn": "_pubsub_40_MessageStoragePolicyIn",
        "MessageStoragePolicyOut": "_pubsub_41_MessageStoragePolicyOut",
        "SchemaIn": "_pubsub_42_SchemaIn",
        "SchemaOut": "_pubsub_43_SchemaOut",
        "PullRequestIn": "_pubsub_44_PullRequestIn",
        "PullRequestOut": "_pubsub_45_PullRequestOut",
        "UpdateSnapshotRequestIn": "_pubsub_46_UpdateSnapshotRequestIn",
        "UpdateSnapshotRequestOut": "_pubsub_47_UpdateSnapshotRequestOut",
        "TestIamPermissionsResponseIn": "_pubsub_48_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_pubsub_49_TestIamPermissionsResponseOut",
        "CreateSnapshotRequestIn": "_pubsub_50_CreateSnapshotRequestIn",
        "CreateSnapshotRequestOut": "_pubsub_51_CreateSnapshotRequestOut",
        "EmptyIn": "_pubsub_52_EmptyIn",
        "EmptyOut": "_pubsub_53_EmptyOut",
        "ListTopicsResponseIn": "_pubsub_54_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsub_55_ListTopicsResponseOut",
        "TestIamPermissionsRequestIn": "_pubsub_56_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_pubsub_57_TestIamPermissionsRequestOut",
        "SetIamPolicyRequestIn": "_pubsub_58_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_pubsub_59_SetIamPolicyRequestOut",
        "PushConfigIn": "_pubsub_60_PushConfigIn",
        "PushConfigOut": "_pubsub_61_PushConfigOut",
        "SeekRequestIn": "_pubsub_62_SeekRequestIn",
        "SeekRequestOut": "_pubsub_63_SeekRequestOut",
        "SubscriptionIn": "_pubsub_64_SubscriptionIn",
        "SubscriptionOut": "_pubsub_65_SubscriptionOut",
        "ModifyAckDeadlineRequestIn": "_pubsub_66_ModifyAckDeadlineRequestIn",
        "ModifyAckDeadlineRequestOut": "_pubsub_67_ModifyAckDeadlineRequestOut",
        "TextConfigIn": "_pubsub_68_TextConfigIn",
        "TextConfigOut": "_pubsub_69_TextConfigOut",
        "SnapshotIn": "_pubsub_70_SnapshotIn",
        "SnapshotOut": "_pubsub_71_SnapshotOut",
        "SchemaSettingsIn": "_pubsub_72_SchemaSettingsIn",
        "SchemaSettingsOut": "_pubsub_73_SchemaSettingsOut",
        "DeadLetterPolicyIn": "_pubsub_74_DeadLetterPolicyIn",
        "DeadLetterPolicyOut": "_pubsub_75_DeadLetterPolicyOut",
        "ListTopicSubscriptionsResponseIn": "_pubsub_76_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsub_77_ListTopicSubscriptionsResponseOut",
        "ListSubscriptionsResponseIn": "_pubsub_78_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsub_79_ListSubscriptionsResponseOut",
        "PublishRequestIn": "_pubsub_80_PublishRequestIn",
        "PublishRequestOut": "_pubsub_81_PublishRequestOut",
        "ReceivedMessageIn": "_pubsub_82_ReceivedMessageIn",
        "ReceivedMessageOut": "_pubsub_83_ReceivedMessageOut",
        "ListSnapshotsResponseIn": "_pubsub_84_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_pubsub_85_ListSnapshotsResponseOut",
        "ListSchemaRevisionsResponseIn": "_pubsub_86_ListSchemaRevisionsResponseIn",
        "ListSchemaRevisionsResponseOut": "_pubsub_87_ListSchemaRevisionsResponseOut",
        "PullResponseIn": "_pubsub_88_PullResponseIn",
        "PullResponseOut": "_pubsub_89_PullResponseOut",
        "TopicIn": "_pubsub_90_TopicIn",
        "TopicOut": "_pubsub_91_TopicOut",
        "BigQueryConfigIn": "_pubsub_92_BigQueryConfigIn",
        "BigQueryConfigOut": "_pubsub_93_BigQueryConfigOut",
        "CloudStorageConfigIn": "_pubsub_94_CloudStorageConfigIn",
        "CloudStorageConfigOut": "_pubsub_95_CloudStorageConfigOut",
        "PubsubMessageIn": "_pubsub_96_PubsubMessageIn",
        "PubsubMessageOut": "_pubsub_97_PubsubMessageOut",
        "DetachSubscriptionResponseIn": "_pubsub_98_DetachSubscriptionResponseIn",
        "DetachSubscriptionResponseOut": "_pubsub_99_DetachSubscriptionResponseOut",
        "ValidateMessageRequestIn": "_pubsub_100_ValidateMessageRequestIn",
        "ValidateMessageRequestOut": "_pubsub_101_ValidateMessageRequestOut",
        "UpdateTopicRequestIn": "_pubsub_102_UpdateTopicRequestIn",
        "UpdateTopicRequestOut": "_pubsub_103_UpdateTopicRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ValidateSchemaResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateSchemaResponseIn"]
    )
    types["ValidateSchemaResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateSchemaResponseOut"])
    types["ExpirationPolicyIn"] = t.struct({"ttl": t.string().optional()}).named(
        renames["ExpirationPolicyIn"]
    )
    types["ExpirationPolicyOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpirationPolicyOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ValidateSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["ValidateSchemaRequestIn"])
    types["ValidateSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateSchemaRequestOut"])
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
    types["ListTopicSnapshotsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snapshots": t.array(t.string()).optional(),
        }
    ).named(renames["ListTopicSnapshotsResponseIn"])
    types["ListTopicSnapshotsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snapshots": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTopicSnapshotsResponseOut"])
    types["OidcTokenIn"] = t.struct(
        {"audience": t.string().optional(), "serviceAccountEmail": t.string()}
    ).named(renames["OidcTokenIn"])
    types["OidcTokenOut"] = t.struct(
        {
            "audience": t.string().optional(),
            "serviceAccountEmail": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OidcTokenOut"])
    types["RollbackSchemaRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackSchemaRequestIn"]
    )
    types["RollbackSchemaRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackSchemaRequestOut"])
    types["CommitSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["CommitSchemaRequestIn"])
    types["CommitSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitSchemaRequestOut"])
    types["UpdateSubscriptionRequestIn"] = t.struct(
        {"subscription": t.proxy(renames["SubscriptionIn"]), "updateMask": t.string()}
    ).named(renames["UpdateSubscriptionRequestIn"])
    types["UpdateSubscriptionRequestOut"] = t.struct(
        {
            "subscription": t.proxy(renames["SubscriptionOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSubscriptionRequestOut"])
    types["SeekResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekResponseIn"]
    )
    types["SeekResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekResponseOut"])
    types["AvroConfigIn"] = t.struct({"writeMetadata": t.boolean().optional()}).named(
        renames["AvroConfigIn"]
    )
    types["AvroConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvroConfigOut"])
    types["ModifyPushConfigRequestIn"] = t.struct(
        {"pushConfig": t.proxy(renames["PushConfigIn"])}
    ).named(renames["ModifyPushConfigRequestIn"])
    types["ModifyPushConfigRequestOut"] = t.struct(
        {
            "pushConfig": t.proxy(renames["PushConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyPushConfigRequestOut"])
    types["ListSchemasResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "schemas": t.array(t.proxy(renames["SchemaIn"])).optional(),
        }
    ).named(renames["ListSchemasResponseIn"])
    types["ListSchemasResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "schemas": t.array(t.proxy(renames["SchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSchemasResponseOut"])
    types["AcknowledgeRequestIn"] = t.struct({"ackIds": t.array(t.string())}).named(
        renames["AcknowledgeRequestIn"]
    )
    types["AcknowledgeRequestOut"] = t.struct(
        {
            "ackIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcknowledgeRequestOut"])
    types["ValidateMessageResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateMessageResponseIn"]
    )
    types["ValidateMessageResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateMessageResponseOut"])
    types["PublishResponseIn"] = t.struct(
        {"messageIds": t.array(t.string()).optional()}
    ).named(renames["PublishResponseIn"])
    types["PublishResponseOut"] = t.struct(
        {
            "messageIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishResponseOut"])
    types["RetryPolicyIn"] = t.struct(
        {
            "minimumBackoff": t.string().optional(),
            "maximumBackoff": t.string().optional(),
        }
    ).named(renames["RetryPolicyIn"])
    types["RetryPolicyOut"] = t.struct(
        {
            "minimumBackoff": t.string().optional(),
            "maximumBackoff": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryPolicyOut"])
    types["MessageStoragePolicyIn"] = t.struct(
        {"allowedPersistenceRegions": t.array(t.string()).optional()}
    ).named(renames["MessageStoragePolicyIn"])
    types["MessageStoragePolicyOut"] = t.struct(
        {
            "allowedPersistenceRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageStoragePolicyOut"])
    types["SchemaIn"] = t.struct(
        {
            "name": t.string(),
            "type": t.string().optional(),
            "definition": t.string().optional(),
        }
    ).named(renames["SchemaIn"])
    types["SchemaOut"] = t.struct(
        {
            "name": t.string(),
            "type": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "definition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaOut"])
    types["PullRequestIn"] = t.struct(
        {"maxMessages": t.integer(), "returnImmediately": t.boolean().optional()}
    ).named(renames["PullRequestIn"])
    types["PullRequestOut"] = t.struct(
        {
            "maxMessages": t.integer(),
            "returnImmediately": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullRequestOut"])
    types["UpdateSnapshotRequestIn"] = t.struct(
        {"snapshot": t.proxy(renames["SnapshotIn"]), "updateMask": t.string()}
    ).named(renames["UpdateSnapshotRequestIn"])
    types["UpdateSnapshotRequestOut"] = t.struct(
        {
            "snapshot": t.proxy(renames["SnapshotOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSnapshotRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["CreateSnapshotRequestIn"] = t.struct(
        {
            "subscription": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CreateSnapshotRequestIn"])
    types["CreateSnapshotRequestOut"] = t.struct(
        {
            "subscription": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateSnapshotRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListTopicsResponseIn"] = t.struct(
        {
            "topics": t.array(t.proxy(renames["TopicIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTopicsResponseIn"])
    types["ListTopicsResponseOut"] = t.struct(
        {
            "topics": t.array(t.proxy(renames["TopicOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTopicsResponseOut"])
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
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["PushConfigIn"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "pushEndpoint": t.string().optional(),
        }
    ).named(renames["PushConfigIn"])
    types["PushConfigOut"] = t.struct(
        {
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "pushEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushConfigOut"])
    types["SeekRequestIn"] = t.struct(
        {"time": t.string().optional(), "snapshot": t.string().optional()}
    ).named(renames["SeekRequestIn"])
    types["SeekRequestOut"] = t.struct(
        {
            "time": t.string().optional(),
            "snapshot": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeekRequestOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "enableMessageOrdering": t.boolean().optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyIn"]).optional(),
            "messageRetentionDuration": t.string().optional(),
            "name": t.string(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyIn"]).optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigIn"]).optional(),
            "pushConfig": t.proxy(renames["PushConfigIn"]).optional(),
            "detached": t.boolean().optional(),
            "filter": t.string().optional(),
            "topic": t.string(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigIn"]).optional(),
            "expirationPolicy": t.proxy(renames["ExpirationPolicyIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retainAckedMessages": t.boolean().optional(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "enableMessageOrdering": t.boolean().optional(),
            "state": t.string().optional(),
            "topicMessageRetentionDuration": t.string().optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyOut"]).optional(),
            "messageRetentionDuration": t.string().optional(),
            "name": t.string(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyOut"]).optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigOut"]).optional(),
            "pushConfig": t.proxy(renames["PushConfigOut"]).optional(),
            "detached": t.boolean().optional(),
            "filter": t.string().optional(),
            "topic": t.string(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigOut"]).optional(),
            "expirationPolicy": t.proxy(renames["ExpirationPolicyOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retainAckedMessages": t.boolean().optional(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["ModifyAckDeadlineRequestIn"] = t.struct(
        {"ackIds": t.array(t.string()), "ackDeadlineSeconds": t.integer()}
    ).named(renames["ModifyAckDeadlineRequestIn"])
    types["ModifyAckDeadlineRequestOut"] = t.struct(
        {
            "ackIds": t.array(t.string()),
            "ackDeadlineSeconds": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyAckDeadlineRequestOut"])
    types["TextConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextConfigIn"]
    )
    types["TextConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextConfigOut"])
    types["SnapshotIn"] = t.struct(
        {
            "topic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["SchemaSettingsIn"] = t.struct(
        {
            "firstRevisionId": t.string().optional(),
            "lastRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
            "schema": t.string(),
        }
    ).named(renames["SchemaSettingsIn"])
    types["SchemaSettingsOut"] = t.struct(
        {
            "firstRevisionId": t.string().optional(),
            "lastRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
            "schema": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaSettingsOut"])
    types["DeadLetterPolicyIn"] = t.struct(
        {
            "deadLetterTopic": t.string().optional(),
            "maxDeliveryAttempts": t.integer().optional(),
        }
    ).named(renames["DeadLetterPolicyIn"])
    types["DeadLetterPolicyOut"] = t.struct(
        {
            "deadLetterTopic": t.string().optional(),
            "maxDeliveryAttempts": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeadLetterPolicyOut"])
    types["ListTopicSubscriptionsResponseIn"] = t.struct(
        {
            "subscriptions": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTopicSubscriptionsResponseIn"])
    types["ListTopicSubscriptionsResponseOut"] = t.struct(
        {
            "subscriptions": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTopicSubscriptionsResponseOut"])
    types["ListSubscriptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subscriptions": t.array(t.proxy(renames["SubscriptionIn"])).optional(),
        }
    ).named(renames["ListSubscriptionsResponseIn"])
    types["ListSubscriptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subscriptions": t.array(t.proxy(renames["SubscriptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSubscriptionsResponseOut"])
    types["PublishRequestIn"] = t.struct(
        {"messages": t.array(t.proxy(renames["PubsubMessageIn"]))}
    ).named(renames["PublishRequestIn"])
    types["PublishRequestOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["PubsubMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishRequestOut"])
    types["ReceivedMessageIn"] = t.struct(
        {
            "message": t.proxy(renames["PubsubMessageIn"]).optional(),
            "deliveryAttempt": t.integer().optional(),
            "ackId": t.string().optional(),
        }
    ).named(renames["ReceivedMessageIn"])
    types["ReceivedMessageOut"] = t.struct(
        {
            "message": t.proxy(renames["PubsubMessageOut"]).optional(),
            "deliveryAttempt": t.integer().optional(),
            "ackId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReceivedMessageOut"])
    types["ListSnapshotsResponseIn"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
    types["ListSchemaRevisionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "schemas": t.array(t.proxy(renames["SchemaIn"])).optional(),
        }
    ).named(renames["ListSchemaRevisionsResponseIn"])
    types["ListSchemaRevisionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "schemas": t.array(t.proxy(renames["SchemaOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSchemaRevisionsResponseOut"])
    types["PullResponseIn"] = t.struct(
        {"receivedMessages": t.array(t.proxy(renames["ReceivedMessageIn"])).optional()}
    ).named(renames["PullResponseIn"])
    types["PullResponseOut"] = t.struct(
        {
            "receivedMessages": t.array(
                t.proxy(renames["ReceivedMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullResponseOut"])
    types["TopicIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyIn"]
            ).optional(),
            "name": t.string(),
            "messageRetentionDuration": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "schemaSettings": t.proxy(renames["SchemaSettingsIn"]).optional(),
            "kmsKeyName": t.string().optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyOut"]
            ).optional(),
            "name": t.string(),
            "messageRetentionDuration": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "schemaSettings": t.proxy(renames["SchemaSettingsOut"]).optional(),
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["BigQueryConfigIn"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "dropUnknownFields": t.boolean().optional(),
            "useTopicSchema": t.boolean().optional(),
            "table": t.string().optional(),
        }
    ).named(renames["BigQueryConfigIn"])
    types["BigQueryConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "dropUnknownFields": t.boolean().optional(),
            "useTopicSchema": t.boolean().optional(),
            "table": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryConfigOut"])
    types["CloudStorageConfigIn"] = t.struct(
        {
            "filenameSuffix": t.string().optional(),
            "filenamePrefix": t.string().optional(),
            "bucket": t.string(),
            "avroConfig": t.proxy(renames["AvroConfigIn"]).optional(),
            "maxDuration": t.string().optional(),
            "maxBytes": t.string().optional(),
            "textConfig": t.proxy(renames["TextConfigIn"]).optional(),
        }
    ).named(renames["CloudStorageConfigIn"])
    types["CloudStorageConfigOut"] = t.struct(
        {
            "filenameSuffix": t.string().optional(),
            "filenamePrefix": t.string().optional(),
            "bucket": t.string(),
            "state": t.string().optional(),
            "avroConfig": t.proxy(renames["AvroConfigOut"]).optional(),
            "maxDuration": t.string().optional(),
            "maxBytes": t.string().optional(),
            "textConfig": t.proxy(renames["TextConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageConfigOut"])
    types["PubsubMessageIn"] = t.struct(
        {
            "data": t.string().optional(),
            "messageId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "publishTime": t.string().optional(),
            "orderingKey": t.string().optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "data": t.string().optional(),
            "messageId": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "publishTime": t.string().optional(),
            "orderingKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["DetachSubscriptionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DetachSubscriptionResponseIn"])
    types["DetachSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetachSubscriptionResponseOut"])
    types["ValidateMessageRequestIn"] = t.struct(
        {
            "message": t.string().optional(),
            "schema": t.proxy(renames["SchemaIn"]).optional(),
            "encoding": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ValidateMessageRequestIn"])
    types["ValidateMessageRequestOut"] = t.struct(
        {
            "message": t.string().optional(),
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "encoding": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateMessageRequestOut"])
    types["UpdateTopicRequestIn"] = t.struct(
        {"topic": t.proxy(renames["TopicIn"]), "updateMask": t.string()}
    ).named(renames["UpdateTopicRequestIn"])
    types["UpdateTopicRequestOut"] = t.struct(
        {
            "topic": t.proxy(renames["TopicOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTopicRequestOut"])

    functions = {}
    functions["projectsSchemasGetIamPolicy"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasListRevisions"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasRollback"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDeleteRevision"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasGet"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidateMessage"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDelete"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasList"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasTestIamPermissions"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCommit"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasSetIamPolicy"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidate"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCreate"] = pubsub.post(
        "v1/{parent}/schemas",
        t.struct(
            {
                "schemaId": t.string().optional(),
                "parent": t.string(),
                "name": t.string(),
                "type": t.string().optional(),
                "definition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SchemaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsDetach"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsCreate"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsList"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsModifyAckDeadline"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsSetIamPolicy"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsTestIamPermissions"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsPull"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsGet"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsModifyPushConfig"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsGetIamPolicy"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsSeek"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsPatch"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsDelete"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsAcknowledge"] = pubsub.post(
        "v1/{subscription}:acknowledge",
        t.struct(
            {
                "subscription": t.string(),
                "ackIds": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsGetIamPolicy"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsCreate"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsList"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSetIamPolicy"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsGet"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsPublish"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsTestIamPermissions"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsDelete"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsPatch"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "topic": t.proxy(renames["TopicIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSubscriptionsList"] = pubsub.get(
        "v1/{topic}/subscriptions",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "topic": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSnapshotsList"] = pubsub.get(
        "v1/{topic}/snapshots",
        t.struct(
            {
                "topic": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsGet"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsDelete"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsPatch"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsSetIamPolicy"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsList"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsGetIamPolicy"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsTestIamPermissions"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsCreate"] = pubsub.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "subscription": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="pubsub", renames=renames, types=types, functions=functions)
