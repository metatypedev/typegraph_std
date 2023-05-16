from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_bigqueryreservation() -> Import:
    bigqueryreservation = HTTPRuntime("https://bigqueryreservation.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryreservation_1_ErrorResponse",
        "SearchAllAssignmentsResponseIn": "_bigqueryreservation_2_SearchAllAssignmentsResponseIn",
        "SearchAllAssignmentsResponseOut": "_bigqueryreservation_3_SearchAllAssignmentsResponseOut",
        "SplitCapacityCommitmentRequestIn": "_bigqueryreservation_4_SplitCapacityCommitmentRequestIn",
        "SplitCapacityCommitmentRequestOut": "_bigqueryreservation_5_SplitCapacityCommitmentRequestOut",
        "SplitCapacityCommitmentResponseIn": "_bigqueryreservation_6_SplitCapacityCommitmentResponseIn",
        "SplitCapacityCommitmentResponseOut": "_bigqueryreservation_7_SplitCapacityCommitmentResponseOut",
        "ListReservationsResponseIn": "_bigqueryreservation_8_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_bigqueryreservation_9_ListReservationsResponseOut",
        "ReservationIn": "_bigqueryreservation_10_ReservationIn",
        "ReservationOut": "_bigqueryreservation_11_ReservationOut",
        "CapacityCommitmentIn": "_bigqueryreservation_12_CapacityCommitmentIn",
        "CapacityCommitmentOut": "_bigqueryreservation_13_CapacityCommitmentOut",
        "TableReferenceIn": "_bigqueryreservation_14_TableReferenceIn",
        "TableReferenceOut": "_bigqueryreservation_15_TableReferenceOut",
        "EmptyIn": "_bigqueryreservation_16_EmptyIn",
        "EmptyOut": "_bigqueryreservation_17_EmptyOut",
        "ListCapacityCommitmentsResponseIn": "_bigqueryreservation_18_ListCapacityCommitmentsResponseIn",
        "ListCapacityCommitmentsResponseOut": "_bigqueryreservation_19_ListCapacityCommitmentsResponseOut",
        "BiReservationIn": "_bigqueryreservation_20_BiReservationIn",
        "BiReservationOut": "_bigqueryreservation_21_BiReservationOut",
        "AutoscaleIn": "_bigqueryreservation_22_AutoscaleIn",
        "AutoscaleOut": "_bigqueryreservation_23_AutoscaleOut",
        "AssignmentIn": "_bigqueryreservation_24_AssignmentIn",
        "AssignmentOut": "_bigqueryreservation_25_AssignmentOut",
        "StatusIn": "_bigqueryreservation_26_StatusIn",
        "StatusOut": "_bigqueryreservation_27_StatusOut",
        "ListAssignmentsResponseIn": "_bigqueryreservation_28_ListAssignmentsResponseIn",
        "ListAssignmentsResponseOut": "_bigqueryreservation_29_ListAssignmentsResponseOut",
        "SearchAssignmentsResponseIn": "_bigqueryreservation_30_SearchAssignmentsResponseIn",
        "SearchAssignmentsResponseOut": "_bigqueryreservation_31_SearchAssignmentsResponseOut",
        "MergeCapacityCommitmentsRequestIn": "_bigqueryreservation_32_MergeCapacityCommitmentsRequestIn",
        "MergeCapacityCommitmentsRequestOut": "_bigqueryreservation_33_MergeCapacityCommitmentsRequestOut",
        "MoveAssignmentRequestIn": "_bigqueryreservation_34_MoveAssignmentRequestIn",
        "MoveAssignmentRequestOut": "_bigqueryreservation_35_MoveAssignmentRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SplitCapacityCommitmentRequestIn"] = t.struct(
        {"slotCount": t.string().optional()}
    ).named(renames["SplitCapacityCommitmentRequestIn"])
    types["SplitCapacityCommitmentRequestOut"] = t.struct(
        {
            "slotCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentRequestOut"])
    types["SplitCapacityCommitmentResponseIn"] = t.struct(
        {
            "first": t.proxy(renames["CapacityCommitmentIn"]).optional(),
            "second": t.proxy(renames["CapacityCommitmentIn"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentResponseIn"])
    types["SplitCapacityCommitmentResponseOut"] = t.struct(
        {
            "first": t.proxy(renames["CapacityCommitmentOut"]).optional(),
            "second": t.proxy(renames["CapacityCommitmentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentResponseOut"])
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
        {
            "slotCapacity": t.string().optional(),
            "ignoreIdleSlots": t.boolean().optional(),
            "edition": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "name": t.string().optional(),
            "concurrency": t.string().optional(),
        }
    ).named(renames["ReservationIn"])
    types["ReservationOut"] = t.struct(
        {
            "slotCapacity": t.string().optional(),
            "ignoreIdleSlots": t.boolean().optional(),
            "edition": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleOut"]).optional(),
            "creationTime": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "concurrency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationOut"])
    types["CapacityCommitmentIn"] = t.struct(
        {
            "plan": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "slotCount": t.string().optional(),
            "renewalPlan": t.string().optional(),
            "edition": t.string().optional(),
        }
    ).named(renames["CapacityCommitmentIn"])
    types["CapacityCommitmentOut"] = t.struct(
        {
            "plan": t.string().optional(),
            "commitmentEndTime": t.string().optional(),
            "commitmentStartTime": t.string().optional(),
            "name": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "slotCount": t.string().optional(),
            "renewalPlan": t.string().optional(),
            "edition": t.string().optional(),
            "failureStatus": t.proxy(renames["StatusOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityCommitmentOut"])
    types["TableReferenceIn"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["TableReferenceIn"])
    types["TableReferenceOut"] = t.struct(
        {
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableReferenceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["BiReservationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "size": t.string().optional(),
            "preferredTables": t.array(t.proxy(renames["TableReferenceIn"])).optional(),
        }
    ).named(renames["BiReservationIn"])
    types["BiReservationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "size": t.string().optional(),
            "preferredTables": t.array(
                t.proxy(renames["TableReferenceOut"])
            ).optional(),
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
    types["AssignmentIn"] = t.struct(
        {"assignee": t.string().optional(), "jobType": t.string().optional()}
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "assignee": t.string().optional(),
            "state": t.string().optional(),
            "jobType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
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
    types["SearchAssignmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignments": t.array(t.proxy(renames["AssignmentIn"])).optional(),
        }
    ).named(renames["SearchAssignmentsResponseIn"])
    types["SearchAssignmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignments": t.array(t.proxy(renames["AssignmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAssignmentsResponseOut"])
    types["MergeCapacityCommitmentsRequestIn"] = t.struct(
        {"capacityCommitmentIds": t.array(t.string()).optional()}
    ).named(renames["MergeCapacityCommitmentsRequestIn"])
    types["MergeCapacityCommitmentsRequestOut"] = t.struct(
        {
            "capacityCommitmentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeCapacityCommitmentsRequestOut"])
    types["MoveAssignmentRequestIn"] = t.struct(
        {"destinationId": t.string().optional(), "assignmentId": t.string().optional()}
    ).named(renames["MoveAssignmentRequestIn"])
    types["MoveAssignmentRequestOut"] = t.struct(
        {
            "destinationId": t.string().optional(),
            "assignmentId": t.string().optional(),
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
    functions["projectsLocationsCapacityCommitmentsList"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
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
    functions["projectsLocationsCapacityCommitmentsPatch"] = bigqueryreservation.get(
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
    functions["projectsLocationsCapacityCommitmentsGet"] = bigqueryreservation.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CapacityCommitmentOut"]),
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
    functions["projectsLocationsReservationsDelete"] = bigqueryreservation.get(
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
    ] = bigqueryreservation.post(
        "v1/{parent}/assignments",
        t.struct(
            {
                "assignmentId": t.string().optional(),
                "parent": t.string(),
                "assignee": t.string().optional(),
                "jobType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsList"
    ] = bigqueryreservation.post(
        "v1/{parent}/assignments",
        t.struct(
            {
                "assignmentId": t.string().optional(),
                "parent": t.string(),
                "assignee": t.string().optional(),
                "jobType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsPatch"
    ] = bigqueryreservation.post(
        "v1/{parent}/assignments",
        t.struct(
            {
                "assignmentId": t.string().optional(),
                "parent": t.string(),
                "assignee": t.string().optional(),
                "jobType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsDelete"
    ] = bigqueryreservation.post(
        "v1/{parent}/assignments",
        t.struct(
            {
                "assignmentId": t.string().optional(),
                "parent": t.string(),
                "assignee": t.string().optional(),
                "jobType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsCreate"
    ] = bigqueryreservation.post(
        "v1/{parent}/assignments",
        t.struct(
            {
                "assignmentId": t.string().optional(),
                "parent": t.string(),
                "assignee": t.string().optional(),
                "jobType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigqueryreservation",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
