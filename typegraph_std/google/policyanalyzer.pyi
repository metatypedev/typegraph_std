from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    GoogleCloudPolicyanalyzerV1QueryActivityResponseIn: t.typedef = ...
    GoogleCloudPolicyanalyzerV1QueryActivityResponseOut: t.typedef = ...
    GoogleCloudPolicyanalyzerV1ObservationPeriodIn: t.typedef = ...
    GoogleCloudPolicyanalyzerV1ObservationPeriodOut: t.typedef = ...
    GoogleCloudPolicyanalyzerV1ActivityIn: t.typedef = ...
    GoogleCloudPolicyanalyzerV1ActivityOut: t.typedef = ...

class FuncList:
    projectsLocationsActivityTypesActivitiesQuery: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_policyanalyzer() -> Import: ...
