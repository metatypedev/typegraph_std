from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_pubsublite() -> Import:
    pubsublite = HTTPRuntime("https://pubsublite.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsublite_1_ErrorResponse",
        "ListSubscriptionsResponseIn": "_pubsublite_2_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsublite_3_ListSubscriptionsResponseOut",
        "DeliveryConfigIn": "_pubsublite_4_DeliveryConfigIn",
        "DeliveryConfigOut": "_pubsublite_5_DeliveryConfigOut",
        "ReservationIn": "_pubsublite_6_ReservationIn",
        "ReservationOut": "_pubsublite_7_ReservationOut",
        "ComputeHeadCursorResponseIn": "_pubsublite_8_ComputeHeadCursorResponseIn",
        "ComputeHeadCursorResponseOut": "_pubsublite_9_ComputeHeadCursorResponseOut",
        "ListReservationTopicsResponseIn": "_pubsublite_10_ListReservationTopicsResponseIn",
        "ListReservationTopicsResponseOut": "_pubsublite_11_ListReservationTopicsResponseOut",
        "CancelOperationRequestIn": "_pubsublite_12_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_pubsublite_13_CancelOperationRequestOut",
        "SubscriptionIn": "_pubsublite_14_SubscriptionIn",
        "SubscriptionOut": "_pubsublite_15_SubscriptionOut",
        "ListTopicSubscriptionsResponseIn": "_pubsublite_16_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsublite_17_ListTopicSubscriptionsResponseOut",
        "ReservationConfigIn": "_pubsublite_18_ReservationConfigIn",
        "ReservationConfigOut": "_pubsublite_19_ReservationConfigOut",
        "ExportConfigIn": "_pubsublite_20_ExportConfigIn",
        "ExportConfigOut": "_pubsublite_21_ExportConfigOut",
        "ComputeMessageStatsRequestIn": "_pubsublite_22_ComputeMessageStatsRequestIn",
        "ComputeMessageStatsRequestOut": "_pubsublite_23_ComputeMessageStatsRequestOut",
        "CapacityIn": "_pubsublite_24_CapacityIn",
        "CapacityOut": "_pubsublite_25_CapacityOut",
        "SeekSubscriptionResponseIn": "_pubsublite_26_SeekSubscriptionResponseIn",
        "SeekSubscriptionResponseOut": "_pubsublite_27_SeekSubscriptionResponseOut",
        "StatusIn": "_pubsublite_28_StatusIn",
        "StatusOut": "_pubsublite_29_StatusOut",
        "TimeTargetIn": "_pubsublite_30_TimeTargetIn",
        "TimeTargetOut": "_pubsublite_31_TimeTargetOut",
        "ListPartitionCursorsResponseIn": "_pubsublite_32_ListPartitionCursorsResponseIn",
        "ListPartitionCursorsResponseOut": "_pubsublite_33_ListPartitionCursorsResponseOut",
        "OperationIn": "_pubsublite_34_OperationIn",
        "OperationOut": "_pubsublite_35_OperationOut",
        "PartitionCursorIn": "_pubsublite_36_PartitionCursorIn",
        "PartitionCursorOut": "_pubsublite_37_PartitionCursorOut",
        "ComputeTimeCursorResponseIn": "_pubsublite_38_ComputeTimeCursorResponseIn",
        "ComputeTimeCursorResponseOut": "_pubsublite_39_ComputeTimeCursorResponseOut",
        "PartitionConfigIn": "_pubsublite_40_PartitionConfigIn",
        "PartitionConfigOut": "_pubsublite_41_PartitionConfigOut",
        "ListReservationsResponseIn": "_pubsublite_42_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_pubsublite_43_ListReservationsResponseOut",
        "EmptyIn": "_pubsublite_44_EmptyIn",
        "EmptyOut": "_pubsublite_45_EmptyOut",
        "TopicPartitionsIn": "_pubsublite_46_TopicPartitionsIn",
        "TopicPartitionsOut": "_pubsublite_47_TopicPartitionsOut",
        "ComputeTimeCursorRequestIn": "_pubsublite_48_ComputeTimeCursorRequestIn",
        "ComputeTimeCursorRequestOut": "_pubsublite_49_ComputeTimeCursorRequestOut",
        "RetentionConfigIn": "_pubsublite_50_RetentionConfigIn",
        "RetentionConfigOut": "_pubsublite_51_RetentionConfigOut",
        "ListOperationsResponseIn": "_pubsublite_52_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_pubsublite_53_ListOperationsResponseOut",
        "ComputeMessageStatsResponseIn": "_pubsublite_54_ComputeMessageStatsResponseIn",
        "ComputeMessageStatsResponseOut": "_pubsublite_55_ComputeMessageStatsResponseOut",
        "ListTopicsResponseIn": "_pubsublite_56_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsublite_57_ListTopicsResponseOut",
        "CommitCursorRequestIn": "_pubsublite_58_CommitCursorRequestIn",
        "CommitCursorRequestOut": "_pubsublite_59_CommitCursorRequestOut",
        "OperationMetadataIn": "_pubsublite_60_OperationMetadataIn",
        "OperationMetadataOut": "_pubsublite_61_OperationMetadataOut",
        "CommitCursorResponseIn": "_pubsublite_62_CommitCursorResponseIn",
        "CommitCursorResponseOut": "_pubsublite_63_CommitCursorResponseOut",
        "ComputeHeadCursorRequestIn": "_pubsublite_64_ComputeHeadCursorRequestIn",
        "ComputeHeadCursorRequestOut": "_pubsublite_65_ComputeHeadCursorRequestOut",
        "PubSubConfigIn": "_pubsublite_66_PubSubConfigIn",
        "PubSubConfigOut": "_pubsublite_67_PubSubConfigOut",
        "TopicIn": "_pubsublite_68_TopicIn",
        "TopicOut": "_pubsublite_69_TopicOut",
        "CursorIn": "_pubsublite_70_CursorIn",
        "CursorOut": "_pubsublite_71_CursorOut",
        "SeekSubscriptionRequestIn": "_pubsublite_72_SeekSubscriptionRequestIn",
        "SeekSubscriptionRequestOut": "_pubsublite_73_SeekSubscriptionRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DeliveryConfigIn"] = t.struct(
        {"deliveryRequirement": t.string().optional()}
    ).named(renames["DeliveryConfigIn"])
    types["DeliveryConfigOut"] = t.struct(
        {
            "deliveryRequirement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryConfigOut"])
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
    types["ComputeHeadCursorResponseIn"] = t.struct(
        {"headCursor": t.proxy(renames["CursorIn"]).optional()}
    ).named(renames["ComputeHeadCursorResponseIn"])
    types["ComputeHeadCursorResponseOut"] = t.struct(
        {
            "headCursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeHeadCursorResponseOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["SubscriptionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "topic": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigIn"]).optional(),
            "exportConfig": t.proxy(renames["ExportConfigIn"]).optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "topic": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigOut"]).optional(),
            "exportConfig": t.proxy(renames["ExportConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
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
    types["ReservationConfigIn"] = t.struct(
        {"throughputReservation": t.string().optional()}
    ).named(renames["ReservationConfigIn"])
    types["ReservationConfigOut"] = t.struct(
        {
            "throughputReservation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationConfigOut"])
    types["ExportConfigIn"] = t.struct(
        {
            "pubsubConfig": t.proxy(renames["PubSubConfigIn"]).optional(),
            "deadLetterTopic": t.string().optional(),
            "desiredState": t.string().optional(),
        }
    ).named(renames["ExportConfigIn"])
    types["ExportConfigOut"] = t.struct(
        {
            "pubsubConfig": t.proxy(renames["PubSubConfigOut"]).optional(),
            "deadLetterTopic": t.string().optional(),
            "desiredState": t.string().optional(),
            "currentState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportConfigOut"])
    types["ComputeMessageStatsRequestIn"] = t.struct(
        {
            "endCursor": t.proxy(renames["CursorIn"]).optional(),
            "startCursor": t.proxy(renames["CursorIn"]).optional(),
            "partition": t.string(),
        }
    ).named(renames["ComputeMessageStatsRequestIn"])
    types["ComputeMessageStatsRequestOut"] = t.struct(
        {
            "endCursor": t.proxy(renames["CursorOut"]).optional(),
            "startCursor": t.proxy(renames["CursorOut"]).optional(),
            "partition": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeMessageStatsRequestOut"])
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
    types["SeekSubscriptionResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekSubscriptionResponseIn"]
    )
    types["SeekSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekSubscriptionResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ComputeTimeCursorResponseIn"] = t.struct(
        {"cursor": t.proxy(renames["CursorIn"]).optional()}
    ).named(renames["ComputeTimeCursorResponseIn"])
    types["ComputeTimeCursorResponseOut"] = t.struct(
        {
            "cursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeTimeCursorResponseOut"])
    types["PartitionConfigIn"] = t.struct(
        {
            "count": t.string().optional(),
            "scale": t.integer().optional(),
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
        }
    ).named(renames["PartitionConfigIn"])
    types["PartitionConfigOut"] = t.struct(
        {
            "count": t.string().optional(),
            "scale": t.integer().optional(),
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionConfigOut"])
    types["ListReservationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reservations": t.array(t.proxy(renames["ReservationIn"])).optional(),
        }
    ).named(renames["ListReservationsResponseIn"])
    types["ListReservationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "reservations": t.array(t.proxy(renames["ReservationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReservationsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TopicPartitionsIn"] = t.struct(
        {"partitionCount": t.string().optional()}
    ).named(renames["TopicPartitionsIn"])
    types["TopicPartitionsOut"] = t.struct(
        {
            "partitionCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicPartitionsOut"])
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
    types["ComputeMessageStatsResponseIn"] = t.struct(
        {
            "minimumEventTime": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
            "messageBytes": t.string().optional(),
            "messageCount": t.string().optional(),
        }
    ).named(renames["ComputeMessageStatsResponseIn"])
    types["ComputeMessageStatsResponseOut"] = t.struct(
        {
            "minimumEventTime": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
            "messageBytes": t.string().optional(),
            "messageCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeMessageStatsResponseOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CommitCursorResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CommitCursorResponseIn"]
    )
    types["CommitCursorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommitCursorResponseOut"])
    types["ComputeHeadCursorRequestIn"] = t.struct({"partition": t.string()}).named(
        renames["ComputeHeadCursorRequestIn"]
    )
    types["ComputeHeadCursorRequestOut"] = t.struct(
        {"partition": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ComputeHeadCursorRequestOut"])
    types["PubSubConfigIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubSubConfigIn"]
    )
    types["PubSubConfigOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubConfigOut"])
    types["TopicIn"] = t.struct(
        {
            "partitionConfig": t.proxy(renames["PartitionConfigIn"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigIn"]).optional(),
            "retentionConfig": t.proxy(renames["RetentionConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "partitionConfig": t.proxy(renames["PartitionConfigOut"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigOut"]).optional(),
            "retentionConfig": t.proxy(renames["RetentionConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["CursorIn"] = t.struct({"offset": t.string().optional()}).named(
        renames["CursorIn"]
    )
    types["CursorOut"] = t.struct(
        {
            "offset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CursorOut"])
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

    functions = {}
    functions["adminProjectsLocationsReservationsList"] = pubsublite.post(
        "v1/admin/{parent}/reservations",
        t.struct(
            {
                "reservationId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "throughputCapacity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsGet"] = pubsublite.post(
        "v1/admin/{parent}/reservations",
        t.struct(
            {
                "reservationId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "throughputCapacity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsDelete"] = pubsublite.post(
        "v1/admin/{parent}/reservations",
        t.struct(
            {
                "reservationId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "throughputCapacity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsPatch"] = pubsublite.post(
        "v1/admin/{parent}/reservations",
        t.struct(
            {
                "reservationId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "throughputCapacity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsCreate"] = pubsublite.post(
        "v1/admin/{parent}/reservations",
        t.struct(
            {
                "reservationId": t.string(),
                "parent": t.string(),
                "name": t.string().optional(),
                "throughputCapacity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsTopicsList"] = pubsublite.get(
        "v1/admin/{name}/topics",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReservationTopicsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsSubscriptionsSeek"] = pubsublite.get(
        "v1/admin/{parent}/subscriptions",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsCancel"] = pubsublite.get(
        "v1/admin/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsDelete"] = pubsublite.get(
        "v1/admin/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsDelete"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsPatch"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsList"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsGetPartitions"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsCreate"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsGet"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsSubscriptionsList"] = pubsublite.get(
        "v1/admin/{name}/subscriptions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartitionCursorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["topicStatsProjectsLocationsTopicsComputeTimeCursor"] = pubsublite.post(
        "v1/topicStats/{topic}:computeMessageStats",
        t.struct(
            {
                "topic": t.string(),
                "endCursor": t.proxy(renames["CursorIn"]).optional(),
                "startCursor": t.proxy(renames["CursorIn"]).optional(),
                "partition": t.string(),
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
                "endCursor": t.proxy(renames["CursorIn"]).optional(),
                "startCursor": t.proxy(renames["CursorIn"]).optional(),
                "partition": t.string(),
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
                "endCursor": t.proxy(renames["CursorIn"]).optional(),
                "startCursor": t.proxy(renames["CursorIn"]).optional(),
                "partition": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeMessageStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="pubsublite", renames=renames, types=types, functions=functions
    )
