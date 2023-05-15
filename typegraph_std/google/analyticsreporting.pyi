from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SegmentSequenceStepIn: t.typedef = ...
    SegmentSequenceStepOut: t.typedef = ...
    SearchUserActivityResponseIn: t.typedef = ...
    SearchUserActivityResponseOut: t.typedef = ...
    PivotIn: t.typedef = ...
    PivotOut: t.typedef = ...
    EcommerceDataIn: t.typedef = ...
    EcommerceDataOut: t.typedef = ...
    TransactionDataIn: t.typedef = ...
    TransactionDataOut: t.typedef = ...
    SegmentDefinitionIn: t.typedef = ...
    SegmentDefinitionOut: t.typedef = ...
    UserIn: t.typedef = ...
    UserOut: t.typedef = ...
    DimensionIn: t.typedef = ...
    DimensionOut: t.typedef = ...
    UserActivitySessionIn: t.typedef = ...
    UserActivitySessionOut: t.typedef = ...
    ActivityIn: t.typedef = ...
    ActivityOut: t.typedef = ...
    MetricFilterIn: t.typedef = ...
    MetricFilterOut: t.typedef = ...
    PivotValueRegionIn: t.typedef = ...
    PivotValueRegionOut: t.typedef = ...
    ReportIn: t.typedef = ...
    ReportOut: t.typedef = ...
    GetReportsResponseIn: t.typedef = ...
    GetReportsResponseOut: t.typedef = ...
    CohortGroupIn: t.typedef = ...
    CohortGroupOut: t.typedef = ...
    PivotHeaderIn: t.typedef = ...
    PivotHeaderOut: t.typedef = ...
    GetReportsRequestIn: t.typedef = ...
    GetReportsRequestOut: t.typedef = ...
    CustomDimensionIn: t.typedef = ...
    CustomDimensionOut: t.typedef = ...
    MetricFilterClauseIn: t.typedef = ...
    MetricFilterClauseOut: t.typedef = ...
    ColumnHeaderIn: t.typedef = ...
    ColumnHeaderOut: t.typedef = ...
    ScreenviewDataIn: t.typedef = ...
    ScreenviewDataOut: t.typedef = ...
    DateRangeValuesIn: t.typedef = ...
    DateRangeValuesOut: t.typedef = ...
    ReportRowIn: t.typedef = ...
    ReportRowOut: t.typedef = ...
    ProductDataIn: t.typedef = ...
    ProductDataOut: t.typedef = ...
    SequenceSegmentIn: t.typedef = ...
    SequenceSegmentOut: t.typedef = ...
    SegmentMetricFilterIn: t.typedef = ...
    SegmentMetricFilterOut: t.typedef = ...
    PageviewDataIn: t.typedef = ...
    PageviewDataOut: t.typedef = ...
    CohortIn: t.typedef = ...
    CohortOut: t.typedef = ...
    SimpleSegmentIn: t.typedef = ...
    SimpleSegmentOut: t.typedef = ...
    ResourceQuotasRemainingIn: t.typedef = ...
    ResourceQuotasRemainingOut: t.typedef = ...
    SearchUserActivityRequestIn: t.typedef = ...
    SearchUserActivityRequestOut: t.typedef = ...
    MetricHeaderIn: t.typedef = ...
    MetricHeaderOut: t.typedef = ...
    OrderByIn: t.typedef = ...
    OrderByOut: t.typedef = ...
    DateRangeIn: t.typedef = ...
    DateRangeOut: t.typedef = ...
    GoalSetDataIn: t.typedef = ...
    GoalSetDataOut: t.typedef = ...
    DynamicSegmentIn: t.typedef = ...
    DynamicSegmentOut: t.typedef = ...
    OrFiltersForSegmentIn: t.typedef = ...
    OrFiltersForSegmentOut: t.typedef = ...
    SegmentDimensionFilterIn: t.typedef = ...
    SegmentDimensionFilterOut: t.typedef = ...
    DimensionFilterClauseIn: t.typedef = ...
    DimensionFilterClauseOut: t.typedef = ...
    MetricIn: t.typedef = ...
    MetricOut: t.typedef = ...
    SegmentFilterIn: t.typedef = ...
    SegmentFilterOut: t.typedef = ...
    ReportDataIn: t.typedef = ...
    ReportDataOut: t.typedef = ...
    EventDataIn: t.typedef = ...
    EventDataOut: t.typedef = ...
    DimensionFilterIn: t.typedef = ...
    DimensionFilterOut: t.typedef = ...
    SegmentIn: t.typedef = ...
    SegmentOut: t.typedef = ...
    GoalDataIn: t.typedef = ...
    GoalDataOut: t.typedef = ...
    PivotHeaderEntryIn: t.typedef = ...
    PivotHeaderEntryOut: t.typedef = ...
    ReportRequestIn: t.typedef = ...
    ReportRequestOut: t.typedef = ...
    SegmentFilterClauseIn: t.typedef = ...
    SegmentFilterClauseOut: t.typedef = ...
    MetricHeaderEntryIn: t.typedef = ...
    MetricHeaderEntryOut: t.typedef = ...

class FuncList:
    userActivitySearch: t.func = ...
    reportsBatchGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_analyticsreporting() -> Import: ...