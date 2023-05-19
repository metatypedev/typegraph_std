from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_pubsub() -> Import:
    pubsub = HTTPRuntime("https://pubsub.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsub_1_ErrorResponse",
        "CloudStorageConfigIn": "_pubsub_2_CloudStorageConfigIn",
        "CloudStorageConfigOut": "_pubsub_3_CloudStorageConfigOut",
        "PublishResponseIn": "_pubsub_4_PublishResponseIn",
        "PublishResponseOut": "_pubsub_5_PublishResponseOut",
        "ValidateMessageRequestIn": "_pubsub_6_ValidateMessageRequestIn",
        "ValidateMessageRequestOut": "_pubsub_7_ValidateMessageRequestOut",
        "SeekRequestIn": "_pubsub_8_SeekRequestIn",
        "SeekRequestOut": "_pubsub_9_SeekRequestOut",
        "SchemaSettingsIn": "_pubsub_10_SchemaSettingsIn",
        "SchemaSettingsOut": "_pubsub_11_SchemaSettingsOut",
        "DeadLetterPolicyIn": "_pubsub_12_DeadLetterPolicyIn",
        "DeadLetterPolicyOut": "_pubsub_13_DeadLetterPolicyOut",
        "ValidateMessageResponseIn": "_pubsub_14_ValidateMessageResponseIn",
        "ValidateMessageResponseOut": "_pubsub_15_ValidateMessageResponseOut",
        "PullRequestIn": "_pubsub_16_PullRequestIn",
        "PullRequestOut": "_pubsub_17_PullRequestOut",
        "SchemaIn": "_pubsub_18_SchemaIn",
        "SchemaOut": "_pubsub_19_SchemaOut",
        "TestIamPermissionsResponseIn": "_pubsub_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_pubsub_21_TestIamPermissionsResponseOut",
        "BindingIn": "_pubsub_22_BindingIn",
        "BindingOut": "_pubsub_23_BindingOut",
        "AvroConfigIn": "_pubsub_24_AvroConfigIn",
        "AvroConfigOut": "_pubsub_25_AvroConfigOut",
        "ReceivedMessageIn": "_pubsub_26_ReceivedMessageIn",
        "ReceivedMessageOut": "_pubsub_27_ReceivedMessageOut",
        "ModifyAckDeadlineRequestIn": "_pubsub_28_ModifyAckDeadlineRequestIn",
        "ModifyAckDeadlineRequestOut": "_pubsub_29_ModifyAckDeadlineRequestOut",
        "OidcTokenIn": "_pubsub_30_OidcTokenIn",
        "OidcTokenOut": "_pubsub_31_OidcTokenOut",
        "PullResponseIn": "_pubsub_32_PullResponseIn",
        "PullResponseOut": "_pubsub_33_PullResponseOut",
        "ValidateSchemaRequestIn": "_pubsub_34_ValidateSchemaRequestIn",
        "ValidateSchemaRequestOut": "_pubsub_35_ValidateSchemaRequestOut",
        "TestIamPermissionsRequestIn": "_pubsub_36_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_pubsub_37_TestIamPermissionsRequestOut",
        "ModifyPushConfigRequestIn": "_pubsub_38_ModifyPushConfigRequestIn",
        "ModifyPushConfigRequestOut": "_pubsub_39_ModifyPushConfigRequestOut",
        "CommitSchemaRequestIn": "_pubsub_40_CommitSchemaRequestIn",
        "CommitSchemaRequestOut": "_pubsub_41_CommitSchemaRequestOut",
        "PubsubMessageIn": "_pubsub_42_PubsubMessageIn",
        "PubsubMessageOut": "_pubsub_43_PubsubMessageOut",
        "SetIamPolicyRequestIn": "_pubsub_44_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_pubsub_45_SetIamPolicyRequestOut",
        "ListSubscriptionsResponseIn": "_pubsub_46_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsub_47_ListSubscriptionsResponseOut",
        "BigQueryConfigIn": "_pubsub_48_BigQueryConfigIn",
        "BigQueryConfigOut": "_pubsub_49_BigQueryConfigOut",
        "DetachSubscriptionResponseIn": "_pubsub_50_DetachSubscriptionResponseIn",
        "DetachSubscriptionResponseOut": "_pubsub_51_DetachSubscriptionResponseOut",
        "ListTopicSnapshotsResponseIn": "_pubsub_52_ListTopicSnapshotsResponseIn",
        "ListTopicSnapshotsResponseOut": "_pubsub_53_ListTopicSnapshotsResponseOut",
        "PolicyIn": "_pubsub_54_PolicyIn",
        "PolicyOut": "_pubsub_55_PolicyOut",
        "UpdateSubscriptionRequestIn": "_pubsub_56_UpdateSubscriptionRequestIn",
        "UpdateSubscriptionRequestOut": "_pubsub_57_UpdateSubscriptionRequestOut",
        "ExpirationPolicyIn": "_pubsub_58_ExpirationPolicyIn",
        "ExpirationPolicyOut": "_pubsub_59_ExpirationPolicyOut",
        "SubscriptionIn": "_pubsub_60_SubscriptionIn",
        "SubscriptionOut": "_pubsub_61_SubscriptionOut",
        "ListSchemaRevisionsResponseIn": "_pubsub_62_ListSchemaRevisionsResponseIn",
        "ListSchemaRevisionsResponseOut": "_pubsub_63_ListSchemaRevisionsResponseOut",
        "PublishRequestIn": "_pubsub_64_PublishRequestIn",
        "PublishRequestOut": "_pubsub_65_PublishRequestOut",
        "RetryPolicyIn": "_pubsub_66_RetryPolicyIn",
        "RetryPolicyOut": "_pubsub_67_RetryPolicyOut",
        "ValidateSchemaResponseIn": "_pubsub_68_ValidateSchemaResponseIn",
        "ValidateSchemaResponseOut": "_pubsub_69_ValidateSchemaResponseOut",
        "ListSchemasResponseIn": "_pubsub_70_ListSchemasResponseIn",
        "ListSchemasResponseOut": "_pubsub_71_ListSchemasResponseOut",
        "SeekResponseIn": "_pubsub_72_SeekResponseIn",
        "SeekResponseOut": "_pubsub_73_SeekResponseOut",
        "CreateSnapshotRequestIn": "_pubsub_74_CreateSnapshotRequestIn",
        "CreateSnapshotRequestOut": "_pubsub_75_CreateSnapshotRequestOut",
        "ListSnapshotsResponseIn": "_pubsub_76_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_pubsub_77_ListSnapshotsResponseOut",
        "MessageStoragePolicyIn": "_pubsub_78_MessageStoragePolicyIn",
        "MessageStoragePolicyOut": "_pubsub_79_MessageStoragePolicyOut",
        "UpdateSnapshotRequestIn": "_pubsub_80_UpdateSnapshotRequestIn",
        "UpdateSnapshotRequestOut": "_pubsub_81_UpdateSnapshotRequestOut",
        "TopicIn": "_pubsub_82_TopicIn",
        "TopicOut": "_pubsub_83_TopicOut",
        "ListTopicsResponseIn": "_pubsub_84_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsub_85_ListTopicsResponseOut",
        "UpdateTopicRequestIn": "_pubsub_86_UpdateTopicRequestIn",
        "UpdateTopicRequestOut": "_pubsub_87_UpdateTopicRequestOut",
        "SnapshotIn": "_pubsub_88_SnapshotIn",
        "SnapshotOut": "_pubsub_89_SnapshotOut",
        "RollbackSchemaRequestIn": "_pubsub_90_RollbackSchemaRequestIn",
        "RollbackSchemaRequestOut": "_pubsub_91_RollbackSchemaRequestOut",
        "AcknowledgeRequestIn": "_pubsub_92_AcknowledgeRequestIn",
        "AcknowledgeRequestOut": "_pubsub_93_AcknowledgeRequestOut",
        "TextConfigIn": "_pubsub_94_TextConfigIn",
        "TextConfigOut": "_pubsub_95_TextConfigOut",
        "ExprIn": "_pubsub_96_ExprIn",
        "ExprOut": "_pubsub_97_ExprOut",
        "EmptyIn": "_pubsub_98_EmptyIn",
        "EmptyOut": "_pubsub_99_EmptyOut",
        "ListTopicSubscriptionsResponseIn": "_pubsub_100_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsub_101_ListTopicSubscriptionsResponseOut",
        "PushConfigIn": "_pubsub_102_PushConfigIn",
        "PushConfigOut": "_pubsub_103_PushConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CloudStorageConfigIn"] = t.struct(
        {
            "bucket": t.string(),
            "avroConfig": t.proxy(renames["AvroConfigIn"]).optional(),
            "textConfig": t.proxy(renames["TextConfigIn"]).optional(),
            "filenameSuffix": t.string().optional(),
            "maxDuration": t.string().optional(),
            "maxBytes": t.string().optional(),
            "filenamePrefix": t.string().optional(),
        }
    ).named(renames["CloudStorageConfigIn"])
    types["CloudStorageConfigOut"] = t.struct(
        {
            "bucket": t.string(),
            "avroConfig": t.proxy(renames["AvroConfigOut"]).optional(),
            "state": t.string().optional(),
            "textConfig": t.proxy(renames["TextConfigOut"]).optional(),
            "filenameSuffix": t.string().optional(),
            "maxDuration": t.string().optional(),
            "maxBytes": t.string().optional(),
            "filenamePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageConfigOut"])
    types["PublishResponseIn"] = t.struct(
        {"messageIds": t.array(t.string()).optional()}
    ).named(renames["PublishResponseIn"])
    types["PublishResponseOut"] = t.struct(
        {
            "messageIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishResponseOut"])
    types["ValidateMessageRequestIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "message": t.string().optional(),
            "name": t.string().optional(),
            "schema": t.proxy(renames["SchemaIn"]).optional(),
        }
    ).named(renames["ValidateMessageRequestIn"])
    types["ValidateMessageRequestOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "message": t.string().optional(),
            "name": t.string().optional(),
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateMessageRequestOut"])
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
    types["SchemaSettingsIn"] = t.struct(
        {
            "firstRevisionId": t.string().optional(),
            "schema": t.string(),
            "lastRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
        }
    ).named(renames["SchemaSettingsIn"])
    types["SchemaSettingsOut"] = t.struct(
        {
            "firstRevisionId": t.string().optional(),
            "schema": t.string(),
            "lastRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
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
    types["ValidateMessageResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateMessageResponseIn"]
    )
    types["ValidateMessageResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateMessageResponseOut"])
    types["PullRequestIn"] = t.struct(
        {"returnImmediately": t.boolean().optional(), "maxMessages": t.integer()}
    ).named(renames["PullRequestIn"])
    types["PullRequestOut"] = t.struct(
        {
            "returnImmediately": t.boolean().optional(),
            "maxMessages": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PullRequestOut"])
    types["SchemaIn"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string(),
            "definition": t.string().optional(),
        }
    ).named(renames["SchemaIn"])
    types["SchemaOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string(),
            "revisionCreateTime": t.string().optional(),
            "definition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["AvroConfigIn"] = t.struct({"writeMetadata": t.boolean().optional()}).named(
        renames["AvroConfigIn"]
    )
    types["AvroConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvroConfigOut"])
    types["ReceivedMessageIn"] = t.struct(
        {
            "message": t.proxy(renames["PubsubMessageIn"]).optional(),
            "ackId": t.string().optional(),
            "deliveryAttempt": t.integer().optional(),
        }
    ).named(renames["ReceivedMessageIn"])
    types["ReceivedMessageOut"] = t.struct(
        {
            "message": t.proxy(renames["PubsubMessageOut"]).optional(),
            "ackId": t.string().optional(),
            "deliveryAttempt": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReceivedMessageOut"])
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
    types["ValidateSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["ValidateSchemaRequestIn"])
    types["ValidateSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateSchemaRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ModifyPushConfigRequestIn"] = t.struct(
        {"pushConfig": t.proxy(renames["PushConfigIn"])}
    ).named(renames["ModifyPushConfigRequestIn"])
    types["ModifyPushConfigRequestOut"] = t.struct(
        {
            "pushConfig": t.proxy(renames["PushConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyPushConfigRequestOut"])
    types["CommitSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["CommitSchemaRequestIn"])
    types["CommitSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitSchemaRequestOut"])
    types["PubsubMessageIn"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "data": t.string().optional(),
            "publishTime": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "orderingKey": t.string().optional(),
            "data": t.string().optional(),
            "publishTime": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "messageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
    types["BigQueryConfigIn"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "useTopicSchema": t.boolean().optional(),
            "dropUnknownFields": t.boolean().optional(),
            "table": t.string().optional(),
        }
    ).named(renames["BigQueryConfigIn"])
    types["BigQueryConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "useTopicSchema": t.boolean().optional(),
            "dropUnknownFields": t.boolean().optional(),
            "table": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryConfigOut"])
    types["DetachSubscriptionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DetachSubscriptionResponseIn"])
    types["DetachSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetachSubscriptionResponseOut"])
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
    types["ExpirationPolicyIn"] = t.struct({"ttl": t.string().optional()}).named(
        renames["ExpirationPolicyIn"]
    )
    types["ExpirationPolicyOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpirationPolicyOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "messageRetentionDuration": t.string().optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "detached": t.boolean().optional(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
            "name": t.string(),
            "filter": t.string().optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyIn"]).optional(),
            "pushConfig": t.proxy(renames["PushConfigIn"]).optional(),
            "topic": t.string(),
            "expirationPolicy": t.proxy(renames["ExpirationPolicyIn"]).optional(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyIn"]).optional(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigIn"]).optional(),
            "enableMessageOrdering": t.boolean().optional(),
            "retainAckedMessages": t.boolean().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "messageRetentionDuration": t.string().optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "detached": t.boolean().optional(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
            "name": t.string(),
            "filter": t.string().optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyOut"]).optional(),
            "topicMessageRetentionDuration": t.string().optional(),
            "pushConfig": t.proxy(renames["PushConfigOut"]).optional(),
            "state": t.string().optional(),
            "topic": t.string(),
            "expirationPolicy": t.proxy(renames["ExpirationPolicyOut"]).optional(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyOut"]).optional(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigOut"]).optional(),
            "enableMessageOrdering": t.boolean().optional(),
            "retainAckedMessages": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
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
    types["PublishRequestIn"] = t.struct(
        {"messages": t.array(t.proxy(renames["PubsubMessageIn"]))}
    ).named(renames["PublishRequestIn"])
    types["PublishRequestOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["PubsubMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishRequestOut"])
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
    types["ValidateSchemaResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateSchemaResponseIn"]
    )
    types["ValidateSchemaResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateSchemaResponseOut"])
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
    types["SeekResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekResponseIn"]
    )
    types["SeekResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekResponseOut"])
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
    types["ListSnapshotsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snapshots": t.array(t.proxy(renames["SnapshotIn"])).optional(),
        }
    ).named(renames["ListSnapshotsResponseIn"])
    types["ListSnapshotsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "snapshots": t.array(t.proxy(renames["SnapshotOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSnapshotsResponseOut"])
    types["MessageStoragePolicyIn"] = t.struct(
        {"allowedPersistenceRegions": t.array(t.string()).optional()}
    ).named(renames["MessageStoragePolicyIn"])
    types["MessageStoragePolicyOut"] = t.struct(
        {
            "allowedPersistenceRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageStoragePolicyOut"])
    types["UpdateSnapshotRequestIn"] = t.struct(
        {"updateMask": t.string(), "snapshot": t.proxy(renames["SnapshotIn"])}
    ).named(renames["UpdateSnapshotRequestIn"])
    types["UpdateSnapshotRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "snapshot": t.proxy(renames["SnapshotOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSnapshotRequestOut"])
    types["TopicIn"] = t.struct(
        {
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyIn"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "name": t.string(),
            "schemaSettings": t.proxy(renames["SchemaSettingsIn"]).optional(),
            "messageRetentionDuration": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyOut"]
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "name": t.string(),
            "schemaSettings": t.proxy(renames["SchemaSettingsOut"]).optional(),
            "messageRetentionDuration": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
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
    types["UpdateTopicRequestIn"] = t.struct(
        {"updateMask": t.string(), "topic": t.proxy(renames["TopicIn"])}
    ).named(renames["UpdateTopicRequestIn"])
    types["UpdateTopicRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "topic": t.proxy(renames["TopicOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateTopicRequestOut"])
    types["SnapshotIn"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "name": t.string().optional(),
            "topic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SnapshotIn"])
    types["SnapshotOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "name": t.string().optional(),
            "topic": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotOut"])
    types["RollbackSchemaRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackSchemaRequestIn"]
    )
    types["RollbackSchemaRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackSchemaRequestOut"])
    types["AcknowledgeRequestIn"] = t.struct({"ackIds": t.array(t.string())}).named(
        renames["AcknowledgeRequestIn"]
    )
    types["AcknowledgeRequestOut"] = t.struct(
        {
            "ackIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcknowledgeRequestOut"])
    types["TextConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextConfigIn"]
    )
    types["TextConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextConfigOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["PushConfigIn"] = t.struct(
        {
            "oidcToken": t.proxy(renames["OidcTokenIn"]).optional(),
            "pushEndpoint": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PushConfigIn"])
    types["PushConfigOut"] = t.struct(
        {
            "oidcToken": t.proxy(renames["OidcTokenOut"]).optional(),
            "pushEndpoint": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PushConfigOut"])

    functions = {}
    functions["projectsSubscriptionsSeek"] = pubsub.post(
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
    functions["projectsSubscriptionsDetach"] = pubsub.post(
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
    functions["projectsSubscriptionsDelete"] = pubsub.post(
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
    functions["projectsSubscriptionsSetIamPolicy"] = pubsub.post(
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
    functions["projectsSubscriptionsList"] = pubsub.post(
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
    functions["projectsSubscriptionsPull"] = pubsub.post(
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
    functions["projectsSubscriptionsGetIamPolicy"] = pubsub.post(
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
    functions["projectsSubscriptionsModifyAckDeadline"] = pubsub.post(
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
    functions["projectsSubscriptionsPatch"] = pubsub.post(
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
    functions["projectsSubscriptionsModifyPushConfig"] = pubsub.post(
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
    functions["projectsSubscriptionsCreate"] = pubsub.post(
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
    functions["projectsSubscriptionsGet"] = pubsub.post(
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
    functions["projectsSubscriptionsAcknowledge"] = pubsub.post(
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
    functions["projectsSubscriptionsTestIamPermissions"] = pubsub.post(
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
    functions["projectsTopicsPatch"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsCreate"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsTestIamPermissions"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsDelete"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSetIamPolicy"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsGet"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsGetIamPolicy"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsList"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsPublish"] = pubsub.post(
        "v1/{topic}:publish",
        t.struct(
            {
                "topic": t.string(),
                "messages": t.array(t.proxy(renames["PubsubMessageIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PublishResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSnapshotsList"] = pubsub.get(
        "v1/{topic}/snapshots",
        t.struct(
            {
                "topic": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSubscriptionsList"] = pubsub.get(
        "v1/{topic}/subscriptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "topic": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasList"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasListRevisions"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCreate"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDeleteRevision"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasTestIamPermissions"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasRollback"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasGet"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidate"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasGetIamPolicy"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidateMessage"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasSetIamPolicy"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCommit"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDelete"] = pubsub.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="pubsub", renames=renames, types=Box(types), functions=Box(functions)
    )
