from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_fitness() -> Import:
    fitness = HTTPRuntime("https://fitness.googleapis.com/")

    renames = {
        "ErrorResponse": "_fitness_1_ErrorResponse",
        "DatasetIn": "_fitness_2_DatasetIn",
        "DatasetOut": "_fitness_3_DatasetOut",
        "ListDataSourcesResponseIn": "_fitness_4_ListDataSourcesResponseIn",
        "ListDataSourcesResponseOut": "_fitness_5_ListDataSourcesResponseOut",
        "DataPointIn": "_fitness_6_DataPointIn",
        "DataPointOut": "_fitness_7_DataPointOut",
        "AggregateByIn": "_fitness_8_AggregateByIn",
        "AggregateByOut": "_fitness_9_AggregateByOut",
        "MapValueIn": "_fitness_10_MapValueIn",
        "MapValueOut": "_fitness_11_MapValueOut",
        "BucketBySessionIn": "_fitness_12_BucketBySessionIn",
        "BucketBySessionOut": "_fitness_13_BucketBySessionOut",
        "SessionIn": "_fitness_14_SessionIn",
        "SessionOut": "_fitness_15_SessionOut",
        "DataTypeIn": "_fitness_16_DataTypeIn",
        "DataTypeOut": "_fitness_17_DataTypeOut",
        "AggregateBucketIn": "_fitness_18_AggregateBucketIn",
        "AggregateBucketOut": "_fitness_19_AggregateBucketOut",
        "ListDataPointChangesResponseIn": "_fitness_20_ListDataPointChangesResponseIn",
        "ListDataPointChangesResponseOut": "_fitness_21_ListDataPointChangesResponseOut",
        "DataSourceIn": "_fitness_22_DataSourceIn",
        "DataSourceOut": "_fitness_23_DataSourceOut",
        "AggregateRequestIn": "_fitness_24_AggregateRequestIn",
        "AggregateRequestOut": "_fitness_25_AggregateRequestOut",
        "ApplicationIn": "_fitness_26_ApplicationIn",
        "ApplicationOut": "_fitness_27_ApplicationOut",
        "ValueIn": "_fitness_28_ValueIn",
        "ValueOut": "_fitness_29_ValueOut",
        "ValueMapValEntryIn": "_fitness_30_ValueMapValEntryIn",
        "ValueMapValEntryOut": "_fitness_31_ValueMapValEntryOut",
        "DataTypeFieldIn": "_fitness_32_DataTypeFieldIn",
        "DataTypeFieldOut": "_fitness_33_DataTypeFieldOut",
        "DeviceIn": "_fitness_34_DeviceIn",
        "DeviceOut": "_fitness_35_DeviceOut",
        "ListSessionsResponseIn": "_fitness_36_ListSessionsResponseIn",
        "ListSessionsResponseOut": "_fitness_37_ListSessionsResponseOut",
        "BucketByTimeIn": "_fitness_38_BucketByTimeIn",
        "BucketByTimeOut": "_fitness_39_BucketByTimeOut",
        "BucketByTimePeriodIn": "_fitness_40_BucketByTimePeriodIn",
        "BucketByTimePeriodOut": "_fitness_41_BucketByTimePeriodOut",
        "BucketByActivityIn": "_fitness_42_BucketByActivityIn",
        "BucketByActivityOut": "_fitness_43_BucketByActivityOut",
        "AggregateResponseIn": "_fitness_44_AggregateResponseIn",
        "AggregateResponseOut": "_fitness_45_AggregateResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DatasetIn"] = t.struct(
        {
            "minStartTimeNs": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "maxEndTimeNs": t.string().optional(),
            "point": t.array(t.proxy(renames["DataPointIn"])).optional(),
        }
    ).named(renames["DatasetIn"])
    types["DatasetOut"] = t.struct(
        {
            "minStartTimeNs": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "maxEndTimeNs": t.string().optional(),
            "point": t.array(t.proxy(renames["DataPointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatasetOut"])
    types["ListDataSourcesResponseIn"] = t.struct(
        {"dataSource": t.array(t.proxy(renames["DataSourceIn"])).optional()}
    ).named(renames["ListDataSourcesResponseIn"])
    types["ListDataSourcesResponseOut"] = t.struct(
        {
            "dataSource": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataSourcesResponseOut"])
    types["DataPointIn"] = t.struct(
        {
            "dataTypeName": t.string().optional(),
            "value": t.array(t.proxy(renames["ValueIn"])).optional(),
            "startTimeNanos": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "endTimeNanos": t.string().optional(),
            "rawTimestampNanos": t.string().optional(),
            "originDataSourceId": t.string().optional(),
            "computationTimeMillis": t.string().optional(),
        }
    ).named(renames["DataPointIn"])
    types["DataPointOut"] = t.struct(
        {
            "dataTypeName": t.string().optional(),
            "value": t.array(t.proxy(renames["ValueOut"])).optional(),
            "startTimeNanos": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "endTimeNanos": t.string().optional(),
            "rawTimestampNanos": t.string().optional(),
            "originDataSourceId": t.string().optional(),
            "computationTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataPointOut"])
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
    types["MapValueIn"] = t.struct({"fpVal": t.number().optional()}).named(
        renames["MapValueIn"]
    )
    types["MapValueOut"] = t.struct(
        {
            "fpVal": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MapValueOut"])
    types["BucketBySessionIn"] = t.struct(
        {"minDurationMillis": t.string().optional()}
    ).named(renames["BucketBySessionIn"])
    types["BucketBySessionOut"] = t.struct(
        {
            "minDurationMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketBySessionOut"])
    types["SessionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "activityType": t.integer().optional(),
            "description": t.string().optional(),
            "application": t.proxy(renames["ApplicationIn"]).optional(),
            "activeTimeMillis": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "endTimeMillis": t.string().optional(),
            "startTimeMillis": t.string().optional(),
        }
    ).named(renames["SessionIn"])
    types["SessionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "activityType": t.integer().optional(),
            "description": t.string().optional(),
            "application": t.proxy(renames["ApplicationOut"]).optional(),
            "activeTimeMillis": t.string().optional(),
            "modifiedTimeMillis": t.string().optional(),
            "endTimeMillis": t.string().optional(),
            "startTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SessionOut"])
    types["DataTypeIn"] = t.struct(
        {
            "field": t.array(t.proxy(renames["DataTypeFieldIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DataTypeIn"])
    types["DataTypeOut"] = t.struct(
        {
            "field": t.array(t.proxy(renames["DataTypeFieldOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataTypeOut"])
    types["AggregateBucketIn"] = t.struct(
        {
            "endTimeMillis": t.string().optional(),
            "type": t.string().optional(),
            "session": t.proxy(renames["SessionIn"]).optional(),
            "activity": t.integer().optional(),
            "dataset": t.array(t.proxy(renames["DatasetIn"])).optional(),
            "startTimeMillis": t.string().optional(),
        }
    ).named(renames["AggregateBucketIn"])
    types["AggregateBucketOut"] = t.struct(
        {
            "endTimeMillis": t.string().optional(),
            "type": t.string().optional(),
            "session": t.proxy(renames["SessionOut"]).optional(),
            "activity": t.integer().optional(),
            "dataset": t.array(t.proxy(renames["DatasetOut"])).optional(),
            "startTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateBucketOut"])
    types["ListDataPointChangesResponseIn"] = t.struct(
        {
            "insertedDataPoint": t.array(t.proxy(renames["DataPointIn"])).optional(),
            "dataSourceId": t.string().optional(),
            "deletedDataPoint": t.array(t.proxy(renames["DataPointIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDataPointChangesResponseIn"])
    types["ListDataPointChangesResponseOut"] = t.struct(
        {
            "insertedDataPoint": t.array(t.proxy(renames["DataPointOut"])).optional(),
            "dataSourceId": t.string().optional(),
            "deletedDataPoint": t.array(t.proxy(renames["DataPointOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataPointChangesResponseOut"])
    types["DataSourceIn"] = t.struct(
        {
            "type": t.string().optional(),
            "application": t.proxy(renames["ApplicationIn"]).optional(),
            "name": t.string().optional(),
            "dataQualityStandard": t.array(t.string()).optional(),
            "dataStreamName": t.string().optional(),
            "device": t.proxy(renames["DeviceIn"]).optional(),
            "dataType": t.proxy(renames["DataTypeIn"]).optional(),
            "dataStreamId": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "application": t.proxy(renames["ApplicationOut"]).optional(),
            "name": t.string().optional(),
            "dataQualityStandard": t.array(t.string()).optional(),
            "dataStreamName": t.string().optional(),
            "device": t.proxy(renames["DeviceOut"]).optional(),
            "dataType": t.proxy(renames["DataTypeOut"]).optional(),
            "dataStreamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["AggregateRequestIn"] = t.struct(
        {
            "filteredDataQualityStandard": t.array(t.string()).optional(),
            "bucketByActivitySegment": t.proxy(
                renames["BucketByActivityIn"]
            ).optional(),
            "bucketBySession": t.proxy(renames["BucketBySessionIn"]).optional(),
            "endTimeMillis": t.string().optional(),
            "aggregateBy": t.array(t.proxy(renames["AggregateByIn"])).optional(),
            "bucketByActivityType": t.proxy(renames["BucketByActivityIn"]).optional(),
            "bucketByTime": t.proxy(renames["BucketByTimeIn"]).optional(),
            "startTimeMillis": t.string().optional(),
        }
    ).named(renames["AggregateRequestIn"])
    types["AggregateRequestOut"] = t.struct(
        {
            "filteredDataQualityStandard": t.array(t.string()).optional(),
            "bucketByActivitySegment": t.proxy(
                renames["BucketByActivityOut"]
            ).optional(),
            "bucketBySession": t.proxy(renames["BucketBySessionOut"]).optional(),
            "endTimeMillis": t.string().optional(),
            "aggregateBy": t.array(t.proxy(renames["AggregateByOut"])).optional(),
            "bucketByActivityType": t.proxy(renames["BucketByActivityOut"]).optional(),
            "bucketByTime": t.proxy(renames["BucketByTimeOut"]).optional(),
            "startTimeMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AggregateRequestOut"])
    types["ApplicationIn"] = t.struct(
        {
            "version": t.string().optional(),
            "detailsUrl": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "version": t.string().optional(),
            "detailsUrl": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["ValueIn"] = t.struct(
        {
            "stringVal": t.string().optional(),
            "mapVal": t.array(t.proxy(renames["ValueMapValEntryIn"])).optional(),
            "fpVal": t.number().optional(),
            "intVal": t.integer().optional(),
        }
    ).named(renames["ValueIn"])
    types["ValueOut"] = t.struct(
        {
            "stringVal": t.string().optional(),
            "mapVal": t.array(t.proxy(renames["ValueMapValEntryOut"])).optional(),
            "fpVal": t.number().optional(),
            "intVal": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueOut"])
    types["ValueMapValEntryIn"] = t.struct(
        {"value": t.proxy(renames["MapValueIn"]), "key": t.string()}
    ).named(renames["ValueMapValEntryIn"])
    types["ValueMapValEntryOut"] = t.struct(
        {
            "value": t.proxy(renames["MapValueOut"]),
            "key": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueMapValEntryOut"])
    types["DataTypeFieldIn"] = t.struct(
        {
            "name": t.string().optional(),
            "optional": t.boolean(),
            "format": t.string().optional(),
        }
    ).named(renames["DataTypeFieldIn"])
    types["DataTypeFieldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "optional": t.boolean(),
            "format": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataTypeFieldOut"])
    types["DeviceIn"] = t.struct(
        {
            "version": t.string().optional(),
            "type": t.string().optional(),
            "uid": t.string().optional(),
            "model": t.string().optional(),
            "manufacturer": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "version": t.string().optional(),
            "type": t.string().optional(),
            "uid": t.string().optional(),
            "model": t.string().optional(),
            "manufacturer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["ListSessionsResponseIn"] = t.struct(
        {
            "deletedSession": t.array(t.proxy(renames["SessionIn"])).optional(),
            "hasMoreData": t.boolean().optional(),
            "nextPageToken": t.string().optional(),
            "session": t.array(t.proxy(renames["SessionIn"])).optional(),
        }
    ).named(renames["ListSessionsResponseIn"])
    types["ListSessionsResponseOut"] = t.struct(
        {
            "deletedSession": t.array(t.proxy(renames["SessionOut"])).optional(),
            "hasMoreData": t.boolean().optional(),
            "nextPageToken": t.string().optional(),
            "session": t.array(t.proxy(renames["SessionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSessionsResponseOut"])
    types["BucketByTimeIn"] = t.struct(
        {
            "durationMillis": t.string().optional(),
            "period": t.proxy(renames["BucketByTimePeriodIn"]),
        }
    ).named(renames["BucketByTimeIn"])
    types["BucketByTimeOut"] = t.struct(
        {
            "durationMillis": t.string().optional(),
            "period": t.proxy(renames["BucketByTimePeriodOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketByTimeOut"])
    types["BucketByTimePeriodIn"] = t.struct(
        {"type": t.string(), "timeZoneId": t.string().optional(), "value": t.integer()}
    ).named(renames["BucketByTimePeriodIn"])
    types["BucketByTimePeriodOut"] = t.struct(
        {
            "type": t.string(),
            "timeZoneId": t.string().optional(),
            "value": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketByTimePeriodOut"])
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

    functions = {}
    functions["usersDataSourcesCreate"] = fitness.get(
        "{userId}/dataSources",
        t.struct(
            {
                "userId": t.string().optional(),
                "dataTypeName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesGet"] = fitness.get(
        "{userId}/dataSources",
        t.struct(
            {
                "userId": t.string().optional(),
                "dataTypeName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDelete"] = fitness.get(
        "{userId}/dataSources",
        t.struct(
            {
                "userId": t.string().optional(),
                "dataTypeName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesUpdate"] = fitness.get(
        "{userId}/dataSources",
        t.struct(
            {
                "userId": t.string().optional(),
                "dataTypeName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesList"] = fitness.get(
        "{userId}/dataSources",
        t.struct(
            {
                "userId": t.string().optional(),
                "dataTypeName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDatasetsDelete"] = fitness.patch(
        "{userId}/dataSources/{dataSourceId}/datasets/{datasetId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "datasetId": t.string().optional(),
                "userId": t.string().optional(),
                "minStartTimeNs": t.string().optional(),
                "nextPageToken": t.string().optional(),
                "maxEndTimeNs": t.string().optional(),
                "point": t.array(t.proxy(renames["DataPointIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDatasetsGet"] = fitness.patch(
        "{userId}/dataSources/{dataSourceId}/datasets/{datasetId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "datasetId": t.string().optional(),
                "userId": t.string().optional(),
                "minStartTimeNs": t.string().optional(),
                "nextPageToken": t.string().optional(),
                "maxEndTimeNs": t.string().optional(),
                "point": t.array(t.proxy(renames["DataPointIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDatasetsPatch"] = fitness.patch(
        "{userId}/dataSources/{dataSourceId}/datasets/{datasetId}",
        t.struct(
            {
                "dataSourceId": t.string().optional(),
                "datasetId": t.string().optional(),
                "userId": t.string().optional(),
                "minStartTimeNs": t.string().optional(),
                "nextPageToken": t.string().optional(),
                "maxEndTimeNs": t.string().optional(),
                "point": t.array(t.proxy(renames["DataPointIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatasetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDataSourcesDataPointChangesList"] = fitness.get(
        "{userId}/dataSources/{dataSourceId}/dataPointChanges",
        t.struct(
            {
                "limit": t.integer().optional(),
                "userId": t.string().optional(),
                "pageToken": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataPointChangesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDatasetAggregate"] = fitness.post(
        "{userId}/dataset:aggregate",
        t.struct(
            {
                "userId": t.string().optional(),
                "filteredDataQualityStandard": t.array(t.string()).optional(),
                "bucketByActivitySegment": t.proxy(
                    renames["BucketByActivityIn"]
                ).optional(),
                "bucketBySession": t.proxy(renames["BucketBySessionIn"]).optional(),
                "endTimeMillis": t.string().optional(),
                "aggregateBy": t.array(t.proxy(renames["AggregateByIn"])).optional(),
                "bucketByActivityType": t.proxy(
                    renames["BucketByActivityIn"]
                ).optional(),
                "bucketByTime": t.proxy(renames["BucketByTimeIn"]).optional(),
                "startTimeMillis": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AggregateResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSessionsDelete"] = fitness.get(
        "{userId}/sessions",
        t.struct(
            {
                "userId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
                "activityType": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSessionsUpdate"] = fitness.get(
        "{userId}/sessions",
        t.struct(
            {
                "userId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
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
                "userId": t.string().optional(),
                "includeDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "endTime": t.string().optional(),
                "startTime": t.string().optional(),
                "activityType": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSessionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="fitness", renames=renames, types=Box(types), functions=Box(functions)
    )
