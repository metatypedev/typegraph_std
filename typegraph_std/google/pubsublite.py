from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_pubsublite():
    pubsublite = HTTPRuntime("https://pubsublite.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsublite_1_ErrorResponse",
        "TopicIn": "_pubsublite_2_TopicIn",
        "TopicOut": "_pubsublite_3_TopicOut",
        "CommitCursorRequestIn": "_pubsublite_4_CommitCursorRequestIn",
        "CommitCursorRequestOut": "_pubsublite_5_CommitCursorRequestOut",
        "PubSubConfigIn": "_pubsublite_6_PubSubConfigIn",
        "PubSubConfigOut": "_pubsublite_7_PubSubConfigOut",
        "OperationIn": "_pubsublite_8_OperationIn",
        "OperationOut": "_pubsublite_9_OperationOut",
        "ComputeMessageStatsRequestIn": "_pubsublite_10_ComputeMessageStatsRequestIn",
        "ComputeMessageStatsRequestOut": "_pubsublite_11_ComputeMessageStatsRequestOut",
        "ComputeMessageStatsResponseIn": "_pubsublite_12_ComputeMessageStatsResponseIn",
        "ComputeMessageStatsResponseOut": "_pubsublite_13_ComputeMessageStatsResponseOut",
        "PartitionCursorIn": "_pubsublite_14_PartitionCursorIn",
        "PartitionCursorOut": "_pubsublite_15_PartitionCursorOut",
        "ListSubscriptionsResponseIn": "_pubsublite_16_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsublite_17_ListSubscriptionsResponseOut",
        "SeekSubscriptionRequestIn": "_pubsublite_18_SeekSubscriptionRequestIn",
        "SeekSubscriptionRequestOut": "_pubsublite_19_SeekSubscriptionRequestOut",
        "ComputeTimeCursorRequestIn": "_pubsublite_20_ComputeTimeCursorRequestIn",
        "ComputeTimeCursorRequestOut": "_pubsublite_21_ComputeTimeCursorRequestOut",
        "PartitionConfigIn": "_pubsublite_22_PartitionConfigIn",
        "PartitionConfigOut": "_pubsublite_23_PartitionConfigOut",
        "ListReservationTopicsResponseIn": "_pubsublite_24_ListReservationTopicsResponseIn",
        "ListReservationTopicsResponseOut": "_pubsublite_25_ListReservationTopicsResponseOut",
        "TopicPartitionsIn": "_pubsublite_26_TopicPartitionsIn",
        "TopicPartitionsOut": "_pubsublite_27_TopicPartitionsOut",
        "ComputeTimeCursorResponseIn": "_pubsublite_28_ComputeTimeCursorResponseIn",
        "ComputeTimeCursorResponseOut": "_pubsublite_29_ComputeTimeCursorResponseOut",
        "ReservationConfigIn": "_pubsublite_30_ReservationConfigIn",
        "ReservationConfigOut": "_pubsublite_31_ReservationConfigOut",
        "OperationMetadataIn": "_pubsublite_32_OperationMetadataIn",
        "OperationMetadataOut": "_pubsublite_33_OperationMetadataOut",
        "EmptyIn": "_pubsublite_34_EmptyIn",
        "EmptyOut": "_pubsublite_35_EmptyOut",
        "ListTopicSubscriptionsResponseIn": "_pubsublite_36_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsublite_37_ListTopicSubscriptionsResponseOut",
        "TimeTargetIn": "_pubsublite_38_TimeTargetIn",
        "TimeTargetOut": "_pubsublite_39_TimeTargetOut",
        "ReservationIn": "_pubsublite_40_ReservationIn",
        "ReservationOut": "_pubsublite_41_ReservationOut",
        "CursorIn": "_pubsublite_42_CursorIn",
        "CursorOut": "_pubsublite_43_CursorOut",
        "StatusIn": "_pubsublite_44_StatusIn",
        "StatusOut": "_pubsublite_45_StatusOut",
        "ListPartitionCursorsResponseIn": "_pubsublite_46_ListPartitionCursorsResponseIn",
        "ListPartitionCursorsResponseOut": "_pubsublite_47_ListPartitionCursorsResponseOut",
        "ListOperationsResponseIn": "_pubsublite_48_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_pubsublite_49_ListOperationsResponseOut",
        "SubscriptionIn": "_pubsublite_50_SubscriptionIn",
        "SubscriptionOut": "_pubsublite_51_SubscriptionOut",
        "SeekSubscriptionResponseIn": "_pubsublite_52_SeekSubscriptionResponseIn",
        "SeekSubscriptionResponseOut": "_pubsublite_53_SeekSubscriptionResponseOut",
        "DeliveryConfigIn": "_pubsublite_54_DeliveryConfigIn",
        "DeliveryConfigOut": "_pubsublite_55_DeliveryConfigOut",
        "ComputeHeadCursorResponseIn": "_pubsublite_56_ComputeHeadCursorResponseIn",
        "ComputeHeadCursorResponseOut": "_pubsublite_57_ComputeHeadCursorResponseOut",
        "CapacityIn": "_pubsublite_58_CapacityIn",
        "CapacityOut": "_pubsublite_59_CapacityOut",
        "ListTopicsResponseIn": "_pubsublite_60_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsublite_61_ListTopicsResponseOut",
        "CommitCursorResponseIn": "_pubsublite_62_CommitCursorResponseIn",
        "CommitCursorResponseOut": "_pubsublite_63_CommitCursorResponseOut",
        "CancelOperationRequestIn": "_pubsublite_64_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_pubsublite_65_CancelOperationRequestOut",
        "ComputeHeadCursorRequestIn": "_pubsublite_66_ComputeHeadCursorRequestIn",
        "ComputeHeadCursorRequestOut": "_pubsublite_67_ComputeHeadCursorRequestOut",
        "RetentionConfigIn": "_pubsublite_68_RetentionConfigIn",
        "RetentionConfigOut": "_pubsublite_69_RetentionConfigOut",
        "ListReservationsResponseIn": "_pubsublite_70_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_pubsublite_71_ListReservationsResponseOut",
        "ExportConfigIn": "_pubsublite_72_ExportConfigIn",
        "ExportConfigOut": "_pubsublite_73_ExportConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TopicIn"] = t.struct(
        {
            "partitionConfig": t.proxy(renames["PartitionConfigIn"]).optional(),
            "retentionConfig": t.proxy(renames["RetentionConfigIn"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "partitionConfig": t.proxy(renames["PartitionConfigOut"]).optional(),
            "retentionConfig": t.proxy(renames["RetentionConfigOut"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["CommitCursorRequestIn"] = t.struct(
        {
            "cursor": t.proxy(renames["CursorIn"]).optional(),
            "partition": t.string().optional(),
        }
    ).named(renames["CommitCursorRequestIn"])
    types["CommitCursorRequestOut"] = t.struct(
        {
            "cursor": t.proxy(renames["CursorOut"]).optional(),
            "partition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitCursorRequestOut"])
    types["PubSubConfigIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubSubConfigIn"]
    )
    types["PubSubConfigOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubConfigOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ComputeMessageStatsRequestIn"] = t.struct(
        {
            "partition": t.string(),
            "endCursor": t.proxy(renames["CursorIn"]).optional(),
            "startCursor": t.proxy(renames["CursorIn"]).optional(),
        }
    ).named(renames["ComputeMessageStatsRequestIn"])
    types["ComputeMessageStatsRequestOut"] = t.struct(
        {
            "partition": t.string(),
            "endCursor": t.proxy(renames["CursorOut"]).optional(),
            "startCursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeMessageStatsRequestOut"])
    types["ComputeMessageStatsResponseIn"] = t.struct(
        {
            "messageBytes": t.string().optional(),
            "messageCount": t.string().optional(),
            "minimumEventTime": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
        }
    ).named(renames["ComputeMessageStatsResponseIn"])
    types["ComputeMessageStatsResponseOut"] = t.struct(
        {
            "messageBytes": t.string().optional(),
            "messageCount": t.string().optional(),
            "minimumEventTime": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeMessageStatsResponseOut"])
    types["PartitionCursorIn"] = t.struct(
        {
            "cursor": t.proxy(renames["CursorIn"]).optional(),
            "partition": t.string().optional(),
        }
    ).named(renames["PartitionCursorIn"])
    types["PartitionCursorOut"] = t.struct(
        {
            "cursor": t.proxy(renames["CursorOut"]).optional(),
            "partition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionCursorOut"])
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
    types["SeekSubscriptionRequestIn"] = t.struct(
        {
            "timeTarget": t.proxy(renames["TimeTargetIn"]).optional(),
            "namedTarget": t.string().optional(),
        }
    ).named(renames["SeekSubscriptionRequestIn"])
    types["SeekSubscriptionRequestOut"] = t.struct(
        {
            "timeTarget": t.proxy(renames["TimeTargetOut"]).optional(),
            "namedTarget": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeekSubscriptionRequestOut"])
    types["ComputeTimeCursorRequestIn"] = t.struct(
        {"target": t.proxy(renames["TimeTargetIn"]), "partition": t.string()}
    ).named(renames["ComputeTimeCursorRequestIn"])
    types["ComputeTimeCursorRequestOut"] = t.struct(
        {
            "target": t.proxy(renames["TimeTargetOut"]),
            "partition": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeTimeCursorRequestOut"])
    types["PartitionConfigIn"] = t.struct(
        {
            "scale": t.integer().optional(),
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
            "count": t.string().optional(),
        }
    ).named(renames["PartitionConfigIn"])
    types["PartitionConfigOut"] = t.struct(
        {
            "scale": t.integer().optional(),
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionConfigOut"])
    types["ListReservationTopicsResponseIn"] = t.struct(
        {
            "topics": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReservationTopicsResponseIn"])
    types["ListReservationTopicsResponseOut"] = t.struct(
        {
            "topics": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReservationTopicsResponseOut"])
    types["TopicPartitionsIn"] = t.struct(
        {"partitionCount": t.string().optional()}
    ).named(renames["TopicPartitionsIn"])
    types["TopicPartitionsOut"] = t.struct(
        {
            "partitionCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicPartitionsOut"])
    types["ComputeTimeCursorResponseIn"] = t.struct(
        {"cursor": t.proxy(renames["CursorIn"]).optional()}
    ).named(renames["ComputeTimeCursorResponseIn"])
    types["ComputeTimeCursorResponseOut"] = t.struct(
        {
            "cursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeTimeCursorResponseOut"])
    types["ReservationConfigIn"] = t.struct(
        {"throughputReservation": t.string().optional()}
    ).named(renames["ReservationConfigIn"])
    types["ReservationConfigOut"] = t.struct(
        {
            "throughputReservation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationConfigOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["TimeTargetIn"] = t.struct(
        {"publishTime": t.string().optional(), "eventTime": t.string().optional()}
    ).named(renames["TimeTargetIn"])
    types["TimeTargetOut"] = t.struct(
        {
            "publishTime": t.string().optional(),
            "eventTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeTargetOut"])
    types["ReservationIn"] = t.struct(
        {"name": t.string().optional(), "throughputCapacity": t.string().optional()}
    ).named(renames["ReservationIn"])
    types["ReservationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "throughputCapacity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationOut"])
    types["CursorIn"] = t.struct({"offset": t.string().optional()}).named(
        renames["CursorIn"]
    )
    types["CursorOut"] = t.struct(
        {
            "offset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CursorOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ListPartitionCursorsResponseIn"] = t.struct(
        {
            "partitionCursors": t.array(
                t.proxy(renames["PartitionCursorIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPartitionCursorsResponseIn"])
    types["ListPartitionCursorsResponseOut"] = t.struct(
        {
            "partitionCursors": t.array(
                t.proxy(renames["PartitionCursorOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPartitionCursorsResponseOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "exportConfig": t.proxy(renames["ExportConfigIn"]).optional(),
            "name": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigIn"]).optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "exportConfig": t.proxy(renames["ExportConfigOut"]).optional(),
            "name": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigOut"]).optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
    types["SeekSubscriptionResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekSubscriptionResponseIn"]
    )
    types["SeekSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekSubscriptionResponseOut"])
    types["DeliveryConfigIn"] = t.struct(
        {"deliveryRequirement": t.string().optional()}
    ).named(renames["DeliveryConfigIn"])
    types["DeliveryConfigOut"] = t.struct(
        {
            "deliveryRequirement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryConfigOut"])
    types["ComputeHeadCursorResponseIn"] = t.struct(
        {"headCursor": t.proxy(renames["CursorIn"]).optional()}
    ).named(renames["ComputeHeadCursorResponseIn"])
    types["ComputeHeadCursorResponseOut"] = t.struct(
        {
            "headCursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeHeadCursorResponseOut"])
    types["CapacityIn"] = t.struct(
        {
            "subscribeMibPerSec": t.integer().optional(),
            "publishMibPerSec": t.integer().optional(),
        }
    ).named(renames["CapacityIn"])
    types["CapacityOut"] = t.struct(
        {
            "subscribeMibPerSec": t.integer().optional(),
            "publishMibPerSec": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityOut"])
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
    types["CommitCursorResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CommitCursorResponseIn"]
    )
    types["CommitCursorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommitCursorResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ComputeHeadCursorRequestIn"] = t.struct({"partition": t.string()}).named(
        renames["ComputeHeadCursorRequestIn"]
    )
    types["ComputeHeadCursorRequestOut"] = t.struct(
        {"partition": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ComputeHeadCursorRequestOut"])
    types["RetentionConfigIn"] = t.struct(
        {"perPartitionBytes": t.string().optional(), "period": t.string().optional()}
    ).named(renames["RetentionConfigIn"])
    types["RetentionConfigOut"] = t.struct(
        {
            "perPartitionBytes": t.string().optional(),
            "period": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetentionConfigOut"])
    types["ListReservationsResponseIn"] = t.struct(
        {
            "reservations": t.array(t.proxy(renames["ReservationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReservationsResponseIn"])
    types["ListReservationsResponseOut"] = t.struct(
        {
            "reservations": t.array(t.proxy(renames["ReservationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReservationsResponseOut"])
    types["ExportConfigIn"] = t.struct(
        {
            "desiredState": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubSubConfigIn"]).optional(),
            "deadLetterTopic": t.string().optional(),
        }
    ).named(renames["ExportConfigIn"])
    types["ExportConfigOut"] = t.struct(
        {
            "currentState": t.string().optional(),
            "desiredState": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubSubConfigOut"]).optional(),
            "deadLetterTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportConfigOut"])

    functions = {}
    functions["topicStatsProjectsLocationsTopicsComputeMessageStats"] = pubsublite.post(
        "v1/topicStats/{topic}:computeHeadCursor",
        t.struct(
            {
                "topic": t.string(),
                "partition": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeHeadCursorResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["topicStatsProjectsLocationsTopicsComputeTimeCursor"] = pubsublite.post(
        "v1/topicStats/{topic}:computeHeadCursor",
        t.struct(
            {
                "topic": t.string(),
                "partition": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeHeadCursorResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["topicStatsProjectsLocationsTopicsComputeHeadCursor"] = pubsublite.post(
        "v1/topicStats/{topic}:computeHeadCursor",
        t.struct(
            {
                "topic": t.string(),
                "partition": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeHeadCursorResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsList"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsCreate"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsGet"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsPatch"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsGetPartitions"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsDelete"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsSubscriptionsList"] = pubsublite.get(
        "v1/admin/{name}/subscriptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsCreate"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsPatch"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsGet"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsList"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsDelete"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsTopicsList"] = pubsublite.get(
        "v1/admin/{name}/topics",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReservationTopicsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsDelete"] = pubsublite.get(
        "v1/admin/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsGet"] = pubsublite.get(
        "v1/admin/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsCancel"] = pubsublite.get(
        "v1/admin/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsList"] = pubsublite.get(
        "v1/admin/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsSeek"] = pubsublite.get(
        "v1/admin/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsPatch"] = pubsublite.get(
        "v1/admin/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsCreate"] = pubsublite.get(
        "v1/admin/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsDelete"] = pubsublite.get(
        "v1/admin/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsGet"] = pubsublite.get(
        "v1/admin/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsList"] = pubsublite.get(
        "v1/admin/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cursorProjectsLocationsSubscriptionsCommitCursor"] = pubsublite.post(
        "v1/cursor/{subscription}:commitCursor",
        t.struct(
            {
                "subscription": t.string().optional(),
                "cursor": t.proxy(renames["CursorIn"]).optional(),
                "partition": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CommitCursorResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cursorProjectsLocationsSubscriptionsCursorsList"] = pubsublite.get(
        "v1/cursor/{parent}/cursors",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartitionCursorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="pubsublite",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
