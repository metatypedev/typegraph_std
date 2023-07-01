from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_bigqueryreservation():
    bigqueryreservation = HTTPRuntime("https://bigqueryreservation.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryreservation_1_ErrorResponse",
        "BiReservationIn": "_bigqueryreservation_2_BiReservationIn",
        "BiReservationOut": "_bigqueryreservation_3_BiReservationOut",
        "AutoscaleIn": "_bigqueryreservation_4_AutoscaleIn",
        "AutoscaleOut": "_bigqueryreservation_5_AutoscaleOut",
        "ListCapacityCommitmentsResponseIn": "_bigqueryreservation_6_ListCapacityCommitmentsResponseIn",
        "ListCapacityCommitmentsResponseOut": "_bigqueryreservation_7_ListCapacityCommitmentsResponseOut",
        "SplitCapacityCommitmentRequestIn": "_bigqueryreservation_8_SplitCapacityCommitmentRequestIn",
        "SplitCapacityCommitmentRequestOut": "_bigqueryreservation_9_SplitCapacityCommitmentRequestOut",
        "SearchAllAssignmentsResponseIn": "_bigqueryreservation_10_SearchAllAssignmentsResponseIn",
        "SearchAllAssignmentsResponseOut": "_bigqueryreservation_11_SearchAllAssignmentsResponseOut",
        "EmptyIn": "_bigqueryreservation_12_EmptyIn",
        "EmptyOut": "_bigqueryreservation_13_EmptyOut",
        "ReservationIn": "_bigqueryreservation_14_ReservationIn",
        "ReservationOut": "_bigqueryreservation_15_ReservationOut",
        "StatusIn": "_bigqueryreservation_16_StatusIn",
        "StatusOut": "_bigqueryreservation_17_StatusOut",
        "TableReferenceIn": "_bigqueryreservation_18_TableReferenceIn",
        "TableReferenceOut": "_bigqueryreservation_19_TableReferenceOut",
        "AssignmentIn": "_bigqueryreservation_20_AssignmentIn",
        "AssignmentOut": "_bigqueryreservation_21_AssignmentOut",
        "SplitCapacityCommitmentResponseIn": "_bigqueryreservation_22_SplitCapacityCommitmentResponseIn",
        "SplitCapacityCommitmentResponseOut": "_bigqueryreservation_23_SplitCapacityCommitmentResponseOut",
        "MergeCapacityCommitmentsRequestIn": "_bigqueryreservation_24_MergeCapacityCommitmentsRequestIn",
        "MergeCapacityCommitmentsRequestOut": "_bigqueryreservation_25_MergeCapacityCommitmentsRequestOut",
        "SearchAssignmentsResponseIn": "_bigqueryreservation_26_SearchAssignmentsResponseIn",
        "SearchAssignmentsResponseOut": "_bigqueryreservation_27_SearchAssignmentsResponseOut",
        "ListReservationsResponseIn": "_bigqueryreservation_28_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_bigqueryreservation_29_ListReservationsResponseOut",
        "ListAssignmentsResponseIn": "_bigqueryreservation_30_ListAssignmentsResponseIn",
        "ListAssignmentsResponseOut": "_bigqueryreservation_31_ListAssignmentsResponseOut",
        "CapacityCommitmentIn": "_bigqueryreservation_32_CapacityCommitmentIn",
        "CapacityCommitmentOut": "_bigqueryreservation_33_CapacityCommitmentOut",
        "MoveAssignmentRequestIn": "_bigqueryreservation_34_MoveAssignmentRequestIn",
        "MoveAssignmentRequestOut": "_bigqueryreservation_35_MoveAssignmentRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BiReservationIn"] = t.struct(
        {
            "preferredTables": t.array(t.proxy(renames["TableReferenceIn"])).optional(),
            "name": t.string().optional(),
            "size": t.string().optional(),
        }
    ).named(renames["BiReservationIn"])
    types["BiReservationOut"] = t.struct(
        {
            "preferredTables": t.array(
                t.proxy(renames["TableReferenceOut"])
            ).optional(),
            "name": t.string().optional(),
            "size": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiReservationOut"])
    types["AutoscaleIn"] = t.struct({"maxSlots": t.string().optional()}).named(
        renames["AutoscaleIn"]
    )
    types["AutoscaleOut"] = t.struct(
        {
            "maxSlots": t.string().optional(),
            "currentSlots": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscaleOut"])
    types["ListCapacityCommitmentsResponseIn"] = t.struct(
        {
            "capacityCommitments": t.array(
                t.proxy(renames["CapacityCommitmentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCapacityCommitmentsResponseIn"])
    types["ListCapacityCommitmentsResponseOut"] = t.struct(
        {
            "capacityCommitments": t.array(
                t.proxy(renames["CapacityCommitmentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCapacityCommitmentsResponseOut"])
    types["SplitCapacityCommitmentRequestIn"] = t.struct(
        {"slotCount": t.string().optional()}
    ).named(renames["SplitCapacityCommitmentRequestIn"])
    types["SplitCapacityCommitmentRequestOut"] = t.struct(
        {
            "slotCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentRequestOut"])
    types["SearchAllAssignmentsResponseIn"] = t.struct(
        {
            "assignments": t.array(t.proxy(renames["AssignmentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchAllAssignmentsResponseIn"])
    types["SearchAllAssignmentsResponseOut"] = t.struct(
        {
            "assignments": t.array(t.proxy(renames["AssignmentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAllAssignmentsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ReservationIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "slotCapacity": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "name": t.string().optional(),
            "concurrency": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
            "ignoreIdleSlots": t.boolean().optional(),
        }
    ).named(renames["ReservationIn"])
    types["ReservationOut"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "edition": t.string().optional(),
            "slotCapacity": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "name": t.string().optional(),
            "concurrency": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleOut"]).optional(),
            "updateTime": t.string().optional(),
            "ignoreIdleSlots": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationOut"])
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
    types["TableReferenceIn"] = t.struct(
        {
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
        }
    ).named(renames["TableReferenceIn"])
    types["TableReferenceOut"] = t.struct(
        {
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableReferenceOut"])
    types["AssignmentIn"] = t.struct(
        {"jobType": t.string().optional(), "assignee": t.string().optional()}
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "jobType": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "assignee": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
    types["SplitCapacityCommitmentResponseIn"] = t.struct(
        {
            "second": t.proxy(renames["CapacityCommitmentIn"]).optional(),
            "first": t.proxy(renames["CapacityCommitmentIn"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentResponseIn"])
    types["SplitCapacityCommitmentResponseOut"] = t.struct(
        {
            "second": t.proxy(renames["CapacityCommitmentOut"]).optional(),
            "first": t.proxy(renames["CapacityCommitmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentResponseOut"])
    types["MergeCapacityCommitmentsRequestIn"] = t.struct(
        {"capacityCommitmentIds": t.array(t.string()).optional()}
    ).named(renames["MergeCapacityCommitmentsRequestIn"])
    types["MergeCapacityCommitmentsRequestOut"] = t.struct(
        {
            "capacityCommitmentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeCapacityCommitmentsRequestOut"])
    types["SearchAssignmentsResponseIn"] = t.struct(
        {
            "assignments": t.array(t.proxy(renames["AssignmentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchAssignmentsResponseIn"])
    types["SearchAssignmentsResponseOut"] = t.struct(
        {
            "assignments": t.array(t.proxy(renames["AssignmentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAssignmentsResponseOut"])
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
    types["ListAssignmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignments": t.array(t.proxy(renames["AssignmentIn"])).optional(),
        }
    ).named(renames["ListAssignmentsResponseIn"])
    types["ListAssignmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignments": t.array(t.proxy(renames["AssignmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssignmentsResponseOut"])
    types["CapacityCommitmentIn"] = t.struct(
        {
            "slotCount": t.string().optional(),
            "plan": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "edition": t.string().optional(),
            "renewalPlan": t.string().optional(),
        }
    ).named(renames["CapacityCommitmentIn"])
    types["CapacityCommitmentOut"] = t.struct(
        {
            "commitmentEndTime": t.string().optional(),
            "isFlatRate": t.boolean().optional(),
            "slotCount": t.string().optional(),
            "plan": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "state": t.string().optional(),
            "edition": t.string().optional(),
            "failureStatus": t.proxy(renames["StatusOut"]).optional(),
            "renewalPlan": t.string().optional(),
            "commitmentStartTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityCommitmentOut"])
    types["MoveAssignmentRequestIn"] = t.struct(
        {"assignmentId": t.string().optional(), "destinationId": t.string().optional()}
    ).named(renames["MoveAssignmentRequestIn"])
    types["MoveAssignmentRequestOut"] = t.struct(
        {
            "assignmentId": t.string().optional(),
            "destinationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveAssignmentRequestOut"])

    functions = {}
    functions["projectsLocationsSearchAssignments"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSearchAllAssignments"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateBiReservation"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetBiReservation"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsDelete"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsPatch"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsCreate"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsList"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsGet"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsMove"
    ] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "jobType": t.string().optional(),
                "assignee": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsDelete"
    ] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "jobType": t.string().optional(),
                "assignee": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsCreate"
    ] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "jobType": t.string().optional(),
                "assignee": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsList"
    ] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "jobType": t.string().optional(),
                "assignee": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsPatch"
    ] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "jobType": t.string().optional(),
                "assignee": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsMerge"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsDelete"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsSplit"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsCreate"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsList"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsPatch"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsGet"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigqueryreservation",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
