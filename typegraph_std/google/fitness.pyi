from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    DatasetIn: t.typedef = ...
    DatasetOut: t.typedef = ...
    ListDataSourcesResponseIn: t.typedef = ...
    ListDataSourcesResponseOut: t.typedef = ...
    DataPointIn: t.typedef = ...
    DataPointOut: t.typedef = ...
    AggregateByIn: t.typedef = ...
    AggregateByOut: t.typedef = ...
    MapValueIn: t.typedef = ...
    MapValueOut: t.typedef = ...
    BucketBySessionIn: t.typedef = ...
    BucketBySessionOut: t.typedef = ...
    SessionIn: t.typedef = ...
    SessionOut: t.typedef = ...
    DataTypeIn: t.typedef = ...
    DataTypeOut: t.typedef = ...
    AggregateBucketIn: t.typedef = ...
    AggregateBucketOut: t.typedef = ...
    ListDataPointChangesResponseIn: t.typedef = ...
    ListDataPointChangesResponseOut: t.typedef = ...
    DataSourceIn: t.typedef = ...
    DataSourceOut: t.typedef = ...
    AggregateRequestIn: t.typedef = ...
    AggregateRequestOut: t.typedef = ...
    ApplicationIn: t.typedef = ...
    ApplicationOut: t.typedef = ...
    ValueIn: t.typedef = ...
    ValueOut: t.typedef = ...
    ValueMapValEntryIn: t.typedef = ...
    ValueMapValEntryOut: t.typedef = ...
    DataTypeFieldIn: t.typedef = ...
    DataTypeFieldOut: t.typedef = ...
    DeviceIn: t.typedef = ...
    DeviceOut: t.typedef = ...
    ListSessionsResponseIn: t.typedef = ...
    ListSessionsResponseOut: t.typedef = ...
    BucketByTimeIn: t.typedef = ...
    BucketByTimeOut: t.typedef = ...
    BucketByTimePeriodIn: t.typedef = ...
    BucketByTimePeriodOut: t.typedef = ...
    BucketByActivityIn: t.typedef = ...
    BucketByActivityOut: t.typedef = ...
    AggregateResponseIn: t.typedef = ...
    AggregateResponseOut: t.typedef = ...

class FuncList:
    usersDataSourcesCreate: t.func = ...
    usersDataSourcesGet: t.func = ...
    usersDataSourcesDelete: t.func = ...
    usersDataSourcesUpdate: t.func = ...
    usersDataSourcesList: t.func = ...
    usersDataSourcesDatasetsDelete: t.func = ...
    usersDataSourcesDatasetsGet: t.func = ...
    usersDataSourcesDatasetsPatch: t.func = ...
    usersDataSourcesDataPointChangesList: t.func = ...
    usersDatasetAggregate: t.func = ...
    usersSessionsDelete: t.func = ...
    usersSessionsUpdate: t.func = ...
    usersSessionsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_fitness() -> Import: ...
