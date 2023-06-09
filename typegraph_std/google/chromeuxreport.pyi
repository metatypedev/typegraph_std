from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    QueryResponseIn: t.typedef = ...
    QueryResponseOut: t.typedef = ...
    CollectionPeriodIn: t.typedef = ...
    CollectionPeriodOut: t.typedef = ...
    QueryHistoryRequestIn: t.typedef = ...
    QueryHistoryRequestOut: t.typedef = ...
    RecordIn: t.typedef = ...
    RecordOut: t.typedef = ...
    HistoryKeyIn: t.typedef = ...
    HistoryKeyOut: t.typedef = ...
    PercentilesIn: t.typedef = ...
    PercentilesOut: t.typedef = ...
    BinIn: t.typedef = ...
    BinOut: t.typedef = ...
    QueryHistoryResponseIn: t.typedef = ...
    QueryHistoryResponseOut: t.typedef = ...
    DateIn: t.typedef = ...
    DateOut: t.typedef = ...
    TimeseriesBinIn: t.typedef = ...
    TimeseriesBinOut: t.typedef = ...
    MetricIn: t.typedef = ...
    MetricOut: t.typedef = ...
    KeyIn: t.typedef = ...
    KeyOut: t.typedef = ...
    UrlNormalizationIn: t.typedef = ...
    UrlNormalizationOut: t.typedef = ...
    MetricTimeseriesIn: t.typedef = ...
    MetricTimeseriesOut: t.typedef = ...
    HistoryRecordIn: t.typedef = ...
    HistoryRecordOut: t.typedef = ...
    TimeseriesPercentilesIn: t.typedef = ...
    TimeseriesPercentilesOut: t.typedef = ...
    QueryRequestIn: t.typedef = ...
    QueryRequestOut: t.typedef = ...

class FuncList:
    recordsQueryHistoryRecord: t.func = ...
    recordsQueryRecord: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_chromeuxreport() -> Import: ...
