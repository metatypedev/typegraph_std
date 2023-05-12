from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_pubsublite() -> Import:
    pubsublite = HTTPRuntime("https://pubsublite.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsublite_1_ErrorResponse",
        "ExportConfigIn": "_pubsublite_2_ExportConfigIn",
        "ExportConfigOut": "_pubsublite_3_ExportConfigOut",
        "SubscriptionIn": "_pubsublite_4_SubscriptionIn",
        "SubscriptionOut": "_pubsublite_5_SubscriptionOut",
        "ComputeTimeCursorResponseIn": "_pubsublite_6_ComputeTimeCursorResponseIn",
        "ComputeTimeCursorResponseOut": "_pubsublite_7_ComputeTimeCursorResponseOut",
        "ReservationConfigIn": "_pubsublite_8_ReservationConfigIn",
        "ReservationConfigOut": "_pubsublite_9_ReservationConfigOut",
        "ComputeHeadCursorRequestIn": "_pubsublite_10_ComputeHeadCursorRequestIn",
        "ComputeHeadCursorRequestOut": "_pubsublite_11_ComputeHeadCursorRequestOut",
        "ComputeHeadCursorResponseIn": "_pubsublite_12_ComputeHeadCursorResponseIn",
        "ComputeHeadCursorResponseOut": "_pubsublite_13_ComputeHeadCursorResponseOut",
        "OperationMetadataIn": "_pubsublite_14_OperationMetadataIn",
        "OperationMetadataOut": "_pubsublite_15_OperationMetadataOut",
        "ComputeTimeCursorRequestIn": "_pubsublite_16_ComputeTimeCursorRequestIn",
        "ComputeTimeCursorRequestOut": "_pubsublite_17_ComputeTimeCursorRequestOut",
        "ListSubscriptionsResponseIn": "_pubsublite_18_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsublite_19_ListSubscriptionsResponseOut",
        "CursorIn": "_pubsublite_20_CursorIn",
        "CursorOut": "_pubsublite_21_CursorOut",
        "ComputeMessageStatsRequestIn": "_pubsublite_22_ComputeMessageStatsRequestIn",
        "ComputeMessageStatsRequestOut": "_pubsublite_23_ComputeMessageStatsRequestOut",
        "ComputeMessageStatsResponseIn": "_pubsublite_24_ComputeMessageStatsResponseIn",
        "ComputeMessageStatsResponseOut": "_pubsublite_25_ComputeMessageStatsResponseOut",
        "SeekSubscriptionRequestIn": "_pubsublite_26_SeekSubscriptionRequestIn",
        "SeekSubscriptionRequestOut": "_pubsublite_27_SeekSubscriptionRequestOut",
        "ListTopicSubscriptionsResponseIn": "_pubsublite_28_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsublite_29_ListTopicSubscriptionsResponseOut",
        "OperationIn": "_pubsublite_30_OperationIn",
        "OperationOut": "_pubsublite_31_OperationOut",
        "ListTopicsResponseIn": "_pubsublite_32_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsublite_33_ListTopicsResponseOut",
        "PubSubConfigIn": "_pubsublite_34_PubSubConfigIn",
        "PubSubConfigOut": "_pubsublite_35_PubSubConfigOut",
        "RetentionConfigIn": "_pubsublite_36_RetentionConfigIn",
        "RetentionConfigOut": "_pubsublite_37_RetentionConfigOut",
        "TopicPartitionsIn": "_pubsublite_38_TopicPartitionsIn",
        "TopicPartitionsOut": "_pubsublite_39_TopicPartitionsOut",
        "TimeTargetIn": "_pubsublite_40_TimeTargetIn",
        "TimeTargetOut": "_pubsublite_41_TimeTargetOut",
        "CommitCursorRequestIn": "_pubsublite_42_CommitCursorRequestIn",
        "CommitCursorRequestOut": "_pubsublite_43_CommitCursorRequestOut",
        "CapacityIn": "_pubsublite_44_CapacityIn",
        "CapacityOut": "_pubsublite_45_CapacityOut",
        "DeliveryConfigIn": "_pubsublite_46_DeliveryConfigIn",
        "DeliveryConfigOut": "_pubsublite_47_DeliveryConfigOut",
        "PartitionCursorIn": "_pubsublite_48_PartitionCursorIn",
        "PartitionCursorOut": "_pubsublite_49_PartitionCursorOut",
        "ListReservationsResponseIn": "_pubsublite_50_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_pubsublite_51_ListReservationsResponseOut",
        "ReservationIn": "_pubsublite_52_ReservationIn",
        "ReservationOut": "_pubsublite_53_ReservationOut",
        "ListPartitionCursorsResponseIn": "_pubsublite_54_ListPartitionCursorsResponseIn",
        "ListPartitionCursorsResponseOut": "_pubsublite_55_ListPartitionCursorsResponseOut",
        "EmptyIn": "_pubsublite_56_EmptyIn",
        "EmptyOut": "_pubsublite_57_EmptyOut",
        "ListOperationsResponseIn": "_pubsublite_58_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_pubsublite_59_ListOperationsResponseOut",
        "StatusIn": "_pubsublite_60_StatusIn",
        "StatusOut": "_pubsublite_61_StatusOut",
        "CancelOperationRequestIn": "_pubsublite_62_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_pubsublite_63_CancelOperationRequestOut",
        "PartitionConfigIn": "_pubsublite_64_PartitionConfigIn",
        "PartitionConfigOut": "_pubsublite_65_PartitionConfigOut",
        "ListReservationTopicsResponseIn": "_pubsublite_66_ListReservationTopicsResponseIn",
        "ListReservationTopicsResponseOut": "_pubsublite_67_ListReservationTopicsResponseOut",
        "CommitCursorResponseIn": "_pubsublite_68_CommitCursorResponseIn",
        "CommitCursorResponseOut": "_pubsublite_69_CommitCursorResponseOut",
        "TopicIn": "_pubsublite_70_TopicIn",
        "TopicOut": "_pubsublite_71_TopicOut",
        "SeekSubscriptionResponseIn": "_pubsublite_72_SeekSubscriptionResponseIn",
        "SeekSubscriptionResponseOut": "_pubsublite_73_SeekSubscriptionResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExportConfigIn"] = t.struct(
        {
            "desiredState": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubSubConfigIn"]).optional(),
            "deadLetterTopic": t.string().optional(),
        }
    ).named(renames["ExportConfigIn"])
    types["ExportConfigOut"] = t.struct(
        {
            "desiredState": t.string().optional(),
            "currentState": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubSubConfigOut"]).optional(),
            "deadLetterTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportConfigOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigIn"]).optional(),
            "topic": t.string().optional(),
            "exportConfig": t.proxy(renames["ExportConfigIn"]).optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigOut"]).optional(),
            "topic": t.string().optional(),
            "exportConfig": t.proxy(renames["ExportConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
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
    types["ComputeHeadCursorRequestIn"] = t.struct({"partition": t.string()}).named(
        renames["ComputeHeadCursorRequestIn"]
    )
    types["ComputeHeadCursorRequestOut"] = t.struct(
        {"partition": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ComputeHeadCursorRequestOut"])
    types["ComputeHeadCursorResponseIn"] = t.struct(
        {"headCursor": t.proxy(renames["CursorIn"]).optional()}
    ).named(renames["ComputeHeadCursorResponseIn"])
    types["ComputeHeadCursorResponseOut"] = t.struct(
        {
            "headCursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeHeadCursorResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ComputeTimeCursorRequestIn"] = t.struct(
        {"partition": t.string(), "target": t.proxy(renames["TimeTargetIn"])}
    ).named(renames["ComputeTimeCursorRequestIn"])
    types["ComputeTimeCursorRequestOut"] = t.struct(
        {
            "partition": t.string(),
            "target": t.proxy(renames["TimeTargetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeTimeCursorRequestOut"])
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
    types["CursorIn"] = t.struct({"offset": t.string().optional()}).named(
        renames["CursorIn"]
    )
    types["CursorOut"] = t.struct(
        {
            "offset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CursorOut"])
    types["ComputeMessageStatsRequestIn"] = t.struct(
        {
            "startCursor": t.proxy(renames["CursorIn"]).optional(),
            "partition": t.string(),
            "endCursor": t.proxy(renames["CursorIn"]).optional(),
        }
    ).named(renames["ComputeMessageStatsRequestIn"])
    types["ComputeMessageStatsRequestOut"] = t.struct(
        {
            "startCursor": t.proxy(renames["CursorOut"]).optional(),
            "partition": t.string(),
            "endCursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeMessageStatsRequestOut"])
    types["ComputeMessageStatsResponseIn"] = t.struct(
        {
            "messageCount": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
            "messageBytes": t.string().optional(),
            "minimumEventTime": t.string().optional(),
        }
    ).named(renames["ComputeMessageStatsResponseIn"])
    types["ComputeMessageStatsResponseOut"] = t.struct(
        {
            "messageCount": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
            "messageBytes": t.string().optional(),
            "minimumEventTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeMessageStatsResponseOut"])
    types["SeekSubscriptionRequestIn"] = t.struct(
        {
            "namedTarget": t.string().optional(),
            "timeTarget": t.proxy(renames["TimeTargetIn"]).optional(),
        }
    ).named(renames["SeekSubscriptionRequestIn"])
    types["SeekSubscriptionRequestOut"] = t.struct(
        {
            "namedTarget": t.string().optional(),
            "timeTarget": t.proxy(renames["TimeTargetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SeekSubscriptionRequestOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["PubSubConfigIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubSubConfigIn"]
    )
    types["PubSubConfigOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubConfigOut"])
    types["RetentionConfigIn"] = t.struct(
        {"period": t.string().optional(), "perPartitionBytes": t.string().optional()}
    ).named(renames["RetentionConfigIn"])
    types["RetentionConfigOut"] = t.struct(
        {
            "period": t.string().optional(),
            "perPartitionBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetentionConfigOut"])
    types["TopicPartitionsIn"] = t.struct(
        {"partitionCount": t.string().optional()}
    ).named(renames["TopicPartitionsIn"])
    types["TopicPartitionsOut"] = t.struct(
        {
            "partitionCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicPartitionsOut"])
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
    types["CommitCursorRequestIn"] = t.struct(
        {
            "partition": t.string().optional(),
            "cursor": t.proxy(renames["CursorIn"]).optional(),
        }
    ).named(renames["CommitCursorRequestIn"])
    types["CommitCursorRequestOut"] = t.struct(
        {
            "partition": t.string().optional(),
            "cursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitCursorRequestOut"])
    types["CapacityIn"] = t.struct(
        {
            "publishMibPerSec": t.integer().optional(),
            "subscribeMibPerSec": t.integer().optional(),
        }
    ).named(renames["CapacityIn"])
    types["CapacityOut"] = t.struct(
        {
            "publishMibPerSec": t.integer().optional(),
            "subscribeMibPerSec": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityOut"])
    types["DeliveryConfigIn"] = t.struct(
        {"deliveryRequirement": t.string().optional()}
    ).named(renames["DeliveryConfigIn"])
    types["DeliveryConfigOut"] = t.struct(
        {
            "deliveryRequirement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryConfigOut"])
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
    types["ReservationIn"] = t.struct(
        {"throughputCapacity": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ReservationIn"])
    types["ReservationOut"] = t.struct(
        {
            "throughputCapacity": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationOut"])
    types["ListPartitionCursorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "partitionCursors": t.array(
                t.proxy(renames["PartitionCursorIn"])
            ).optional(),
        }
    ).named(renames["ListPartitionCursorsResponseIn"])
    types["ListPartitionCursorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "partitionCursors": t.array(
                t.proxy(renames["PartitionCursorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPartitionCursorsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["PartitionConfigIn"] = t.struct(
        {
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
            "scale": t.integer().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["PartitionConfigIn"])
    types["PartitionConfigOut"] = t.struct(
        {
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "scale": t.integer().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionConfigOut"])
    types["ListReservationTopicsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "topics": t.array(t.string()).optional(),
        }
    ).named(renames["ListReservationTopicsResponseIn"])
    types["ListReservationTopicsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "topics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReservationTopicsResponseOut"])
    types["CommitCursorResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CommitCursorResponseIn"]
    )
    types["CommitCursorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommitCursorResponseOut"])
    types["TopicIn"] = t.struct(
        {
            "retentionConfig": t.proxy(renames["RetentionConfigIn"]).optional(),
            "name": t.string().optional(),
            "partitionConfig": t.proxy(renames["PartitionConfigIn"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigIn"]).optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "retentionConfig": t.proxy(renames["RetentionConfigOut"]).optional(),
            "name": t.string().optional(),
            "partitionConfig": t.proxy(renames["PartitionConfigOut"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["SeekSubscriptionResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekSubscriptionResponseIn"]
    )
    types["SeekSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekSubscriptionResponseOut"])

    functions = {}
    functions["topicStatsProjectsLocationsTopicsComputeTimeCursor"] = pubsublite.post(
        "v1/topicStats/{topic}:computeMessageStats",
        t.struct(
            {
                "topic": t.string(),
                "startCursor": t.proxy(renames["CursorIn"]).optional(),
                "partition": t.string(),
                "endCursor": t.proxy(renames["CursorIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeMessageStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["topicStatsProjectsLocationsTopicsComputeHeadCursor"] = pubsublite.post(
        "v1/topicStats/{topic}:computeMessageStats",
        t.struct(
            {
                "topic": t.string(),
                "startCursor": t.proxy(renames["CursorIn"]).optional(),
                "partition": t.string(),
                "endCursor": t.proxy(renames["CursorIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeMessageStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["topicStatsProjectsLocationsTopicsComputeMessageStats"] = pubsublite.post(
        "v1/topicStats/{topic}:computeMessageStats",
        t.struct(
            {
                "topic": t.string(),
                "startCursor": t.proxy(renames["CursorIn"]).optional(),
                "partition": t.string(),
                "endCursor": t.proxy(renames["CursorIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeMessageStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsCreate"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsSeek"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsList"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsGet"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsPatch"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsDelete"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsList"] = pubsublite.post(
        "v1/admin/{name}:cancel",
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
    functions["adminProjectsLocationsOperationsGet"] = pubsublite.post(
        "v1/admin/{name}:cancel",
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
    functions["adminProjectsLocationsOperationsDelete"] = pubsublite.post(
        "v1/admin/{name}:cancel",
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
    functions["adminProjectsLocationsOperationsCancel"] = pubsublite.post(
        "v1/admin/{name}:cancel",
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
    functions["adminProjectsLocationsReservationsCreate"] = pubsublite.delete(
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
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReservationTopicsResponseOut"]),
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
    functions["adminProjectsLocationsTopicsPatch"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["adminProjectsLocationsTopicsGetPartitions"] = pubsublite.delete(
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
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["cursorProjectsLocationsSubscriptionsCommitCursor"] = pubsublite.post(
        "v1/cursor/{subscription}:commitCursor",
        t.struct(
            {
                "subscription": t.string().optional(),
                "partition": t.string().optional(),
                "cursor": t.proxy(renames["CursorIn"]).optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
