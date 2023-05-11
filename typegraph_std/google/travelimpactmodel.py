from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_travelimpactmodel() -> Import:
    travelimpactmodel = HTTPRuntime("https://travelimpactmodel.googleapis.com/")

    renames = {
        "ErrorResponse": "_travelimpactmodel_1_ErrorResponse",
        "FlightWithEmissionsIn": "_travelimpactmodel_2_FlightWithEmissionsIn",
        "FlightWithEmissionsOut": "_travelimpactmodel_3_FlightWithEmissionsOut",
        "ComputeFlightEmissionsRequestIn": "_travelimpactmodel_4_ComputeFlightEmissionsRequestIn",
        "ComputeFlightEmissionsRequestOut": "_travelimpactmodel_5_ComputeFlightEmissionsRequestOut",
        "FlightIn": "_travelimpactmodel_6_FlightIn",
        "FlightOut": "_travelimpactmodel_7_FlightOut",
        "ModelVersionIn": "_travelimpactmodel_8_ModelVersionIn",
        "ModelVersionOut": "_travelimpactmodel_9_ModelVersionOut",
        "ComputeFlightEmissionsResponseIn": "_travelimpactmodel_10_ComputeFlightEmissionsResponseIn",
        "ComputeFlightEmissionsResponseOut": "_travelimpactmodel_11_ComputeFlightEmissionsResponseOut",
        "DateIn": "_travelimpactmodel_12_DateIn",
        "DateOut": "_travelimpactmodel_13_DateOut",
        "EmissionsGramsPerPaxIn": "_travelimpactmodel_14_EmissionsGramsPerPaxIn",
        "EmissionsGramsPerPaxOut": "_travelimpactmodel_15_EmissionsGramsPerPaxOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ComputeFlightEmissionsRequestIn"] = t.struct(
        {"flights": t.array(t.proxy(renames["FlightIn"]))}
    ).named(renames["ComputeFlightEmissionsRequestIn"])
    types["ComputeFlightEmissionsRequestOut"] = t.struct(
        {
            "flights": t.array(t.proxy(renames["FlightOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeFlightEmissionsRequestOut"])
    types["FlightIn"] = t.struct(
        {
            "destination": t.string(),
            "operatingCarrierCode": t.string(),
            "origin": t.string(),
            "departureDate": t.proxy(renames["DateIn"]),
            "flightNumber": t.integer(),
        }
    ).named(renames["FlightIn"])
    types["FlightOut"] = t.struct(
        {
            "destination": t.string(),
            "operatingCarrierCode": t.string(),
            "origin": t.string(),
            "departureDate": t.proxy(renames["DateOut"]),
            "flightNumber": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightOut"])
    types["ModelVersionIn"] = t.struct(
        {
            "major": t.integer().optional(),
            "minor": t.integer().optional(),
            "dated": t.string().optional(),
            "patch": t.integer().optional(),
        }
    ).named(renames["ModelVersionIn"])
    types["ModelVersionOut"] = t.struct(
        {
            "major": t.integer().optional(),
            "minor": t.integer().optional(),
            "dated": t.string().optional(),
            "patch": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelVersionOut"])
    types["ComputeFlightEmissionsResponseIn"] = t.struct(
        {
            "flightEmissions": t.array(
                t.proxy(renames["FlightWithEmissionsIn"])
            ).optional(),
            "modelVersion": t.proxy(renames["ModelVersionIn"]).optional(),
        }
    ).named(renames["ComputeFlightEmissionsResponseIn"])
    types["ComputeFlightEmissionsResponseOut"] = t.struct(
        {
            "flightEmissions": t.array(
                t.proxy(renames["FlightWithEmissionsOut"])
            ).optional(),
            "modelVersion": t.proxy(renames["ModelVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeFlightEmissionsResponseOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["EmissionsGramsPerPaxIn"] = t.struct(
        {
            "premiumEconomy": t.integer().optional(),
            "economy": t.integer().optional(),
            "first": t.integer().optional(),
            "business": t.integer().optional(),
        }
    ).named(renames["EmissionsGramsPerPaxIn"])
    types["EmissionsGramsPerPaxOut"] = t.struct(
        {
            "premiumEconomy": t.integer().optional(),
            "economy": t.integer().optional(),
            "first": t.integer().optional(),
            "business": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmissionsGramsPerPaxOut"])

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
        importer="travelimpactmodel", renames=renames, types=types, functions=functions
    )
