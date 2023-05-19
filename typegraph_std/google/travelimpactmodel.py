from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_travelimpactmodel() -> Import:
    travelimpactmodel = HTTPRuntime("https://travelimpactmodel.googleapis.com/")

    renames = {
        "ErrorResponse": "_travelimpactmodel_1_ErrorResponse",
        "EmissionsGramsPerPaxIn": "_travelimpactmodel_2_EmissionsGramsPerPaxIn",
        "EmissionsGramsPerPaxOut": "_travelimpactmodel_3_EmissionsGramsPerPaxOut",
        "FlightWithEmissionsIn": "_travelimpactmodel_4_FlightWithEmissionsIn",
        "FlightWithEmissionsOut": "_travelimpactmodel_5_FlightWithEmissionsOut",
        "ComputeFlightEmissionsResponseIn": "_travelimpactmodel_6_ComputeFlightEmissionsResponseIn",
        "ComputeFlightEmissionsResponseOut": "_travelimpactmodel_7_ComputeFlightEmissionsResponseOut",
        "FlightIn": "_travelimpactmodel_8_FlightIn",
        "FlightOut": "_travelimpactmodel_9_FlightOut",
        "DateIn": "_travelimpactmodel_10_DateIn",
        "DateOut": "_travelimpactmodel_11_DateOut",
        "ModelVersionIn": "_travelimpactmodel_12_ModelVersionIn",
        "ModelVersionOut": "_travelimpactmodel_13_ModelVersionOut",
        "ComputeFlightEmissionsRequestIn": "_travelimpactmodel_14_ComputeFlightEmissionsRequestIn",
        "ComputeFlightEmissionsRequestOut": "_travelimpactmodel_15_ComputeFlightEmissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmissionsGramsPerPaxIn"] = t.struct(
        {
            "first": t.integer().optional(),
            "business": t.integer().optional(),
            "premiumEconomy": t.integer().optional(),
            "economy": t.integer().optional(),
        }
    ).named(renames["EmissionsGramsPerPaxIn"])
    types["EmissionsGramsPerPaxOut"] = t.struct(
        {
            "first": t.integer().optional(),
            "business": t.integer().optional(),
            "premiumEconomy": t.integer().optional(),
            "economy": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmissionsGramsPerPaxOut"])
    types["FlightWithEmissionsIn"] = t.struct(
        {
            "emissionsGramsPerPax": t.proxy(
                renames["EmissionsGramsPerPaxIn"]
            ).optional(),
            "flight": t.proxy(renames["FlightIn"]),
        }
    ).named(renames["FlightWithEmissionsIn"])
    types["FlightWithEmissionsOut"] = t.struct(
        {
            "emissionsGramsPerPax": t.proxy(
                renames["EmissionsGramsPerPaxOut"]
            ).optional(),
            "flight": t.proxy(renames["FlightOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightWithEmissionsOut"])
    types["ComputeFlightEmissionsResponseIn"] = t.struct(
        {
            "modelVersion": t.proxy(renames["ModelVersionIn"]).optional(),
            "flightEmissions": t.array(
                t.proxy(renames["FlightWithEmissionsIn"])
            ).optional(),
        }
    ).named(renames["ComputeFlightEmissionsResponseIn"])
    types["ComputeFlightEmissionsResponseOut"] = t.struct(
        {
            "modelVersion": t.proxy(renames["ModelVersionOut"]).optional(),
            "flightEmissions": t.array(
                t.proxy(renames["FlightWithEmissionsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeFlightEmissionsResponseOut"])
    types["FlightIn"] = t.struct(
        {
            "destination": t.string(),
            "flightNumber": t.integer(),
            "origin": t.string(),
            "operatingCarrierCode": t.string(),
            "departureDate": t.proxy(renames["DateIn"]),
        }
    ).named(renames["FlightIn"])
    types["FlightOut"] = t.struct(
        {
            "destination": t.string(),
            "flightNumber": t.integer(),
            "origin": t.string(),
            "operatingCarrierCode": t.string(),
            "departureDate": t.proxy(renames["DateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ModelVersionIn"] = t.struct(
        {
            "dated": t.string().optional(),
            "patch": t.integer().optional(),
            "major": t.integer().optional(),
            "minor": t.integer().optional(),
        }
    ).named(renames["ModelVersionIn"])
    types["ModelVersionOut"] = t.struct(
        {
            "dated": t.string().optional(),
            "patch": t.integer().optional(),
            "major": t.integer().optional(),
            "minor": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelVersionOut"])
    types["ComputeFlightEmissionsRequestIn"] = t.struct(
        {"flights": t.array(t.proxy(renames["FlightIn"]))}
    ).named(renames["ComputeFlightEmissionsRequestIn"])
    types["ComputeFlightEmissionsRequestOut"] = t.struct(
        {
            "flights": t.array(t.proxy(renames["FlightOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeFlightEmissionsRequestOut"])

    functions = {}
    functions["flightsComputeFlightEmissions"] = travelimpactmodel.post(
        "v1/flights:computeFlightEmissions",
        t.struct(
            {
                "flights": t.array(t.proxy(renames["FlightIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ComputeFlightEmissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="travelimpactmodel",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
