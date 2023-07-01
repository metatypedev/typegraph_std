from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_fitness():
    fitness = HTTPRuntime("https://fitness.googleapis.com/")

    renames = {
        "ErrorResponse": "_fitness_1_ErrorResponse",
        "AggregateByIn": "_fitness_2_AggregateByIn",
        "AggregateByOut": "_fitness_3_AggregateByOut",
        "ListDataPointChangesResponseIn": "_fitness_4_ListDataPointChangesResponseIn",
        "ListDataPointChangesResponseOut": "_fitness_5_ListDataPointChangesResponseOut",
        "SessionIn": "_fitness_6_SessionIn",
        "SessionOut": "_fitness_7_SessionOut",
        "ValueMapValEntryIn": "_fitness_8_ValueMapValEntryIn",
        "ValueMapValEntryOut": "_fitness_9_ValueMapValEntryOut",
        "BucketByTimePeriodIn": "_fitness_10_BucketByTimePeriodIn",
        "BucketByTimePeriodOut": "_fitness_11_BucketByTimePeriodOut",
        "AggregateBucketIn": "_fitness_12_AggregateBucketIn",
        "AggregateBucketOut": "_fitness_13_AggregateBucketOut",
        "AggregateRequestIn": "_fitness_14_AggregateRequestIn",
        "AggregateRequestOut": "_fitness_15_AggregateRequestOut",
        "ListSessionsResponseIn": "_fitness_16_ListSessionsResponseIn",
        "ListSessionsResponseOut": "_fitness_17_ListSessionsResponseOut",
        "ListDataSourcesResponseIn": "_fitness_18_ListDataSourcesResponseIn",
        "ListDataSourcesResponseOut": "_fitness_19_ListDataSourcesResponseOut",
        "DataTypeIn": "_fitness_20_DataTypeIn",
        "DataTypeOut": "_fitness_21_DataTypeOut",
        "BucketByActivityIn": "_fitness_22_BucketByActivityIn",
        "BucketByActivityOut": "_fitness_23_BucketByActivityOut",
        "AggregateResponseIn": "_fitness_24_AggregateResponseIn",
        "AggregateResponseOut": "_fitness_25_AggregateResponseOut",
        "DataPointIn": "_fitness_26_DataPointIn",
        "DataPointOut": "_fitness_27_DataPointOut",
        "ApplicationIn": "_fitness_28_ApplicationIn",
        "ApplicationOut": "_fitness_29_ApplicationOut",
        "MapValueIn": "_fitness_30_MapValueIn",
        "MapValueOut": "_fitness_31_MapValueOut",
        "ValueIn": "_fitness_32_ValueIn",
        "ValueOut": "_fitness_33_ValueOut",
        "DataSourceIn": "_fitness_34_DataSourceIn",
        "DataSourceOut": "_fitness_35_DataSourceOut",
        "DeviceIn": "_fitness_36_DeviceIn",
        "DeviceOut": "_fitness_37_DeviceOut",
        "DatasetIn": "_fitness_38_DatasetIn",
        "DatasetOut": "_fitness_39_DatasetOut",
        "BucketByTimeIn": "_fitness_40_BucketByTimeIn",
        "BucketByTimeOut": "_fitness_41_BucketByTimeOut",
        "BucketBySessionIn": "_fitness_42_BucketBySessionIn",
        "BucketBySessionOut": "_fitness_43_BucketBySessionOut",
        "DataTypeFieldIn": "_fitness_44_DataTypeFieldIn",
        "DataTypeFieldOut": "_fitness_45_DataTypeFieldOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AggregateByIn"] = t.struct(
        {"dataTypeName": t.string().optional(), "dataSourceId": t.string().optional()}
    ).named(renames["AggregateByIn"])
    types["AggregateByOut"] = t.struct(
        {
            "dataTypeName": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateByOut"])
    types["ListDataPointChangesResponseIn"] = t.struct(
        {
            "insertedDataPoint": t.array(t.proxy(renames["DataPointIn"])).optional(),
            "deletedDataPoint": t.array(t.proxy(renames["DataPointIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "dataSourceId": t.string().optional(),
        }
    ).named(renames["ListDataPointChangesResponseIn"])
    types["ListDataPointChangesResponseOut"] = t.struct(
        {
            "insertedDataPoint": t.array(t.proxy(renames["DataPointOut"])).optional(),
            "deletedDataPoint": t.array(t.proxy(renames["DataPointOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataPointChangesResponseOut"])
    types["SessionIn"] = t.struct(
        {
            "startTimeMillis": t.string().optional(),
            "endTimeMillis": t.string().optional(),
            "application": t.proxy(renames["ApplicationIn"]).optional(),
            "activeTimeMillis": t.string().optional(),
            "activityType": t.integer().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SessionIn"])
    types["SessionOut"] = t.struct(
        {
            "startTimeMillis": t.string().optional(),
            "endTimeMillis": t.string().optional(),
            "application": t.proxy(renames["ApplicationOut"]).optional(),
            "activeTimeMillis": t.string().optional(),
            "activityType": t.integer().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOut"])
    types["ValueMapValEntryIn"] = t.struct(
        {"key": t.string(), "value": t.proxy(renames["MapValueIn"])}
    ).named(renames["ValueMapValEntryIn"])
    types["ValueMapValEntryOut"] = t.struct(
        {
            "key": t.string(),
            "value": t.proxy(renames["MapValueOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueMapValEntryOut"])
    types["BucketByTimePeriodIn"] = t.struct(
        {"timeZoneId": t.string().optional(), "value": t.integer(), "type": t.string()}
    ).named(renames["BucketByTimePeriodIn"])
    types["BucketByTimePeriodOut"] = t.struct(
        {
            "timeZoneId": t.string().optional(),
            "value": t.integer(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketByTimePeriodOut"])
    types["AggregateBucketIn"] = t.struct(
        {
            "startTimeMillis": t.string().optional(),
            "session": t.proxy(renames["SessionIn"]).optional(),
            "dataset": t.array(t.proxy(renames["DatasetIn"])).optional(),
            "type": t.string().optional(),
            "endTimeMillis": t.string().optional(),
            "activity": t.integer().optional(),
        }
    ).named(renames["AggregateBucketIn"])
    types["AggregateBucketOut"] = t.struct(
        {
            "startTimeMillis": t.string().optional(),
            "session": t.proxy(renames["SessionOut"]).optional(),
            "dataset": t.array(t.proxy(renames["DatasetOut"])).optional(),
            "type": t.string().optional(),
            "endTimeMillis": t.string().optional(),
            "activity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateBucketOut"])
    types["AggregateRequestIn"] = t.struct(
        {
            "aggregateBy": t.array(t.proxy(renames["AggregateByIn"])).optional(),
            "filteredDataQualityStandard": t.array(t.string()).optional(),
            "bucketByTime": t.proxy(renames["BucketByTimeIn"]).optional(),
            "bucketByActivitySegment": t.proxy(
                renames["BucketByActivityIn"]
            ).optional(),
            "bucketBySession": t.proxy(renames["BucketBySessionIn"]).optional(),
            "bucketByActivityType": t.proxy(renames["BucketByActivityIn"]).optional(),
            "endTimeMillis": t.string().optional(),
            "startTimeMillis": t.string().optional(),
        }
    ).named(renames["AggregateRequestIn"])
    types["AggregateRequestOut"] = t.struct(
        {
            "aggregateBy": t.array(t.proxy(renames["AggregateByOut"])).optional(),
            "filteredDataQualityStandard": t.array(t.string()).optional(),
            "bucketByTime": t.proxy(renames["BucketByTimeOut"]).optional(),
            "bucketByActivitySegment": t.proxy(
                renames["BucketByActivityOut"]
            ).optional(),
            "bucketBySession": t.proxy(renames["BucketBySessionOut"]).optional(),
            "bucketByActivityType": t.proxy(renames["BucketByActivityOut"]).optional(),
            "endTimeMillis": t.string().optional(),
            "startTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateRequestOut"])
    types["ListSessionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deletedSession": t.array(t.proxy(renames["SessionIn"])).optional(),
            "session": t.array(t.proxy(renames["SessionIn"])).optional(),
            "hasMoreData": t.boolean().optional(),
        }
    ).named(renames["ListSessionsResponseIn"])
    types["ListSessionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deletedSession": t.array(t.proxy(renames["SessionOut"])).optional(),
            "session": t.array(t.proxy(renames["SessionOut"])).optional(),
            "hasMoreData": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSessionsResponseOut"])
    types["ListDataSourcesResponseIn"] = t.struct(
        {"dataSource": t.array(t.proxy(renames["DataSourceIn"])).optional()}
    ).named(renames["ListDataSourcesResponseIn"])
    types["ListDataSourcesResponseOut"] = t.struct(
        {
            "dataSource": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataSourcesResponseOut"])
    types["DataTypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "field": t.array(t.proxy(renames["DataTypeFieldIn"])).optional(),
        }
    ).named(renames["DataTypeIn"])
    types["DataTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "field": t.array(t.proxy(renames["DataTypeFieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataTypeOut"])
    types["BucketByActivityIn"] = t.struct(
        {
            "activityDataSourceId": t.string().optional(),
            "minDurationMillis": t.string().optional(),
        }
    ).named(renames["BucketByActivityIn"])
    types["BucketByActivityOut"] = t.struct(
        {
            "activityDataSourceId": t.string().optional(),
            "minDurationMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketByActivityOut"])
    types["AggregateResponseIn"] = t.struct(
        {"bucket": t.array(t.proxy(renames["AggregateBucketIn"])).optional()}
    ).named(renames["AggregateResponseIn"])
    types["AggregateResponseOut"] = t.struct(
        {
            "bucket": t.array(t.proxy(renames["AggregateBucketOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateResponseOut"])
    types["DataPointIn"] = t.struct(
        {
            "dataTypeName": t.string().optional(),
            "endTimeNanos": t.string().optional(),
            "startTimeNanos": t.string().optional(),
            "value": t.array(t.proxy(renames["ValueIn"])).optional(),
            "rawTimestampNanos": t.string().optional(),
            "originDataSourceId": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "computationTimeMillis": t.string().optional(),
        }
    ).named(renames["DataPointIn"])
    types["DataPointOut"] = t.struct(
        {
            "dataTypeName": t.string().optional(),
            "endTimeNanos": t.string().optional(),
            "startTimeNanos": t.string().optional(),
            "value": t.array(t.proxy(renames["ValueOut"])).optional(),
            "rawTimestampNanos": t.string().optional(),
            "originDataSourceId": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "computationTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataPointOut"])
    types["ApplicationIn"] = t.struct(
        {
            "detailsUrl": t.string().optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "detailsUrl": t.string().optional(),
            "name": t.string().optional(),
            "version": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["MapValueIn"] = t.struct({"fpVal": t.number().optional()}).named(
        renames["MapValueIn"]
    )
    types["MapValueOut"] = t.struct(
        {
            "fpVal": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapValueOut"])
    types["ValueIn"] = t.struct(
        {
            "intVal": t.integer().optional(),
            "fpVal": t.number().optional(),
            "stringVal": t.string().optional(),
            "mapVal": t.array(t.proxy(renames["ValueMapValEntryIn"])).optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "intVal": t.integer().optional(),
            "fpVal": t.number().optional(),
            "stringVal": t.string().optional(),
            "mapVal": t.array(t.proxy(renames["ValueMapValEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["DataSourceIn"] = t.struct(
        {
            "dataStreamId": t.string().optional(),
            "dataQualityStandard": t.array(t.string()).optional(),
            "dataType": t.proxy(renames["DataTypeIn"]).optional(),
            "name": t.string().optional(),
            "dataStreamName": t.string().optional(),
            "device": t.proxy(renames["DeviceIn"]).optional(),
            "application": t.proxy(renames["ApplicationIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "dataStreamId": t.string().optional(),
            "dataQualityStandard": t.array(t.string()).optional(),
            "dataType": t.proxy(renames["DataTypeOut"]).optional(),
            "name": t.string().optional(),
            "dataStreamName": t.string().optional(),
            "device": t.proxy(renames["DeviceOut"]).optional(),
            "application": t.proxy(renames["ApplicationOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["DeviceIn"] = t.struct(
        {
            "version": t.string().optional(),
            "model": t.string().optional(),
            "uid": t.string().optional(),
            "manufacturer": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "version": t.string().optional(),
            "model": t.string().optional(),
            "uid": t.string().optional(),
            "manufacturer": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["DatasetIn"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "point": t.array(t.proxy(renames["DataPointIn"])).optional(),
            "minStartTimeNs": t.string().optional(),
            "maxEndTimeNs": t.string().optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "point": t.array(t.proxy(renames["DataPointOut"])).optional(),
            "minStartTimeNs": t.string().optional(),
            "maxEndTimeNs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["BucketByTimeIn"] = t.struct(
        {
            "period": t.proxy(renames["BucketByTimePeriodIn"]),
            "durationMillis": t.string().optional(),
        }
    ).named(renames["BucketByTimeIn"])
    types["BucketByTimeOut"] = t.struct(
        {
            "period": t.proxy(renames["BucketByTimePeriodOut"]),
            "durationMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketByTimeOut"])
    types["BucketBySessionIn"] = t.struct(
        {"minDurationMillis": t.string().optional()}
    ).named(renames["BucketBySessionIn"])
    types["BucketBySessionOut"] = t.struct(
        {
            "minDurationMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketBySessionOut"])
    types["DataTypeFieldIn"] = t.struct(
        {
            "optional": t.boolean(),
            "format": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DataTypeFieldIn"])
    types["DataTypeFieldOut"] = t.struct(
        {
            "optional": t.boolean(),
            "format": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataTypeFieldOut"])

    functions = {}
    functions["usersSessionsUpdate"] = fitness.get(
        "{userId}/sessions",
        t.struct(
            {
                "includeDeleted": t.boolean().optional(),
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "startTime": t.string().optional(),
                "userId": t.string().optional(),
                "activityType": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSessionsDelete"] = fitness.get(
        "{userId}/sessions",
        t.struct(
            {
                "includeDeleted": t.boolean().optional(),
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "startTime": t.string().optional(),
                "userId": t.string().optional(),
                "activityType": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSessionsList"] = fitness.get(
        "{userId}/sessions",
        t.struct(
            {
                "includeDeleted": t.boolean().optional(),
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "startTime": t.string().optional(),
                "userId": t.string().optional(),
                "activityType": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDatasetAggregate"] = fitness.post(
        "{userId}/dataset:aggregate",
        t.struct(
            {
                "userId": t.string().optional(),
                "aggregateBy": t.array(t.proxy(renames["AggregateByIn"])).optional(),
                "filteredDataQualityStandard": t.array(t.string()).optional(),
                "bucketByTime": t.proxy(renames["BucketByTimeIn"]).optional(),
                "bucketByActivitySegment": t.proxy(
                    renames["BucketByActivityIn"]
                ).optional(),
                "bucketBySession": t.proxy(renames["BucketBySessionIn"]).optional(),
                "bucketByActivityType": t.proxy(
                    renames["BucketByActivityIn"]
                ).optional(),
                "endTimeMillis": t.string().optional(),
                "startTimeMillis": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AggregateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesUpdate"] = fitness.get(
        "{userId}/dataSources/{dataSourceId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesCreate"] = fitness.get(
        "{userId}/dataSources/{dataSourceId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDelete"] = fitness.get(
        "{userId}/dataSources/{dataSourceId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesList"] = fitness.get(
        "{userId}/dataSources/{dataSourceId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesGet"] = fitness.get(
        "{userId}/dataSources/{dataSourceId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDatasetsGet"] = fitness.delete(
        "{userId}/dataSources/{dataSourceId}/datasets/{datasetId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDatasetsPatch"] = fitness.delete(
        "{userId}/dataSources/{dataSourceId}/datasets/{datasetId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDatasetsDelete"] = fitness.delete(
        "{userId}/dataSources/{dataSourceId}/datasets/{datasetId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "userId": t.string().optional(),
                "datasetId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDataPointChangesList"] = fitness.get(
        "{userId}/dataSources/{dataSourceId}/dataPointChanges",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "limit": t.integer().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataPointChangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="fitness", renames=renames, types=Box(types), functions=Box(functions)
    )
