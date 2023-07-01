from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    SqlserverValidationDetailsIn: t.typedef = ...
    SqlserverValidationDetailsOut: t.typedef = ...
    SapDiscoveryComponentIn: t.typedef = ...
    SapDiscoveryComponentOut: t.typedef = ...
    ListRulesResponseIn: t.typedef = ...
    ListRulesResponseOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    ExecutionIn: t.typedef = ...
    ExecutionOut: t.typedef = ...
    SapValidationIn: t.typedef = ...
    SapValidationOut: t.typedef = ...
    ListExecutionsResponseIn: t.typedef = ...
    ListExecutionsResponseOut: t.typedef = ...
    SqlserverValidationValidationDetailIn: t.typedef = ...
    SqlserverValidationValidationDetailOut: t.typedef = ...
    SapDiscoveryMetadataIn: t.typedef = ...
    SapDiscoveryMetadataOut: t.typedef = ...
    ListExecutionResultsResponseIn: t.typedef = ...
    ListExecutionResultsResponseOut: t.typedef = ...
    SapDiscoveryIn: t.typedef = ...
    SapDiscoveryOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ExecutionResultIn: t.typedef = ...
    ExecutionResultOut: t.typedef = ...
    ViolationDetailsIn: t.typedef = ...
    ViolationDetailsOut: t.typedef = ...
    RunEvaluationRequestIn: t.typedef = ...
    RunEvaluationRequestOut: t.typedef = ...
    SapDiscoveryResourceIn: t.typedef = ...
    SapDiscoveryResourceOut: t.typedef = ...
    WriteInsightRequestIn: t.typedef = ...
    WriteInsightRequestOut: t.typedef = ...
    ListEvaluationsResponseIn: t.typedef = ...
    ListEvaluationsResponseOut: t.typedef = ...
    ScannedResourceIn: t.typedef = ...
    ScannedResourceOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    GceInstanceFilterIn: t.typedef = ...
    GceInstanceFilterOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    SqlserverValidationIn: t.typedef = ...
    SqlserverValidationOut: t.typedef = ...
    ResourceFilterIn: t.typedef = ...
    ResourceFilterOut: t.typedef = ...
    ResourceIn: t.typedef = ...
    ResourceOut: t.typedef = ...
    EvaluationIn: t.typedef = ...
    EvaluationOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    InsightIn: t.typedef = ...
    InsightOut: t.typedef = ...
    WriteInsightResponseIn: t.typedef = ...
    WriteInsightResponseOut: t.typedef = ...
    SapValidationValidationDetailIn: t.typedef = ...
    SapValidationValidationDetailOut: t.typedef = ...
    ListScannedResourcesResponseIn: t.typedef = ...
    ListScannedResourcesResponseOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    ResourceStatusIn: t.typedef = ...
    ResourceStatusOut: t.typedef = ...
    RuleIn: t.typedef = ...
    RuleOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsEvaluationsCreate: t.func = ...
    projectsLocationsEvaluationsGet: t.func = ...
    projectsLocationsEvaluationsList: t.func = ...
    projectsLocationsEvaluationsExecutionsRun: t.func = ...
    projectsLocationsEvaluationsExecutionsGet: t.func = ...
    projectsLocationsEvaluationsExecutionsList: t.func = ...
    projectsLocationsEvaluationsExecutionsScannedResourcesList: t.func = ...
    projectsLocationsEvaluationsExecutionsResultsList: t.func = ...
    projectsLocationsInsightsWriteInsight: t.func = ...
    projectsLocationsRulesList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_workloadmanager() -> Import: ...
