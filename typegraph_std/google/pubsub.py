from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_pubsub() -> Import:
    pubsub = HTTPRuntime("https://pubsub.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsub_1_ErrorResponse",
        "ExprIn": "_pubsub_2_ExprIn",
        "ExprOut": "_pubsub_3_ExprOut",
        "BindingIn": "_pubsub_4_BindingIn",
        "BindingOut": "_pubsub_5_BindingOut",
        "ListSchemaRevisionsResponseIn": "_pubsub_6_ListSchemaRevisionsResponseIn",
        "ListSchemaRevisionsResponseOut": "_pubsub_7_ListSchemaRevisionsResponseOut",
        "PullResponseIn": "_pubsub_8_PullResponseIn",
        "PullResponseOut": "_pubsub_9_PullResponseOut",
        "PolicyIn": "_pubsub_10_PolicyIn",
        "PolicyOut": "_pubsub_11_PolicyOut",
        "PushConfigIn": "_pubsub_12_PushConfigIn",
        "PushConfigOut": "_pubsub_13_PushConfigOut",
        "SeekResponseIn": "_pubsub_14_SeekResponseIn",
        "SeekResponseOut": "_pubsub_15_SeekResponseOut",
        "CommitSchemaRequestIn": "_pubsub_16_CommitSchemaRequestIn",
        "CommitSchemaRequestOut": "_pubsub_17_CommitSchemaRequestOut",
        "PublishRequestIn": "_pubsub_18_PublishRequestIn",
        "PublishRequestOut": "_pubsub_19_PublishRequestOut",
        "TestIamPermissionsResponseIn": "_pubsub_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_pubsub_21_TestIamPermissionsResponseOut",
        "TopicIn": "_pubsub_22_TopicIn",
        "TopicOut": "_pubsub_23_TopicOut",
        "SchemaSettingsIn": "_pubsub_24_SchemaSettingsIn",
        "SchemaSettingsOut": "_pubsub_25_SchemaSettingsOut",
        "PullRequestIn": "_pubsub_26_PullRequestIn",
        "PullRequestOut": "_pubsub_27_PullRequestOut",
        "DeadLetterPolicyIn": "_pubsub_28_DeadLetterPolicyIn",
        "DeadLetterPolicyOut": "_pubsub_29_DeadLetterPolicyOut",
        "ListSchemasResponseIn": "_pubsub_30_ListSchemasResponseIn",
        "ListSchemasResponseOut": "_pubsub_31_ListSchemasResponseOut",
        "TextConfigIn": "_pubsub_32_TextConfigIn",
        "TextConfigOut": "_pubsub_33_TextConfigOut",
        "UpdateSubscriptionRequestIn": "_pubsub_34_UpdateSubscriptionRequestIn",
        "UpdateSubscriptionRequestOut": "_pubsub_35_UpdateSubscriptionRequestOut",
        "ListTopicSnapshotsResponseIn": "_pubsub_36_ListTopicSnapshotsResponseIn",
        "ListTopicSnapshotsResponseOut": "_pubsub_37_ListTopicSnapshotsResponseOut",
        "SnapshotIn": "_pubsub_38_SnapshotIn",
        "SnapshotOut": "_pubsub_39_SnapshotOut",
        "ExpirationPolicyIn": "_pubsub_40_ExpirationPolicyIn",
        "ExpirationPolicyOut": "_pubsub_41_ExpirationPolicyOut",
        "ModifyAckDeadlineRequestIn": "_pubsub_42_ModifyAckDeadlineRequestIn",
        "ModifyAckDeadlineRequestOut": "_pubsub_43_ModifyAckDeadlineRequestOut",
        "CreateSnapshotRequestIn": "_pubsub_44_CreateSnapshotRequestIn",
        "CreateSnapshotRequestOut": "_pubsub_45_CreateSnapshotRequestOut",
        "ModifyPushConfigRequestIn": "_pubsub_46_ModifyPushConfigRequestIn",
        "ModifyPushConfigRequestOut": "_pubsub_47_ModifyPushConfigRequestOut",
        "CloudStorageConfigIn": "_pubsub_48_CloudStorageConfigIn",
        "CloudStorageConfigOut": "_pubsub_49_CloudStorageConfigOut",
        "BigQueryConfigIn": "_pubsub_50_BigQueryConfigIn",
        "BigQueryConfigOut": "_pubsub_51_BigQueryConfigOut",
        "DetachSubscriptionResponseIn": "_pubsub_52_DetachSubscriptionResponseIn",
        "DetachSubscriptionResponseOut": "_pubsub_53_DetachSubscriptionResponseOut",
        "OidcTokenIn": "_pubsub_54_OidcTokenIn",
        "OidcTokenOut": "_pubsub_55_OidcTokenOut",
        "TestIamPermissionsRequestIn": "_pubsub_56_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_pubsub_57_TestIamPermissionsRequestOut",
        "ListSubscriptionsResponseIn": "_pubsub_58_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsub_59_ListSubscriptionsResponseOut",
        "PubsubMessageIn": "_pubsub_60_PubsubMessageIn",
        "PubsubMessageOut": "_pubsub_61_PubsubMessageOut",
        "SeekRequestIn": "_pubsub_62_SeekRequestIn",
        "SeekRequestOut": "_pubsub_63_SeekRequestOut",
        "RetryPolicyIn": "_pubsub_64_RetryPolicyIn",
        "RetryPolicyOut": "_pubsub_65_RetryPolicyOut",
        "ValidateMessageResponseIn": "_pubsub_66_ValidateMessageResponseIn",
        "ValidateMessageResponseOut": "_pubsub_67_ValidateMessageResponseOut",
        "AvroConfigIn": "_pubsub_68_AvroConfigIn",
        "AvroConfigOut": "_pubsub_69_AvroConfigOut",
        "ValidateSchemaResponseIn": "_pubsub_70_ValidateSchemaResponseIn",
        "ValidateSchemaResponseOut": "_pubsub_71_ValidateSchemaResponseOut",
        "MessageStoragePolicyIn": "_pubsub_72_MessageStoragePolicyIn",
        "MessageStoragePolicyOut": "_pubsub_73_MessageStoragePolicyOut",
        "ListSnapshotsResponseIn": "_pubsub_74_ListSnapshotsResponseIn",
        "ListSnapshotsResponseOut": "_pubsub_75_ListSnapshotsResponseOut",
        "ListTopicSubscriptionsResponseIn": "_pubsub_76_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsub_77_ListTopicSubscriptionsResponseOut",
        "RollbackSchemaRequestIn": "_pubsub_78_RollbackSchemaRequestIn",
        "RollbackSchemaRequestOut": "_pubsub_79_RollbackSchemaRequestOut",
        "SetIamPolicyRequestIn": "_pubsub_80_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_pubsub_81_SetIamPolicyRequestOut",
        "UpdateTopicRequestIn": "_pubsub_82_UpdateTopicRequestIn",
        "UpdateTopicRequestOut": "_pubsub_83_UpdateTopicRequestOut",
        "UpdateSnapshotRequestIn": "_pubsub_84_UpdateSnapshotRequestIn",
        "UpdateSnapshotRequestOut": "_pubsub_85_UpdateSnapshotRequestOut",
        "ReceivedMessageIn": "_pubsub_86_ReceivedMessageIn",
        "ReceivedMessageOut": "_pubsub_87_ReceivedMessageOut",
        "SchemaIn": "_pubsub_88_SchemaIn",
        "SchemaOut": "_pubsub_89_SchemaOut",
        "EmptyIn": "_pubsub_90_EmptyIn",
        "EmptyOut": "_pubsub_91_EmptyOut",
        "ValidateMessageRequestIn": "_pubsub_92_ValidateMessageRequestIn",
        "ValidateMessageRequestOut": "_pubsub_93_ValidateMessageRequestOut",
        "ValidateSchemaRequestIn": "_pubsub_94_ValidateSchemaRequestIn",
        "ValidateSchemaRequestOut": "_pubsub_95_ValidateSchemaRequestOut",
        "AcknowledgeRequestIn": "_pubsub_96_AcknowledgeRequestIn",
        "AcknowledgeRequestOut": "_pubsub_97_AcknowledgeRequestOut",
        "ListTopicsResponseIn": "_pubsub_98_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsub_99_ListTopicsResponseOut",
        "SubscriptionIn": "_pubsub_100_SubscriptionIn",
        "SubscriptionOut": "_pubsub_101_SubscriptionOut",
        "PublishResponseIn": "_pubsub_102_PublishResponseIn",
        "PublishResponseOut": "_pubsub_103_PublishResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["SeekResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekResponseIn"]
    )
    types["SeekResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekResponseOut"])
    types["CommitSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["CommitSchemaRequestIn"])
    types["CommitSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitSchemaRequestOut"])
    types["PublishRequestIn"] = t.struct(
        {"messages": t.array(t.proxy(renames["PubsubMessageIn"]))}
    ).named(renames["PublishRequestIn"])
    types["PublishRequestOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["PubsubMessageOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["TopicIn"] = t.struct(
        {
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyIn"]
            ).optional(),
            "messageRetentionDuration": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "schemaSettings": t.proxy(renames["SchemaSettingsIn"]).optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "messageStoragePolicy": t.proxy(
                renames["MessageStoragePolicyOut"]
            ).optional(),
            "messageRetentionDuration": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "kmsKeyName": t.string().optional(),
            "name": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "schemaSettings": t.proxy(renames["SchemaSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["SchemaSettingsIn"] = t.struct(
        {
            "lastRevisionId": t.string().optional(),
            "firstRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
            "schema": t.string(),
        }
    ).named(renames["SchemaSettingsIn"])
    types["SchemaSettingsOut"] = t.struct(
        {
            "lastRevisionId": t.string().optional(),
            "firstRevisionId": t.string().optional(),
            "encoding": t.string().optional(),
            "schema": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaSettingsOut"])
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
    types["TextConfigIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextConfigIn"]
    )
    types["TextConfigOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextConfigOut"])
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
    types["ExpirationPolicyIn"] = t.struct({"ttl": t.string().optional()}).named(
        renames["ExpirationPolicyIn"]
    )
    types["ExpirationPolicyOut"] = t.struct(
        {
            "ttl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExpirationPolicyOut"])
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
    types["ModifyPushConfigRequestIn"] = t.struct(
        {"pushConfig": t.proxy(renames["PushConfigIn"])}
    ).named(renames["ModifyPushConfigRequestIn"])
    types["ModifyPushConfigRequestOut"] = t.struct(
        {
            "pushConfig": t.proxy(renames["PushConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModifyPushConfigRequestOut"])
    types["CloudStorageConfigIn"] = t.struct(
        {
            "avroConfig": t.proxy(renames["AvroConfigIn"]).optional(),
            "maxBytes": t.string().optional(),
            "filenameSuffix": t.string().optional(),
            "maxDuration": t.string().optional(),
            "bucket": t.string(),
            "filenamePrefix": t.string().optional(),
            "textConfig": t.proxy(renames["TextConfigIn"]).optional(),
        }
    ).named(renames["CloudStorageConfigIn"])
    types["CloudStorageConfigOut"] = t.struct(
        {
            "state": t.string().optional(),
            "avroConfig": t.proxy(renames["AvroConfigOut"]).optional(),
            "maxBytes": t.string().optional(),
            "filenameSuffix": t.string().optional(),
            "maxDuration": t.string().optional(),
            "bucket": t.string(),
            "filenamePrefix": t.string().optional(),
            "textConfig": t.proxy(renames["TextConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudStorageConfigOut"])
    types["BigQueryConfigIn"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "dropUnknownFields": t.boolean().optional(),
            "table": t.string().optional(),
            "useTopicSchema": t.boolean().optional(),
        }
    ).named(renames["BigQueryConfigIn"])
    types["BigQueryConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "dropUnknownFields": t.boolean().optional(),
            "table": t.string().optional(),
            "state": t.string().optional(),
            "useTopicSchema": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BigQueryConfigOut"])
    types["DetachSubscriptionResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DetachSubscriptionResponseIn"])
    types["DetachSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DetachSubscriptionResponseOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["PubsubMessageIn"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "messageId": t.string().optional(),
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["PubsubMessageIn"])
    types["PubsubMessageOut"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "messageId": t.string().optional(),
            "orderingKey": t.string().optional(),
            "attributes": t.struct({"_": t.string().optional()}).optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubsubMessageOut"])
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
    types["ValidateMessageResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateMessageResponseIn"]
    )
    types["ValidateMessageResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateMessageResponseOut"])
    types["AvroConfigIn"] = t.struct({"writeMetadata": t.boolean().optional()}).named(
        renames["AvroConfigIn"]
    )
    types["AvroConfigOut"] = t.struct(
        {
            "writeMetadata": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvroConfigOut"])
    types["ValidateSchemaResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ValidateSchemaResponseIn"]
    )
    types["ValidateSchemaResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ValidateSchemaResponseOut"])
    types["MessageStoragePolicyIn"] = t.struct(
        {"allowedPersistenceRegions": t.array(t.string()).optional()}
    ).named(renames["MessageStoragePolicyIn"])
    types["MessageStoragePolicyOut"] = t.struct(
        {
            "allowedPersistenceRegions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageStoragePolicyOut"])
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
    types["RollbackSchemaRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackSchemaRequestIn"]
    )
    types["RollbackSchemaRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackSchemaRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
            "type": t.string().optional(),
            "definition": t.string().optional(),
            "name": t.string(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchemaOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ValidateMessageRequestIn"] = t.struct(
        {
            "encoding": t.string().optional(),
            "name": t.string().optional(),
            "message": t.string().optional(),
            "schema": t.proxy(renames["SchemaIn"]).optional(),
        }
    ).named(renames["ValidateMessageRequestIn"])
    types["ValidateMessageRequestOut"] = t.struct(
        {
            "encoding": t.string().optional(),
            "name": t.string().optional(),
            "message": t.string().optional(),
            "schema": t.proxy(renames["SchemaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateMessageRequestOut"])
    types["ValidateSchemaRequestIn"] = t.struct(
        {"schema": t.proxy(renames["SchemaIn"])}
    ).named(renames["ValidateSchemaRequestIn"])
    types["ValidateSchemaRequestOut"] = t.struct(
        {
            "schema": t.proxy(renames["SchemaOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateSchemaRequestOut"])
    types["AcknowledgeRequestIn"] = t.struct({"ackIds": t.array(t.string())}).named(
        renames["AcknowledgeRequestIn"]
    )
    types["AcknowledgeRequestOut"] = t.struct(
        {
            "ackIds": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AcknowledgeRequestOut"])
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
    types["SubscriptionIn"] = t.struct(
        {
            "expirationPolicy": t.proxy(renames["ExpirationPolicyIn"]).optional(),
            "topic": t.string(),
            "messageRetentionDuration": t.string().optional(),
            "detached": t.boolean().optional(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigIn"]).optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigIn"]).optional(),
            "filter": t.string().optional(),
            "name": t.string(),
            "enableMessageOrdering": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retainAckedMessages": t.boolean().optional(),
            "pushConfig": t.proxy(renames["PushConfigIn"]).optional(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyIn"]).optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyIn"]).optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "expirationPolicy": t.proxy(renames["ExpirationPolicyOut"]).optional(),
            "state": t.string().optional(),
            "topic": t.string(),
            "messageRetentionDuration": t.string().optional(),
            "detached": t.boolean().optional(),
            "enableExactlyOnceDelivery": t.boolean().optional(),
            "topicMessageRetentionDuration": t.string().optional(),
            "bigqueryConfig": t.proxy(renames["BigQueryConfigOut"]).optional(),
            "ackDeadlineSeconds": t.integer().optional(),
            "cloudStorageConfig": t.proxy(renames["CloudStorageConfigOut"]).optional(),
            "filter": t.string().optional(),
            "name": t.string(),
            "enableMessageOrdering": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "retainAckedMessages": t.boolean().optional(),
            "pushConfig": t.proxy(renames["PushConfigOut"]).optional(),
            "deadLetterPolicy": t.proxy(renames["DeadLetterPolicyOut"]).optional(),
            "retryPolicy": t.proxy(renames["RetryPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["PublishResponseIn"] = t.struct(
        {"messageIds": t.array(t.string()).optional()}
    ).named(renames["PublishResponseIn"])
    types["PublishResponseOut"] = t.struct(
        {
            "messageIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishResponseOut"])

    functions = {}
    functions["projectsTopicsGetIamPolicy"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsPublish"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsCreate"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsGet"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsPatch"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSetIamPolicy"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsList"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsTestIamPermissions"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsDelete"] = pubsub.delete(
        "v1/{topic}",
        t.struct({"topic": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTopicsSubscriptionsList"] = pubsub.get(
        "v1/{topic}/subscriptions",
        t.struct(
            {
                "topic": t.string(),
                "pageToken": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "topic": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSnapshotsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsAcknowledge"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsDelete"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsSetIamPolicy"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsPull"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsModifyPushConfig"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsGet"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsList"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsModifyAckDeadline"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsDetach"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsCreate"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsTestIamPermissions"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsGetIamPolicy"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsPatch"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubscriptionsSeek"] = pubsub.post(
        "v1/{subscription}:seek",
        t.struct(
            {
                "subscription": t.string(),
                "snapshot": t.string().optional(),
                "time": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SeekResponseOut"]),
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
    functions["projectsSchemasGet"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasTestIamPermissions"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasRollback"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDelete"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCommit"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidateMessage"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasListRevisions"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasSetIamPolicy"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasDeleteRevision"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasCreate"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasGetIamPolicy"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasValidate"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSchemasList"] = pubsub.get(
        "v1/{parent}/schemas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "view": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSchemasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="pubsub", renames=renames, types=Box(types), functions=Box(functions)
    )
