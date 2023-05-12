from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_bigqueryreservation() -> Import:
    bigqueryreservation = HTTPRuntime("https://bigqueryreservation.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigqueryreservation_1_ErrorResponse",
        "MoveAssignmentRequestIn": "_bigqueryreservation_2_MoveAssignmentRequestIn",
        "MoveAssignmentRequestOut": "_bigqueryreservation_3_MoveAssignmentRequestOut",
        "MergeCapacityCommitmentsRequestIn": "_bigqueryreservation_4_MergeCapacityCommitmentsRequestIn",
        "MergeCapacityCommitmentsRequestOut": "_bigqueryreservation_5_MergeCapacityCommitmentsRequestOut",
        "BiReservationIn": "_bigqueryreservation_6_BiReservationIn",
        "BiReservationOut": "_bigqueryreservation_7_BiReservationOut",
        "ListReservationsResponseIn": "_bigqueryreservation_8_ListReservationsResponseIn",
        "ListReservationsResponseOut": "_bigqueryreservation_9_ListReservationsResponseOut",
        "SearchAssignmentsResponseIn": "_bigqueryreservation_10_SearchAssignmentsResponseIn",
        "SearchAssignmentsResponseOut": "_bigqueryreservation_11_SearchAssignmentsResponseOut",
        "StatusIn": "_bigqueryreservation_12_StatusIn",
        "StatusOut": "_bigqueryreservation_13_StatusOut",
        "SplitCapacityCommitmentResponseIn": "_bigqueryreservation_14_SplitCapacityCommitmentResponseIn",
        "SplitCapacityCommitmentResponseOut": "_bigqueryreservation_15_SplitCapacityCommitmentResponseOut",
        "CapacityCommitmentIn": "_bigqueryreservation_16_CapacityCommitmentIn",
        "CapacityCommitmentOut": "_bigqueryreservation_17_CapacityCommitmentOut",
        "SplitCapacityCommitmentRequestIn": "_bigqueryreservation_18_SplitCapacityCommitmentRequestIn",
        "SplitCapacityCommitmentRequestOut": "_bigqueryreservation_19_SplitCapacityCommitmentRequestOut",
        "ListAssignmentsResponseIn": "_bigqueryreservation_20_ListAssignmentsResponseIn",
        "ListAssignmentsResponseOut": "_bigqueryreservation_21_ListAssignmentsResponseOut",
        "AssignmentIn": "_bigqueryreservation_22_AssignmentIn",
        "AssignmentOut": "_bigqueryreservation_23_AssignmentOut",
        "SearchAllAssignmentsResponseIn": "_bigqueryreservation_24_SearchAllAssignmentsResponseIn",
        "SearchAllAssignmentsResponseOut": "_bigqueryreservation_25_SearchAllAssignmentsResponseOut",
        "ListCapacityCommitmentsResponseIn": "_bigqueryreservation_26_ListCapacityCommitmentsResponseIn",
        "ListCapacityCommitmentsResponseOut": "_bigqueryreservation_27_ListCapacityCommitmentsResponseOut",
        "AutoscaleIn": "_bigqueryreservation_28_AutoscaleIn",
        "AutoscaleOut": "_bigqueryreservation_29_AutoscaleOut",
        "ReservationIn": "_bigqueryreservation_30_ReservationIn",
        "ReservationOut": "_bigqueryreservation_31_ReservationOut",
        "TableReferenceIn": "_bigqueryreservation_32_TableReferenceIn",
        "TableReferenceOut": "_bigqueryreservation_33_TableReferenceOut",
        "EmptyIn": "_bigqueryreservation_34_EmptyIn",
        "EmptyOut": "_bigqueryreservation_35_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["MergeCapacityCommitmentsRequestIn"] = t.struct(
        {"capacityCommitmentIds": t.array(t.string()).optional()}
    ).named(renames["MergeCapacityCommitmentsRequestIn"])
    types["MergeCapacityCommitmentsRequestOut"] = t.struct(
        {
            "capacityCommitmentIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MergeCapacityCommitmentsRequestOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["CapacityCommitmentIn"] = t.struct(
        {
            "plan": t.string().optional(),
            "renewalPlan": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "edition": t.string().optional(),
            "slotCount": t.string().optional(),
        }
    ).named(renames["CapacityCommitmentIn"])
    types["CapacityCommitmentOut"] = t.struct(
        {
            "commitmentStartTime": t.string().optional(),
            "commitmentEndTime": t.string().optional(),
            "plan": t.string().optional(),
            "renewalPlan": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "edition": t.string().optional(),
            "slotCount": t.string().optional(),
            "failureStatus": t.proxy(renames["StatusOut"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CapacityCommitmentOut"])
    types["SplitCapacityCommitmentRequestIn"] = t.struct(
        {"slotCount": t.string().optional()}
    ).named(renames["SplitCapacityCommitmentRequestIn"])
    types["SplitCapacityCommitmentRequestOut"] = t.struct(
        {
            "slotCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SplitCapacityCommitmentRequestOut"])
    types["ListAssignmentsResponseIn"] = t.struct(
        {
            "assignments": t.array(t.proxy(renames["AssignmentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAssignmentsResponseIn"])
    types["ListAssignmentsResponseOut"] = t.struct(
        {
            "assignments": t.array(t.proxy(renames["AssignmentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAssignmentsResponseOut"])
    types["AssignmentIn"] = t.struct(
        {"jobType": t.string().optional(), "assignee": t.string().optional()}
    ).named(renames["AssignmentIn"])
    types["AssignmentOut"] = t.struct(
        {
            "state": t.string().optional(),
            "jobType": t.string().optional(),
            "assignee": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssignmentOut"])
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
    types["ReservationIn"] = t.struct(
        {
            "concurrency": t.string().optional(),
            "edition": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
            "slotCapacity": t.string().optional(),
            "name": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "ignoreIdleSlots": t.boolean().optional(),
        }
    ).named(renames["ReservationIn"])
    types["ReservationOut"] = t.struct(
        {
            "concurrency": t.string().optional(),
            "edition": t.string().optional(),
            "updateTime": t.string().optional(),
            "autoscale": t.proxy(renames["AutoscaleOut"]).optional(),
            "slotCapacity": t.string().optional(),
            "name": t.string().optional(),
            "creationTime": t.string().optional(),
            "multiRegionAuxiliary": t.boolean().optional(),
            "ignoreIdleSlots": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReservationOut"])
    types["TableReferenceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
        }
    ).named(renames["TableReferenceIn"])
    types["TableReferenceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "datasetId": t.string().optional(),
            "tableId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableReferenceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["projectsLocationsSearchAssignments"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "preferredTables": t.array(
                    t.proxy(renames["TableReferenceIn"])
                ).optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSearchAllAssignments"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "preferredTables": t.array(
                    t.proxy(renames["TableReferenceIn"])
                ).optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGetBiReservation"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "preferredTables": t.array(
                    t.proxy(renames["TableReferenceIn"])
                ).optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsUpdateBiReservation"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "preferredTables": t.array(
                    t.proxy(renames["TableReferenceIn"])
                ).optional(),
                "size": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BiReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsDelete"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "concurrency": t.string().optional(),
                "edition": t.string().optional(),
                "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
                "slotCapacity": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "ignoreIdleSlots": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsList"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "concurrency": t.string().optional(),
                "edition": t.string().optional(),
                "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
                "slotCapacity": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "ignoreIdleSlots": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsGet"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "concurrency": t.string().optional(),
                "edition": t.string().optional(),
                "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
                "slotCapacity": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "ignoreIdleSlots": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsCreate"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "concurrency": t.string().optional(),
                "edition": t.string().optional(),
                "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
                "slotCapacity": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "ignoreIdleSlots": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReservationsPatch"] = bigqueryreservation.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "concurrency": t.string().optional(),
                "edition": t.string().optional(),
                "autoscale": t.proxy(renames["AutoscaleIn"]).optional(),
                "slotCapacity": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "ignoreIdleSlots": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReservationOut"]),
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
    functions["projectsLocationsCapacityCommitmentsSplit"] = bigqueryreservation.post(
        "v1/{parent}/capacityCommitments",
        t.struct(
            {
                "enforceSingleAdminProjectPerOrg": t.boolean().optional(),
                "parent": t.string(),
                "capacityCommitmentId": t.string().optional(),
                "plan": t.string().optional(),
                "renewalPlan": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "edition": t.string().optional(),
                "slotCount": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsPatch"] = bigqueryreservation.post(
        "v1/{parent}/capacityCommitments",
        t.struct(
            {
                "enforceSingleAdminProjectPerOrg": t.boolean().optional(),
                "parent": t.string(),
                "capacityCommitmentId": t.string().optional(),
                "plan": t.string().optional(),
                "renewalPlan": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "edition": t.string().optional(),
                "slotCount": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsGet"] = bigqueryreservation.post(
        "v1/{parent}/capacityCommitments",
        t.struct(
            {
                "enforceSingleAdminProjectPerOrg": t.boolean().optional(),
                "parent": t.string(),
                "capacityCommitmentId": t.string().optional(),
                "plan": t.string().optional(),
                "renewalPlan": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "edition": t.string().optional(),
                "slotCount": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsList"] = bigqueryreservation.post(
        "v1/{parent}/capacityCommitments",
        t.struct(
            {
                "enforceSingleAdminProjectPerOrg": t.boolean().optional(),
                "parent": t.string(),
                "capacityCommitmentId": t.string().optional(),
                "plan": t.string().optional(),
                "renewalPlan": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "edition": t.string().optional(),
                "slotCount": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsMerge"] = bigqueryreservation.post(
        "v1/{parent}/capacityCommitments",
        t.struct(
            {
                "enforceSingleAdminProjectPerOrg": t.boolean().optional(),
                "parent": t.string(),
                "capacityCommitmentId": t.string().optional(),
                "plan": t.string().optional(),
                "renewalPlan": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "edition": t.string().optional(),
                "slotCount": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsDelete"] = bigqueryreservation.post(
        "v1/{parent}/capacityCommitments",
        t.struct(
            {
                "enforceSingleAdminProjectPerOrg": t.boolean().optional(),
                "parent": t.string(),
                "capacityCommitmentId": t.string().optional(),
                "plan": t.string().optional(),
                "renewalPlan": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "edition": t.string().optional(),
                "slotCount": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CapacityCommitmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsCapacityCommitmentsCreate"] = bigqueryreservation.post(
        "v1/{parent}/capacityCommitments",
        t.struct(
            {
                "enforceSingleAdminProjectPerOrg": t.boolean().optional(),
                "parent": t.string(),
                "capacityCommitmentId": t.string().optional(),
                "plan": t.string().optional(),
                "renewalPlan": t.string().optional(),
                "multiRegionAuxiliary": t.boolean().optional(),
                "edition": t.string().optional(),
                "slotCount": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
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
