from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_travelimpactmodel():
    travelimpactmodel = HTTPRuntime("https://travelimpactmodel.googleapis.com/")

    renames = {
        "ErrorResponse": "_travelimpactmodel_1_ErrorResponse",
        "ComputeFlightEmissionsRequestIn": "_travelimpactmodel_2_ComputeFlightEmissionsRequestIn",
        "ComputeFlightEmissionsRequestOut": "_travelimpactmodel_3_ComputeFlightEmissionsRequestOut",
        "DateIn": "_travelimpactmodel_4_DateIn",
        "DateOut": "_travelimpactmodel_5_DateOut",
        "FlightIn": "_travelimpactmodel_6_FlightIn",
        "FlightOut": "_travelimpactmodel_7_FlightOut",
        "ModelVersionIn": "_travelimpactmodel_8_ModelVersionIn",
        "ModelVersionOut": "_travelimpactmodel_9_ModelVersionOut",
        "ComputeFlightEmissionsResponseIn": "_travelimpactmodel_10_ComputeFlightEmissionsResponseIn",
        "ComputeFlightEmissionsResponseOut": "_travelimpactmodel_11_ComputeFlightEmissionsResponseOut",
        "FlightWithEmissionsIn": "_travelimpactmodel_12_FlightWithEmissionsIn",
        "FlightWithEmissionsOut": "_travelimpactmodel_13_FlightWithEmissionsOut",
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
    types["FlightIn"] = t.struct(
        {
            "origin": t.string(),
            "operatingCarrierCode": t.string(),
            "destination": t.string(),
            "flightNumber": t.integer(),
            "departureDate": t.proxy(renames["DateIn"]),
        }
    ).named(renames["FlightIn"])
    types["FlightOut"] = t.struct(
        {
            "origin": t.string(),
            "operatingCarrierCode": t.string(),
            "destination": t.string(),
            "flightNumber": t.integer(),
            "departureDate": t.proxy(renames["DateOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlightOut"])
    types["ModelVersionIn"] = t.struct(
        {
            "minor": t.integer().optional(),
            "major": t.integer().optional(),
            "patch": t.integer().optional(),
            "dated": t.string().optional(),
        }
    ).named(renames["ModelVersionIn"])
    types["ModelVersionOut"] = t.struct(
        {
            "minor": t.integer().optional(),
            "major": t.integer().optional(),
            "patch": t.integer().optional(),
            "dated": t.string().optional(),
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
    types["EmissionsGramsPerPaxIn"] = t.struct(
        {
            "first": t.integer().optional(),
            "economy": t.integer().optional(),
            "business": t.integer().optional(),
            "premiumEconomy": t.integer().optional(),
        }
    ).named(renames["EmissionsGramsPerPaxIn"])
    types["EmissionsGramsPerPaxOut"] = t.struct(
        {
            "first": t.integer().optional(),
            "economy": t.integer().optional(),
            "business": t.integer().optional(),
            "premiumEconomy": t.integer().optional(),
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
