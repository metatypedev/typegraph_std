from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_bigqueryreservation() -> Import:
    bigqueryreservation = HTTPRuntime("https://bigqueryreservation.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryreservation_1_ErrorResponse",
        "AutoscaleIn": "_bigqueryreservation_2_AutoscaleIn",
        "AutoscaleOut": "_bigqueryreservation_3_AutoscaleOut",
        "SearchAssignmentsResponseIn": "_bigqueryreservation_4_SearchAssignmentsResponseIn",
        "SearchAssignmentsResponseOut": "_bigqueryreservation_5_SearchAssignmentsResponseOut",
        "EmptyIn": "_bigqueryreservation_6_EmptyIn",
        "EmptyOut": "_bigqueryreservation_7_EmptyOut",
        "CapacityCommitmentIn": "_bigqueryreservation_8_CapacityCommitmentIn",
        "CapacityCommitmentOut": "_bigqueryreservation_9_CapacityCommitmentOut",
        "ListAssignmentsResponseIn": "_bigqueryreservation_10_ListAssignmentsResponseIn",
        "ListAssignmentsResponseOut": "_bigqueryreservation_11_ListAssignmentsResponseOut",
        "AssignmentIn": "_bigqueryreservation_12_AssignmentIn",
        "AssignmentOut": "_bigqueryreservation_13_AssignmentOut",
        "StatusIn": "_bigqueryreservation_14_StatusIn",
        "StatusOut": "_bigqueryreservation_15_StatusOut",
        "SplitCapacityCommitmentResponseIn": "_bigqueryreservation_16_SplitCapacityCommitmentResponseIn",
        "SplitCapacityCommitmentResponseOut": "_bigqueryreservation_17_SplitCapacityCommitmentResponseOut",
        "MergeCapacityCommitmentsRequestIn": "_bigqueryreservation_18_MergeCapacityCommitmentsRequestIn",
        "MergeCapacityCommitmentsRequestOut": "_bigqueryreservation_19_MergeCapacityCommitmentsRequestOut",
        "MoveAssignmentRequestIn": "_bigqueryreservation_20_MoveAssignmentRequestIn",
        "MoveAssignmentRequestOut": "_bigqueryreservation_21_MoveAssignmentRequestOut",
        "ListCapacityCommitmentsResponseIn": "_bigqueryreservation_22_ListCapacityCommitmentsResponseIn",
        "ListCapacityCommitmentsResponseOut": "_bigqueryreservation_23_ListCapacityCommitmentsResponseOut",
        "TableReferenceIn": "_bigqueryreservation_24_TableReferenceIn",
        "TableReferenceOut": "_bigqueryreservation_25_TableReferenceOut",
        "SplitCapacityCommitmentRequestIn": "_bigqueryreservation_26_SplitCapacityCommitmentRequestIn",
        "SplitCapacityCommitmentRequestOut": "_bigqueryreservation_27_SplitCapacityCommitmentRequestOut",
        "BiReservationIn": "_bigqueryreservation_28_BiReservationIn",
        "BiReservationOut": "_bigqueryreservation_29_BiReservationOut",
        "SearchAllAssignmentsResponseIn": "_bigqueryreservation_30_SearchAllAssignmentsResponseIn",
        "SearchAllAssignmentsResponseOut": "_bigqueryreservation_31_SearchAllAssignmentsResponseOut",
        "ListReservationsResponseIn": "_bigqueryreservation_32_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_bigqueryreservation_33_ListReservationsResponseOut",
        "ReservationIn": "_bigqueryreservation_34_ReservationIn",
        "ReservationOut": "_bigqueryreservation_35_ReservationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AutoscaleIn"] = t.struct({"maxSlots": t.string().optional()}).named(
        renames["AutoscaleIn"]
    )
    types["AutoscaleOut"] = t.struct(
        {
            "currentSlots": t.string().optional(),
            "maxSlots": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoscaleOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CapacityCommitmentIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "renewalPlan": t.string().optional(),
            "slotCount": t.string().optional(),
            "plan": t.string().optional(),
        }
    ).named(renames["CapacityCommitmentIn"])
    types["CapacityCommitmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "edition": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "commitmentStartTime": t.string().optional(),
            "commitmentEndTime": t.string().optional(),
            "renewalPlan": t.string().optional(),
            "name": t.string().optional(),
            "failureStatus": t.proxy(renames["StatusOut"]).optional(),
            "slotCount": t.string().optional(),
            "plan": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityCommitmentOut"])
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
    types["AssignmentIn"] = t.struct(
        {"jobType": t.string().optional(), "assignee": t.string().optional()}
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "jobType": t.string().optional(),
            "assignee": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["ListCapacityCommitmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "capacityCommitments": t.array(
                t.proxy(renames["CapacityCommitmentIn"])
            ).optional(),
        }
    ).named(renames["ListCapacityCommitmentsResponseIn"])
    types["ListCapacityCommitmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "capacityCommitments": t.array(
                t.proxy(renames["CapacityCommitmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCapacityCommitmentsResponseOut"])
    types["TableReferenceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "tableId": t.string().optional(),
            "datasetId": t.string().optional(),
        }
    ).named(renames["TableReferenceIn"])
    types["TableReferenceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "tableId": t.string().optional(),
            "datasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableReferenceOut"])
    types["SplitCapacityCommitmentRequestIn"] = t.struct(
        {"slotCount": t.string().optional()}
    ).named(renames["SplitCapacityCommitmentRequestIn"])
    types["SplitCapacityCommitmentRequestOut"] = t.struct(
        {
            "slotCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentRequestOut"])
    types["BiReservationIn"] = t.struct(
        {
            "size": t.string().optional(),
            "preferredTables": t.array(t.proxy(renames["TableReferenceIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["BiReservationIn"])
    types["BiReservationOut"] = t.struct(
        {
            "size": t.string().optional(),
            "preferredTables": t.array(
                t.proxy(renames["TableReferenceOut"])
            ).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BiReservationOut"])
    types["SearchAllAssignmentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignments": t.array(t.proxy(renames["AssignmentIn"])).optional(),
        }
    ).named(renames["SearchAllAssignmentsResponseIn"])
    types["SearchAllAssignmentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "assignments": t.array(t.proxy(renames["AssignmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchAllAssignmentsResponseOut"])
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
    types["ReservationIn"] = t.struct(
        {
            "ignoreIdleSlots": t.boolean().optional(),
            "name": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
            "edition": t.string().optional(),
            "slotCapacity": t.string().optional(),
            "concurrency": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
        }
    ).named(renames["ReservationIn"])
    types["ReservationOut"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "ignoreIdleSlots": t.boolean().optional(),
            "name": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleOut"]).optional(),
            "edition": t.string().optional(),
            "slotCapacity": t.string().optional(),
            "concurrency": t.string().optional(),
            "updateTime": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationOut"])

    functions = {}
    functions["projectsLocationsUpdateBiReservation"] = bigqueryreservation.get(
        "v1/{parent}:searchAssignments",
        t.struct(
            {
                "parent": t.string(),
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetBiReservation"] = bigqueryreservation.get(
        "v1/{parent}:searchAssignments",
        t.struct(
            {
                "parent": t.string(),
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSearchAllAssignments"] = bigqueryreservation.get(
        "v1/{parent}:searchAssignments",
        t.struct(
            {
                "parent": t.string(),
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSearchAssignments"] = bigqueryreservation.get(
        "v1/{parent}:searchAssignments",
        t.struct(
            {
                "parent": t.string(),
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchAssignmentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsCreate"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "edition": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "renewalPlan": t.string().optional(),
                "slotCount": t.string().optional(),
                "plan": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsSplit"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "edition": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "renewalPlan": t.string().optional(),
                "slotCount": t.string().optional(),
                "plan": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsDelete"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "edition": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "renewalPlan": t.string().optional(),
                "slotCount": t.string().optional(),
                "plan": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsMerge"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "edition": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "renewalPlan": t.string().optional(),
                "slotCount": t.string().optional(),
                "plan": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsGet"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "edition": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "renewalPlan": t.string().optional(),
                "slotCount": t.string().optional(),
                "plan": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsList"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "edition": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "renewalPlan": t.string().optional(),
                "slotCount": t.string().optional(),
                "plan": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsPatch"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "edition": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "renewalPlan": t.string().optional(),
                "slotCount": t.string().optional(),
                "plan": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
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
        "projectsLocationsReservationsAssignmentsPatch"
    ] = bigqueryreservation.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsCreate"
    ] = bigqueryreservation.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsList"
    ] = bigqueryreservation.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsMove"
    ] = bigqueryreservation.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsReservationsAssignmentsDelete"
    ] = bigqueryreservation.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigqueryreservation",
        renames=renames,
        types=types,
        functions=functions,
    )
