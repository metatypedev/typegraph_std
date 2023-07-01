from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ComputeFlightEmissionsRequestIn: t.typedef = ...
    ComputeFlightEmissionsRequestOut: t.typedef = ...
    DateIn: t.typedef = ...
    DateOut: t.typedef = ...
    FlightIn: t.typedef = ...
    FlightOut: t.typedef = ...
    ModelVersionIn: t.typedef = ...
    ModelVersionOut: t.typedef = ...
    ComputeFlightEmissionsResponseIn: t.typedef = ...
    ComputeFlightEmissionsResponseOut: t.typedef = ...
    FlightWithEmissionsIn: t.typedef = ...
    FlightWithEmissionsOut: t.typedef = ...
    EmissionsGramsPerPaxIn: t.typedef = ...
    EmissionsGramsPerPaxOut: t.typedef = ...

class FuncList:
    flightsComputeFlightEmissions: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_travelimpactmodel() -> Import: ...
