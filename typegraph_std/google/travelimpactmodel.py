from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_travelimpactmodel() -> Import:
    travelimpactmodel = HTTPRuntime("https://travelimpactmodel.googleapis.com/")

    renames = {
        "ErrorResponse": "_travelimpactmodel_1_ErrorResponse",
        "ComputeFlightEmissionsRequestIn": "_travelimpactmodel_2_ComputeFlightEmissionsRequestIn",
        "ComputeFlightEmissionsRequestOut": "_travelimpactmodel_3_ComputeFlightEmissionsRequestOut",
        "FlightWithEmissionsIn": "_travelimpactmodel_4_FlightWithEmissionsIn",
        "FlightWithEmissionsOut": "_travelimpactmodel_5_FlightWithEmissionsOut",
        "DateIn": "_travelimpactmodel_6_DateIn",
        "DateOut": "_travelimpactmodel_7_DateOut",
        "ModelVersionIn": "_travelimpactmodel_8_ModelVersionIn",
        "ModelVersionOut": "_travelimpactmodel_9_ModelVersionOut",
        "ComputeFlightEmissionsResponseIn": "_travelimpactmodel_10_ComputeFlightEmissionsResponseIn",
        "ComputeFlightEmissionsResponseOut": "_travelimpactmodel_11_ComputeFlightEmissionsResponseOut",
        "FlightIn": "_travelimpactmodel_12_FlightIn",
        "FlightOut": "_travelimpactmodel_13_FlightOut",
        "EmissionsGramsPerPaxIn": "_travelimpactmodel_14_EmissionsGramsPerPaxIn",
        "EmissionsGramsPerPaxOut": "_travelimpactmodel_15_EmissionsGramsPerPaxOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ComputeFlightEmissionsRequestIn"] = t.struct(
        {"flights": t.array(t.proxy(renames["FlightIn"]))}
    ).named(renames["ComputeFlightEmissionsRequestIn"])
    types["ComputeFlightEmissionsRequestOut"] = t.struct(
        {
            "flights": t.array(t.proxy(renames["FlightOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeFlightEmissionsRequestOut"])
    types["FlightWithEmissionsIn"] = t.struct(
        {
            "flight": t.proxy(renames["FlightIn"]),
            "emissionsGramsPerPax": t.proxy(
                renames["EmissionsGramsPerPaxIn"]
            ).optional(),
        }
    ).named(renames["FlightWithEmissionsIn"])
    types["FlightWithEmissionsOut"] = t.struct(
        {
            "flight": t.proxy(renames["FlightOut"]),
            "emissionsGramsPerPax": t.proxy(
                renames["EmissionsGramsPerPaxOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightWithEmissionsOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ModelVersionIn"] = t.struct(
        {
            "dated": t.string().optional(),
            "minor": t.integer().optional(),
            "major": t.integer().optional(),
            "patch": t.integer().optional(),
        }
    ).named(renames["ModelVersionIn"])
    types["ModelVersionOut"] = t.struct(
        {
            "dated": t.string().optional(),
            "minor": t.integer().optional(),
            "major": t.integer().optional(),
            "patch": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModelVersionOut"])
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
            "flightNumber": t.integer(),
            "operatingCarrierCode": t.string(),
            "departureDate": t.proxy(renames["DateIn"]),
            "origin": t.string(),
            "destination": t.string(),
        }
    ).named(renames["FlightIn"])
    types["FlightOut"] = t.struct(
        {
            "flightNumber": t.integer(),
            "operatingCarrierCode": t.string(),
            "departureDate": t.proxy(renames["DateOut"]),
            "origin": t.string(),
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightOut"])
    types["EmissionsGramsPerPaxIn"] = t.struct(
        {
            "economy": t.integer().optional(),
            "first": t.integer().optional(),
            "premiumEconomy": t.integer().optional(),
            "business": t.integer().optional(),
        }
    ).named(renames["EmissionsGramsPerPaxIn"])
    types["EmissionsGramsPerPaxOut"] = t.struct(
        {
            "economy": t.integer().optional(),
            "first": t.integer().optional(),
            "premiumEconomy": t.integer().optional(),
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
        importer="travelimpactmodel",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
