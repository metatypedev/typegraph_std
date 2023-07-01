from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_pubsub():
    pubsub = HTTPRuntime("https://pubsub.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsub_1_ErrorResponse",
        "NoWrapperIn": "_pubsub_2_NoWrapperIn",
        "NoWrapperOut": "_pubsub_3_NoWrapperOut",
        "ModifyPushConfigRequestIn": "_pubsub_4_ModifyPushConfigRequestIn",
        "ModifyPushConfigRequestOut": "_pubsub_5_ModifyPushConfigRequestOut",
        "SeekRequestIn": "_pubsub_6_SeekRequestIn",
        "SeekRequestOut": "_pubsub_7_SeekRequestOut",
        "ExpirationPolicyIn": "_pubsub_8_ExpirationPolicyIn",
        "ExpirationPolicyOut": "_pubsub_9_ExpirationPolicyOut",
        "SetIamPolicyRequestIn": "_pubsub_10_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_pubsub_11_SetIamPolicyRequestOut",
        "SubscriptionIn": "_pubsub_12_SubscriptionIn",
        "SubscriptionOut": "_pubsub_13_SubscriptionOut",
        "SnapshotIn": "_pubsub_14_SnapshotIn",
        "SnapshotOut": "_pubsub_15_SnapshotOut",
        "ListTopicSubscriptionsResponseIn": "_pubsub_16_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsub_17_ListTopicSubscriptionsResponseOut",
        "RetryPolicyIn": "_pubsub_18_RetryPolicyIn",
        "RetryPolicyOut": "_pubsub_19_RetryPolicyOut",
        "PushConfigIn": "_pubsub_20_PushConfigIn",
        "PushConfigOut": "_pubsub_21_PushConfigOut",
        "ListSnapshotsResponseIn": "_pubsub_22_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_pubsub_23_ListSnapshotsResponseOut",
        "AcknowledgeRequestIn": "_pubsub_24_AcknowledgeRequestIn",
        "AcknowledgeRequestOut": "_pubsub_25_AcknowledgeRequestOut",
        "SchemaIn": "_pubsub_26_SchemaIn",
        "SchemaOut": "_pubsub_27_SchemaOut",
        "UpdateSnapshotRequestIn": "_pubsub_28_UpdateSnapshotRequestIn",
        "UpdateSnapshotRequestOut": "_pubsub_29_UpdateSnapshotRequestOut",
        "ValidateSchemaRequestIn": "_pubsub_30_ValidateSchemaRequestIn",
        "ValidateSchemaRequestOut": "_pubsub_31_ValidateSchemaRequestOut",
        "OidcTokenIn": "_pubsub_32_OidcTokenIn",
        "OidcTokenOut": "_pubsub_33_OidcTokenOut",
        "DeadLetterPolicyIn": "_pubsub_34_DeadLetterPolicyIn",
        "DeadLetterPolicyOut": "_pubsub_35_DeadLetterPolicyOut",
        "MessageStoragePolicyIn": "_pubsub_36_MessageStoragePolicyIn",
        "MessageStoragePolicyOut": "_pubsub_37_MessageStoragePolicyOut",
        "ListTopicSnapshotsResponseIn": "_pubsub_38_ListTopicSnapshotsResponseIn",
        "ListTopicSnapshotsResponseOut": "_pubsub_39_ListTopicSnapshotsResponseOut",
        "ListSubscriptionsResponseIn": "_pubsub_40_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsub_41_ListSubscriptionsResponseOut",
        "UpdateSubscriptionRequestIn": "_pubsub_42_UpdateSubscriptionRequestIn",
        "UpdateSubscriptionRequestOut": "_pubsub_43_UpdateSubscriptionRequestOut",
        "PublishRequestIn": "_pubsub_44_PublishRequestIn",
        "PublishRequestOut": "_pubsub_45_PublishRequestOut",
        "ValidateSchemaResponseIn": "_pubsub_46_ValidateSchemaResponseIn",
        "ValidateSchemaResponseOut": "_pubsub_47_ValidateSchemaResponseOut",
        "ReceivedMessageIn": "_pubsub_48_ReceivedMessageIn",
        "ReceivedMessageOut": "_pubsub_49_ReceivedMessageOut",
        "SchemaSettingsIn": "_pubsub_50_SchemaSettingsIn",
        "SchemaSettingsOut": "_pubsub_51_SchemaSettingsOut",
        "UpdateTopicRequestIn": "_pubsub_52_UpdateTopicRequestIn",
        "UpdateTopicRequestOut": "_pubsub_53_UpdateTopicRequestOut",
        "TestIamPermissionsResponseIn": "_pubsub_54_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_pubsub_55_TestIamPermissionsResponseOut",
        "PubsubWrapperIn": "_pubsub_56_PubsubWrapperIn",
        "PubsubWrapperOut": "_pubsub_57_PubsubWrapperOut",
        "SeekResponseIn": "_pubsub_58_SeekResponseIn",
        "SeekResponseOut": "_pubsub_59_SeekResponseOut",
        "PublishResponseIn": "_pubsub_60_PublishResponseIn",
        "PublishResponseOut": "_pubsub_61_PublishResponseOut",
        "ValidateMessageResponseIn": "_pubsub_62_ValidateMessageResponseIn",
        "ValidateMessageResponseOut": "_pubsub_63_ValidateMessageResponseOut",
        "PullRequestIn": "_pubsub_64_PullRequestIn",
        "PullRequestOut": "_pubsub_65_PullRequestOut",
        "ListSchemaRevisionsResponseIn": "_pubsub_66_ListSchemaRevisionsResponseIn",
        "ListSchemaRevisionsResponseOut": "_pubsub_67_ListSchemaRevisionsResponseOut",
        "EmptyIn": "_pubsub_68_EmptyIn",
        "EmptyOut": "_pubsub_69_EmptyOut",
        "DetachSubscriptionResponseIn": "_pubsub_70_DetachSubscriptionResponseIn",
        "DetachSubscriptionResponseOut": "_pubsub_71_DetachSubscriptionResponseOut",
        "PolicyIn": "_pubsub_72_PolicyIn",
        "PolicyOut": "_pubsub_73_PolicyOut",
        "BigQueryConfigIn": "_pubsub_74_BigQueryConfigIn",
        "BigQueryConfigOut": "_pubsub_75_BigQueryConfigOut",
        "ListSchemasResponseIn": "_pubsub_76_ListSchemasResponseIn",
        "ListSchemasResponseOut": "_pubsub_77_ListSchemasResponseOut",
        "PullResponseIn": "_pubsub_78_PullResponseIn",
        "PullResponseOut": "_pubsub_79_PullResponseOut",
        "TopicIn": "_pubsub_80_TopicIn",
        "TopicOut": "_pubsub_81_TopicOut",
        "ListTopicsResponseIn": "_pubsub_82_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsub_83_ListTopicsResponseOut",
        "CloudStorageConfigIn": "_pubsub_84_CloudStorageConfigIn",
        "CloudStorageConfigOut": "_pubsub_85_CloudStorageConfigOut",
        "CreateSnapshotRequestIn": "_pubsub_86_CreateSnapshotRequestIn",
        "CreateSnapshotRequestOut": "_pubsub_87_CreateSnapshotRequestOut",
        "PubsubMessageIn": "_pubsub_88_PubsubMessageIn",
        "PubsubMessageOut": "_pubsub_89_PubsubMessageOut",
        "ExprIn": "_pubsub_90_ExprIn",
        "ExprOut": "_pubsub_91_ExprOut",
        "ValidateMessageRequestIn": "_pubsub_92_ValidateMessageRequestIn",
        "ValidateMessageRequestOut": "_pubsub_93_ValidateMessageRequestOut",
        "TextConfigIn": "_pubsub_94_TextConfigIn",
        "TextConfigOut": "_pubsub_95_TextConfigOut",
        "RollbackSchemaRequestIn": "_pubsub_96_RollbackSchemaRequestIn",
        "RollbackSchemaRequestOut": "_pubsub_97_RollbackSchemaRequestOut",
        "TestIamPermissionsRequestIn": "_pubsub_98_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_pubsub_99_TestIamPermissionsRequestOut",
        "ModifyAckDeadlineRequestIn": "_pubsub_100_ModifyAckDeadlineRequestIn",
        "ModifyAckDeadlineRequestOut": "_pubsub_101_ModifyAckDeadlineRequestOut",
        "BindingIn": "_pubsub_102_BindingIn",
        "BindingOut": "_pubsub_103_BindingOut",
        "AvroConfigIn": "_pubsub_104_AvroConfigIn",
        "AvroConfigOut": "_pubsub_105_AvroConfigOut",
        "CommitSchemaRequestIn": "_pubsub_106_CommitSchemaRequestIn",
        "CommitSchemaRequestOut": "_pubsub_107_CommitSchemaRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NoWrapperIn"] = t.struct({"writeMetadata": t.boolean().optional()}).named(
        renames["NoWrapperIn"]
    )
    types["NoWrapperOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NoWrapperOut"])
    types["ModifyPushConfigRequestIn"] = t.struct(
        {"pushConfig": t.proxy(renames["PushConfigIn"])}
    ).named(renames["ModifyPushConfigRequestIn"])
    types["ModifyPushConfigRequestOut"] = t.struct(
        {
            "pushConfig": t.proxy(renames["PushConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyPushConfigRequestOut"])
    types["SeekRequestIn"] = t.struct(
        {"snapshot": t.string().optional(), "time": t.string().optional()}
    ).named(renames["SeekRequestIn"])
    types["SeekRequestOut"] = t.struct(
        {
            "snapshot": t.string().optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeekRequestOut"])
    types["ExpirationPolicyIn"] = t.struct({"ttl": t.string().optional()}).named(
        renames["ExpirationPolicyIn"]
    )
    types["ExpirationPolicyOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpirationPolicyOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "filter": t.string().optional(),
            "detached": t.boolean().optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "expirationPolicy": t.proxy(renames["ExpirationPolicyIn"]).optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyIn"]).optional(),
            "topic": t.string(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
            "messageRetentionDuration": t.string().optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyIn"]).optional(),
            "name": t.string(),
            "retainAckedMessages": t.boolean().optional(),
            "enableMessageOrdering": t.boolean().optional(),
            "pushConfig": t.proxy(renames["PushConfigIn"]).optional(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigIn"]).optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "filter": t.string().optional(),
            "detached": t.boolean().optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigOut"]).optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "expirationPolicy": t.proxy(renames["ExpirationPolicyOut"]).optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyOut"]).optional(),
            "topic": t.string(),
            "topicMessageRetentionDuration": t.string().optional(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
            "messageRetentionDuration": t.string().optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyOut"]).optional(),
            "name": t.string(),
            "retainAckedMessages": t.boolean().optional(),
            "enableMessageOrdering": t.boolean().optional(),
            "pushConfig": t.proxy(renames["PushConfigOut"]).optional(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["SnapshotIn"] = t.struct(
        {
            "name": t.string().optional(),
            "topic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "name": t.string().optional(),
            "topic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["ListTopicSubscriptionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subscriptions": t.array(t.string()).optional(),
        }
    ).named(renames["ListTopicSubscriptionsResponseIn"])
    types["ListTopicSubscriptionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "subscriptions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTopicSubscriptionsResponseOut"])
    types["RetryPolicyIn"] = t.struct(
        {
            "maximumBackoff": t.string().optional(),
            "minimumBackoff": t.string().optional(),
        }
    ).named(renames["RetryPolicyIn"])
    types["RetryPolicyOut"] = t.struct(
        {
            "maximumBackoff": t.string().optional(),
            "minimumBackoff": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetryPolicyOut"])
    types["PushConfigIn"] = t.struct(
        {
            "pubsubWrapper": t.proxy(renames["PubsubWrapperIn"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "noWrapper": t.proxy(renames["NoWrapperIn"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "pushEndpoint": t.string().optional(),
        }
    ).named(renames["PushConfigIn"])
    types["PushConfigOut"] = t.struct(
        {
            "pubsubWrapper": t.proxy(renames["PubsubWrapperOut"]).optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "noWrapper": t.proxy(renames["NoWrapperOut"]).optional(),
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "pushEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushConfigOut"])
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
    types["AcknowledgeRequestIn"] = t.struct({"ackIds": t.array(t.string())}).named(
        renames["AcknowledgeRequestIn"]
    )
    types["AcknowledgeRequestOut"] = t.struct(
        {
            "ackIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcknowledgeRequestOut"])
    types["SchemaIn"] = t.struct(
        {
            "type": t.string().optional(),
            "definition": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["SchemaIn"])
    types["SchemaOut"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "revisionId": t.string().optional(),
            "type": t.string().optional(),
            "definition": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaOut"])
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
    types["ValidateSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["ValidateSchemaRequestIn"])
    types["ValidateSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateSchemaRequestOut"])
    types["OidcTokenIn"] = t.struct(
        {
            "audience": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
        }
    ).named(renames["OidcTokenIn"])
    types["OidcTokenOut"] = t.struct(
        {
            "audience": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OidcTokenOut"])
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
    types["MessageStoragePolicyIn"] = t.struct(
        {"allowedPersistenceRegions": t.array(t.string()).optional()}
    ).named(renames["MessageStoragePolicyIn"])
    types["MessageStoragePolicyOut"] = t.struct(
        {
            "allowedPersistenceRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageStoragePolicyOut"])
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
    types["ListSubscriptionsResponseIn"] = t.struct(
        {
            "subscriptions": t.array(t.proxy(renames["SubscriptionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSubscriptionsResponseIn"])
    types["ListSubscriptionsResponseOut"] = t.struct(
        {
            "subscriptions": t.array(t.proxy(renames["SubscriptionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSubscriptionsResponseOut"])
    types["UpdateSubscriptionRequestIn"] = t.struct(
        {"updateMask": t.string(), "subscription": t.proxy(renames["SubscriptionIn"])}
    ).named(renames["UpdateSubscriptionRequestIn"])
    types["UpdateSubscriptionRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "subscription": t.proxy(renames["SubscriptionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSubscriptionRequestOut"])
    types["PublishRequestIn"] = t.struct(
        {"messages": t.array(t.proxy(renames["PubsubMessageIn"]))}
    ).named(renames["PublishRequestIn"])
    types["PublishRequestOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["PubsubMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishRequestOut"])
    types["ValidateSchemaResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateSchemaResponseIn"]
    )
    types["ValidateSchemaResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateSchemaResponseOut"])
    types["ReceivedMessageIn"] = t.struct(
        {
            "ackId": t.string().optional(),
            "message": t.proxy(renames["PubsubMessageIn"]).optional(),
            "deliveryAttempt": t.integer().optional(),
        }
    ).named(renames["ReceivedMessageIn"])
    types["ReceivedMessageOut"] = t.struct(
        {
            "ackId": t.string().optional(),
            "message": t.proxy(renames["PubsubMessageOut"]).optional(),
            "deliveryAttempt": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReceivedMessageOut"])
    types["SchemaSettingsIn"] = t.struct(
        {
            "firstRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
            "lastRevisionId": t.string().optional(),
            "schema": t.string(),
        }
    ).named(renames["SchemaSettingsIn"])
    types["SchemaSettingsOut"] = t.struct(
        {
            "firstRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
            "lastRevisionId": t.string().optional(),
            "schema": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaSettingsOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PubsubWrapperIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PubsubWrapperIn"]
    )
    types["PubsubWrapperOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PubsubWrapperOut"])
    types["SeekResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekResponseIn"]
    )
    types["SeekResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekResponseOut"])
    types["PublishResponseIn"] = t.struct(
        {"messageIds": t.array(t.string()).optional()}
    ).named(renames["PublishResponseIn"])
    types["PublishResponseOut"] = t.struct(
        {
            "messageIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishResponseOut"])
    types["ValidateMessageResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateMessageResponseIn"]
    )
    types["ValidateMessageResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateMessageResponseOut"])
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
    types["ListSchemaRevisionsResponseIn"] = t.struct(
        {
            "schemas": t.array(t.proxy(renames["SchemaIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSchemaRevisionsResponseIn"])
    types["ListSchemaRevisionsResponseOut"] = t.struct(
        {
            "schemas": t.array(t.proxy(renames["SchemaOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSchemaRevisionsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DetachSubscriptionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DetachSubscriptionResponseIn"])
    types["DetachSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetachSubscriptionResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["BigQueryConfigIn"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "useTopicSchema": t.boolean().optional(),
            "table": t.string().optional(),
            "dropUnknownFields": t.boolean().optional(),
        }
    ).named(renames["BigQueryConfigIn"])
    types["BigQueryConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "useTopicSchema": t.boolean().optional(),
            "table": t.string().optional(),
            "state": t.string().optional(),
            "dropUnknownFields": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryConfigOut"])
    types["ListSchemasResponseIn"] = t.struct(
        {
            "schemas": t.array(t.proxy(renames["SchemaIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSchemasResponseIn"])
    types["ListSchemasResponseOut"] = t.struct(
        {
            "schemas": t.array(t.proxy(renames["SchemaOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSchemasResponseOut"])
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
            "schemaSettings": t.proxy(renames["SchemaSettingsIn"]).optional(),
            "messageRetentionDuration": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "kmsKeyName": t.string().optional(),
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyIn"]
            ).optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "schemaSettings": t.proxy(renames["SchemaSettingsOut"]).optional(),
            "messageRetentionDuration": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "kmsKeyName": t.string().optional(),
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["ListTopicsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "topics": t.array(t.proxy(renames["TopicIn"])).optional(),
        }
    ).named(renames["ListTopicsResponseIn"])
    types["ListTopicsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "topics": t.array(t.proxy(renames["TopicOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTopicsResponseOut"])
    types["CloudStorageConfigIn"] = t.struct(
        {
            "textConfig": t.proxy(renames["TextConfigIn"]).optional(),
            "maxDuration": t.string().optional(),
            "maxBytes": t.string().optional(),
            "filenameSuffix": t.string().optional(),
            "bucket": t.string(),
            "avroConfig": t.proxy(renames["AvroConfigIn"]).optional(),
            "filenamePrefix": t.string().optional(),
        }
    ).named(renames["CloudStorageConfigIn"])
    types["CloudStorageConfigOut"] = t.struct(
        {
            "textConfig": t.proxy(renames["TextConfigOut"]).optional(),
            "maxDuration": t.string().optional(),
            "maxBytes": t.string().optional(),
            "filenameSuffix": t.string().optional(),
            "bucket": t.string(),
            "avroConfig": t.proxy(renames["AvroConfigOut"]).optional(),
            "filenamePrefix": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageConfigOut"])
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
    types["PubsubMessageIn"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "publishTime": t.string().optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
            "data": t.string().optional(),
            "publishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ValidateMessageRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "message": t.string().optional(),
            "schema": t.proxy(renames["SchemaIn"]).optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["ValidateMessageRequestIn"])
    types["ValidateMessageRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "message": t.string().optional(),
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "encoding": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateMessageRequestOut"])
    types["TextConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextConfigIn"]
    )
    types["TextConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextConfigOut"])
    types["RollbackSchemaRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackSchemaRequestIn"]
    )
    types["RollbackSchemaRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackSchemaRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ModifyAckDeadlineRequestIn"] = t.struct(
        {"ackDeadlineSeconds": t.integer(), "ackIds": t.array(t.string())}
    ).named(renames["ModifyAckDeadlineRequestIn"])
    types["ModifyAckDeadlineRequestOut"] = t.struct(
        {
            "ackDeadlineSeconds": t.integer(),
            "ackIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyAckDeadlineRequestOut"])
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
    types["AvroConfigIn"] = t.struct({"writeMetadata": t.boolean().optional()}).named(
        renames["AvroConfigIn"]
    )
    types["AvroConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvroConfigOut"])
    types["CommitSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["CommitSchemaRequestIn"])
    types["CommitSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitSchemaRequestOut"])

    functions = {}
    functions["projectsSubscriptionsGet"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsModifyAckDeadline"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsGetIamPolicy"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsModifyPushConfig"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsDelete"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsSetIamPolicy"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsPull"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsTestIamPermissions"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsSeek"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsDetach"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsCreate"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsAcknowledge"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsList"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsPatch"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "updateMask": t.string(),
                "subscription": t.proxy(renames["SubscriptionIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SubscriptionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidate"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDelete"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasListRevisions"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCommit"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasSetIamPolicy"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasGet"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCreate"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDeleteRevision"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasList"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasRollback"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasGetIamPolicy"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasTestIamPermissions"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidateMessage"] = pubsub.post(
        "v1/{parent}/schemas:validateMessage",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "message": t.string().optional(),
                "schema": t.proxy(renames["SchemaIn"]).optional(),
                "encoding": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ValidateMessageResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsPublish"] = pubsub.post(
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
    functions["projectsTopicsPatch"] = pubsub.post(
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
    functions["projectsTopicsList"] = pubsub.post(
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
    functions["projectsTopicsDelete"] = pubsub.post(
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
    functions["projectsTopicsCreate"] = pubsub.post(
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
    functions["projectsTopicsSetIamPolicy"] = pubsub.post(
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
    functions["projectsTopicsGetIamPolicy"] = pubsub.post(
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
    functions["projectsTopicsGet"] = pubsub.post(
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
    functions["projectsTopicsTestIamPermissions"] = pubsub.post(
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
    functions["projectsSnapshotsTestIamPermissions"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsSetIamPolicy"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsGetIamPolicy"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsCreate"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsList"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsGet"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsDelete"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSnapshotsPatch"] = pubsub.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "snapshot": t.proxy(renames["SnapshotIn"]),
                "updateMask": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="pubsub", renames=renames, types=Box(types), functions=Box(functions)
    )
