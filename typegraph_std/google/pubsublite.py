from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_pubsublite() -> Import:
    pubsublite = HTTPRuntime("https://pubsublite.googleapis.com/")

    renames = {
        "ErrorResponse": "_pubsublite_1_ErrorResponse",
        "ComputeMessageStatsResponseIn": "_pubsublite_2_ComputeMessageStatsResponseIn",
        "ComputeMessageStatsResponseOut": "_pubsublite_3_ComputeMessageStatsResponseOut",
        "CursorIn": "_pubsublite_4_CursorIn",
        "CursorOut": "_pubsublite_5_CursorOut",
        "EmptyIn": "_pubsublite_6_EmptyIn",
        "EmptyOut": "_pubsublite_7_EmptyOut",
        "ListSubscriptionsResponseIn": "_pubsublite_8_ListSubscriptionsResponseIn",
        "ListSubscriptionsResponseOut": "_pubsublite_9_ListSubscriptionsResponseOut",
        "ReservationConfigIn": "_pubsublite_10_ReservationConfigIn",
        "ReservationConfigOut": "_pubsublite_11_ReservationConfigOut",
        "ListReservationTopicsResponseIn": "_pubsublite_12_ListReservationTopicsResponseIn",
        "ListReservationTopicsResponseOut": "_pubsublite_13_ListReservationTopicsResponseOut",
        "ListOperationsResponseIn": "_pubsublite_14_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_pubsublite_15_ListOperationsResponseOut",
        "SubscriptionIn": "_pubsublite_16_SubscriptionIn",
        "SubscriptionOut": "_pubsublite_17_SubscriptionOut",
        "ComputeTimeCursorRequestIn": "_pubsublite_18_ComputeTimeCursorRequestIn",
        "ComputeTimeCursorRequestOut": "_pubsublite_19_ComputeTimeCursorRequestOut",
        "TimeTargetIn": "_pubsublite_20_TimeTargetIn",
        "TimeTargetOut": "_pubsublite_21_TimeTargetOut",
        "ReservationIn": "_pubsublite_22_ReservationIn",
        "ReservationOut": "_pubsublite_23_ReservationOut",
        "ComputeTimeCursorResponseIn": "_pubsublite_24_ComputeTimeCursorResponseIn",
        "ComputeTimeCursorResponseOut": "_pubsublite_25_ComputeTimeCursorResponseOut",
        "CommitCursorResponseIn": "_pubsublite_26_CommitCursorResponseIn",
        "CommitCursorResponseOut": "_pubsublite_27_CommitCursorResponseOut",
        "RetentionConfigIn": "_pubsublite_28_RetentionConfigIn",
        "RetentionConfigOut": "_pubsublite_29_RetentionConfigOut",
        "TopicIn": "_pubsublite_30_TopicIn",
        "TopicOut": "_pubsublite_31_TopicOut",
        "CancelOperationRequestIn": "_pubsublite_32_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_pubsublite_33_CancelOperationRequestOut",
        "CapacityIn": "_pubsublite_34_CapacityIn",
        "CapacityOut": "_pubsublite_35_CapacityOut",
        "TopicPartitionsIn": "_pubsublite_36_TopicPartitionsIn",
        "TopicPartitionsOut": "_pubsublite_37_TopicPartitionsOut",
        "ListTopicSubscriptionsResponseIn": "_pubsublite_38_ListTopicSubscriptionsResponseIn",
        "ListTopicSubscriptionsResponseOut": "_pubsublite_39_ListTopicSubscriptionsResponseOut",
        "ListPartitionCursorsResponseIn": "_pubsublite_40_ListPartitionCursorsResponseIn",
        "ListPartitionCursorsResponseOut": "_pubsublite_41_ListPartitionCursorsResponseOut",
        "PubSubConfigIn": "_pubsublite_42_PubSubConfigIn",
        "PubSubConfigOut": "_pubsublite_43_PubSubConfigOut",
        "ComputeHeadCursorResponseIn": "_pubsublite_44_ComputeHeadCursorResponseIn",
        "ComputeHeadCursorResponseOut": "_pubsublite_45_ComputeHeadCursorResponseOut",
        "OperationIn": "_pubsublite_46_OperationIn",
        "OperationOut": "_pubsublite_47_OperationOut",
        "ListReservationsResponseIn": "_pubsublite_48_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_pubsublite_49_ListReservationsResponseOut",
        "DeliveryConfigIn": "_pubsublite_50_DeliveryConfigIn",
        "DeliveryConfigOut": "_pubsublite_51_DeliveryConfigOut",
        "PartitionConfigIn": "_pubsublite_52_PartitionConfigIn",
        "PartitionConfigOut": "_pubsublite_53_PartitionConfigOut",
        "ComputeHeadCursorRequestIn": "_pubsublite_54_ComputeHeadCursorRequestIn",
        "ComputeHeadCursorRequestOut": "_pubsublite_55_ComputeHeadCursorRequestOut",
        "ComputeMessageStatsRequestIn": "_pubsublite_56_ComputeMessageStatsRequestIn",
        "ComputeMessageStatsRequestOut": "_pubsublite_57_ComputeMessageStatsRequestOut",
        "CommitCursorRequestIn": "_pubsublite_58_CommitCursorRequestIn",
        "CommitCursorRequestOut": "_pubsublite_59_CommitCursorRequestOut",
        "PartitionCursorIn": "_pubsublite_60_PartitionCursorIn",
        "PartitionCursorOut": "_pubsublite_61_PartitionCursorOut",
        "ExportConfigIn": "_pubsublite_62_ExportConfigIn",
        "ExportConfigOut": "_pubsublite_63_ExportConfigOut",
        "StatusIn": "_pubsublite_64_StatusIn",
        "StatusOut": "_pubsublite_65_StatusOut",
        "SeekSubscriptionRequestIn": "_pubsublite_66_SeekSubscriptionRequestIn",
        "SeekSubscriptionRequestOut": "_pubsublite_67_SeekSubscriptionRequestOut",
        "ListTopicsResponseIn": "_pubsublite_68_ListTopicsResponseIn",
        "ListTopicsResponseOut": "_pubsublite_69_ListTopicsResponseOut",
        "SeekSubscriptionResponseIn": "_pubsublite_70_SeekSubscriptionResponseIn",
        "SeekSubscriptionResponseOut": "_pubsublite_71_SeekSubscriptionResponseOut",
        "OperationMetadataIn": "_pubsublite_72_OperationMetadataIn",
        "OperationMetadataOut": "_pubsublite_73_OperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ComputeMessageStatsResponseIn"] = t.struct(
        {
            "minimumEventTime": t.string().optional(),
            "messageBytes": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
            "messageCount": t.string().optional(),
        }
    ).named(renames["ComputeMessageStatsResponseIn"])
    types["ComputeMessageStatsResponseOut"] = t.struct(
        {
            "minimumEventTime": t.string().optional(),
            "messageBytes": t.string().optional(),
            "minimumPublishTime": t.string().optional(),
            "messageCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeMessageStatsResponseOut"])
    types["CursorIn"] = t.struct({"offset": t.string().optional()}).named(
        renames["CursorIn"]
    )
    types["CursorOut"] = t.struct(
        {
            "offset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CursorOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ReservationConfigIn"] = t.struct(
        {"throughputReservation": t.string().optional()}
    ).named(renames["ReservationConfigIn"])
    types["ReservationConfigOut"] = t.struct(
        {
            "throughputReservation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationConfigOut"])
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
    types["SubscriptionIn"] = t.struct(
        {
            "topic": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigIn"]).optional(),
            "exportConfig": t.proxy(renames["ExportConfigIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SubscriptionIn"])
    types["SubscriptionOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "deliveryConfig": t.proxy(renames["DeliveryConfigOut"]).optional(),
            "exportConfig": t.proxy(renames["ExportConfigOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubscriptionOut"])
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
    types["TimeTargetIn"] = t.struct(
        {"eventTime": t.string().optional(), "publishTime": t.string().optional()}
    ).named(renames["TimeTargetIn"])
    types["TimeTargetOut"] = t.struct(
        {
            "eventTime": t.string().optional(),
            "publishTime": t.string().optional(),
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
    types["ComputeTimeCursorResponseIn"] = t.struct(
        {"cursor": t.proxy(renames["CursorIn"]).optional()}
    ).named(renames["ComputeTimeCursorResponseIn"])
    types["ComputeTimeCursorResponseOut"] = t.struct(
        {
            "cursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeTimeCursorResponseOut"])
    types["CommitCursorResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CommitCursorResponseIn"]
    )
    types["CommitCursorResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CommitCursorResponseOut"])
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
    types["TopicIn"] = t.struct(
        {
            "name": t.string().optional(),
            "retentionConfig": t.proxy(renames["RetentionConfigIn"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigIn"]).optional(),
            "partitionConfig": t.proxy(renames["PartitionConfigIn"]).optional(),
        }
    ).named(renames["TopicIn"])
    types["TopicOut"] = t.struct(
        {
            "name": t.string().optional(),
            "retentionConfig": t.proxy(renames["RetentionConfigOut"]).optional(),
            "reservationConfig": t.proxy(renames["ReservationConfigOut"]).optional(),
            "partitionConfig": t.proxy(renames["PartitionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["TopicPartitionsIn"] = t.struct(
        {"partitionCount": t.string().optional()}
    ).named(renames["TopicPartitionsIn"])
    types["TopicPartitionsOut"] = t.struct(
        {
            "partitionCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TopicPartitionsOut"])
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
    types["PubSubConfigIn"] = t.struct({"topic": t.string().optional()}).named(
        renames["PubSubConfigIn"]
    )
    types["PubSubConfigOut"] = t.struct(
        {
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PubSubConfigOut"])
    types["ComputeHeadCursorResponseIn"] = t.struct(
        {"headCursor": t.proxy(renames["CursorIn"]).optional()}
    ).named(renames["ComputeHeadCursorResponseIn"])
    types["ComputeHeadCursorResponseOut"] = t.struct(
        {
            "headCursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeHeadCursorResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["DeliveryConfigIn"] = t.struct(
        {"deliveryRequirement": t.string().optional()}
    ).named(renames["DeliveryConfigIn"])
    types["DeliveryConfigOut"] = t.struct(
        {
            "deliveryRequirement": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeliveryConfigOut"])
    types["PartitionConfigIn"] = t.struct(
        {
            "capacity": t.proxy(renames["CapacityIn"]).optional(),
            "count": t.string().optional(),
            "scale": t.integer().optional(),
        }
    ).named(renames["PartitionConfigIn"])
    types["PartitionConfigOut"] = t.struct(
        {
            "capacity": t.proxy(renames["CapacityOut"]).optional(),
            "count": t.string().optional(),
            "scale": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionConfigOut"])
    types["ComputeHeadCursorRequestIn"] = t.struct({"partition": t.string()}).named(
        renames["ComputeHeadCursorRequestIn"]
    )
    types["ComputeHeadCursorRequestOut"] = t.struct(
        {"partition": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ComputeHeadCursorRequestOut"])
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
    types["PartitionCursorIn"] = t.struct(
        {
            "partition": t.string().optional(),
            "cursor": t.proxy(renames["CursorIn"]).optional(),
        }
    ).named(renames["PartitionCursorIn"])
    types["PartitionCursorOut"] = t.struct(
        {
            "partition": t.string().optional(),
            "cursor": t.proxy(renames["CursorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartitionCursorOut"])
    types["ExportConfigIn"] = t.struct(
        {
            "deadLetterTopic": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubSubConfigIn"]).optional(),
            "desiredState": t.string().optional(),
        }
    ).named(renames["ExportConfigIn"])
    types["ExportConfigOut"] = t.struct(
        {
            "deadLetterTopic": t.string().optional(),
            "pubsubConfig": t.proxy(renames["PubSubConfigOut"]).optional(),
            "desiredState": t.string().optional(),
            "currentState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExportConfigOut"])
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
    types["SeekSubscriptionResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SeekSubscriptionResponseIn"]
    )
    types["SeekSubscriptionResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SeekSubscriptionResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])

    functions = {}
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListPartitionCursorsResponseOut"]),
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
    functions["adminProjectsLocationsSubscriptionsPatch"] = pubsublite.delete(
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
    functions["adminProjectsLocationsSubscriptionsDelete"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsList"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsGet"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsCancel"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsOperationsDelete"] = pubsublite.delete(
        "v1/admin/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsCreate"] = pubsublite.get(
        "v1/admin/{name}/partitions",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicPartitionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsGet"] = pubsublite.get(
        "v1/admin/{name}/partitions",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicPartitionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsDelete"] = pubsublite.get(
        "v1/admin/{name}/partitions",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicPartitionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsPatch"] = pubsublite.get(
        "v1/admin/{name}/partitions",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicPartitionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsList"] = pubsublite.get(
        "v1/admin/{name}/partitions",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicPartitionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsGetPartitions"] = pubsublite.get(
        "v1/admin/{name}/partitions",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TopicPartitionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsTopicsSubscriptionsList"] = pubsublite.get(
        "v1/admin/{name}/subscriptions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTopicSubscriptionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsCreate"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsDelete"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsList"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsPatch"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsGet"] = pubsublite.get(
        "v1/admin/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["adminProjectsLocationsReservationsTopicsList"] = pubsublite.get(
        "v1/admin/{name}/topics",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReservationTopicsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="pubsublite",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
