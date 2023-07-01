from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_bigquerydatatransfer():
    bigquerydatatransfer = HTTPRuntime("https://bigquerydatatransfer.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigquerydatatransfer_1_ErrorResponse",
        "DataSourceParameterIn": "_bigquerydatatransfer_2_DataSourceParameterIn",
        "DataSourceParameterOut": "_bigquerydatatransfer_3_DataSourceParameterOut",
        "ScheduleTransferRunsResponseIn": "_bigquerydatatransfer_4_ScheduleTransferRunsResponseIn",
        "ScheduleTransferRunsResponseOut": "_bigquerydatatransfer_5_ScheduleTransferRunsResponseOut",
        "TimeRangeIn": "_bigquerydatatransfer_6_TimeRangeIn",
        "TimeRangeOut": "_bigquerydatatransfer_7_TimeRangeOut",
        "ListTransferConfigsResponseIn": "_bigquerydatatransfer_8_ListTransferConfigsResponseIn",
        "ListTransferConfigsResponseOut": "_bigquerydatatransfer_9_ListTransferConfigsResponseOut",
        "ScheduleOptionsIn": "_bigquerydatatransfer_10_ScheduleOptionsIn",
        "ScheduleOptionsOut": "_bigquerydatatransfer_11_ScheduleOptionsOut",
        "TransferRunIn": "_bigquerydatatransfer_12_TransferRunIn",
        "TransferRunOut": "_bigquerydatatransfer_13_TransferRunOut",
        "ListTransferRunsResponseIn": "_bigquerydatatransfer_14_ListTransferRunsResponseIn",
        "ListTransferRunsResponseOut": "_bigquerydatatransfer_15_ListTransferRunsResponseOut",
        "StartManualTransferRunsRequestIn": "_bigquerydatatransfer_16_StartManualTransferRunsRequestIn",
        "StartManualTransferRunsRequestOut": "_bigquerydatatransfer_17_StartManualTransferRunsRequestOut",
        "EnrollDataSourcesRequestIn": "_bigquerydatatransfer_18_EnrollDataSourcesRequestIn",
        "EnrollDataSourcesRequestOut": "_bigquerydatatransfer_19_EnrollDataSourcesRequestOut",
        "StartManualTransferRunsResponseIn": "_bigquerydatatransfer_20_StartManualTransferRunsResponseIn",
        "StartManualTransferRunsResponseOut": "_bigquerydatatransfer_21_StartManualTransferRunsResponseOut",
        "UserInfoIn": "_bigquerydatatransfer_22_UserInfoIn",
        "UserInfoOut": "_bigquerydatatransfer_23_UserInfoOut",
        "ListLocationsResponseIn": "_bigquerydatatransfer_24_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_bigquerydatatransfer_25_ListLocationsResponseOut",
        "CheckValidCredsResponseIn": "_bigquerydatatransfer_26_CheckValidCredsResponseIn",
        "CheckValidCredsResponseOut": "_bigquerydatatransfer_27_CheckValidCredsResponseOut",
        "TransferMessageIn": "_bigquerydatatransfer_28_TransferMessageIn",
        "TransferMessageOut": "_bigquerydatatransfer_29_TransferMessageOut",
        "CheckValidCredsRequestIn": "_bigquerydatatransfer_30_CheckValidCredsRequestIn",
        "CheckValidCredsRequestOut": "_bigquerydatatransfer_31_CheckValidCredsRequestOut",
        "LocationIn": "_bigquerydatatransfer_32_LocationIn",
        "LocationOut": "_bigquerydatatransfer_33_LocationOut",
        "DataSourceIn": "_bigquerydatatransfer_34_DataSourceIn",
        "DataSourceOut": "_bigquerydatatransfer_35_DataSourceOut",
        "ListDataSourcesResponseIn": "_bigquerydatatransfer_36_ListDataSourcesResponseIn",
        "ListDataSourcesResponseOut": "_bigquerydatatransfer_37_ListDataSourcesResponseOut",
        "EmailPreferencesIn": "_bigquerydatatransfer_38_EmailPreferencesIn",
        "EmailPreferencesOut": "_bigquerydatatransfer_39_EmailPreferencesOut",
        "EmptyIn": "_bigquerydatatransfer_40_EmptyIn",
        "EmptyOut": "_bigquerydatatransfer_41_EmptyOut",
        "ScheduleTransferRunsRequestIn": "_bigquerydatatransfer_42_ScheduleTransferRunsRequestIn",
        "ScheduleTransferRunsRequestOut": "_bigquerydatatransfer_43_ScheduleTransferRunsRequestOut",
        "ListTransferLogsResponseIn": "_bigquerydatatransfer_44_ListTransferLogsResponseIn",
        "ListTransferLogsResponseOut": "_bigquerydatatransfer_45_ListTransferLogsResponseOut",
        "StatusIn": "_bigquerydatatransfer_46_StatusIn",
        "StatusOut": "_bigquerydatatransfer_47_StatusOut",
        "TransferConfigIn": "_bigquerydatatransfer_48_TransferConfigIn",
        "TransferConfigOut": "_bigquerydatatransfer_49_TransferConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DataSourceParameterIn"] = t.struct(
        {
            "deprecated": t.boolean().optional(),
            "validationHelpUrl": t.string().optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "displayName": t.string().optional(),
            "required": t.boolean().optional(),
            "repeated": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "type": t.string().optional(),
            "recurse": t.boolean().optional(),
            "minValue": t.number().optional(),
            "validationDescription": t.string().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "paramId": t.string().optional(),
            "immutable": t.boolean().optional(),
            "description": t.string().optional(),
            "maxValue": t.number().optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "deprecated": t.boolean().optional(),
            "validationHelpUrl": t.string().optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterOut"])).optional(),
            "displayName": t.string().optional(),
            "required": t.boolean().optional(),
            "repeated": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "type": t.string().optional(),
            "recurse": t.boolean().optional(),
            "minValue": t.number().optional(),
            "validationDescription": t.string().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "paramId": t.string().optional(),
            "immutable": t.boolean().optional(),
            "description": t.string().optional(),
            "maxValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
    types["ScheduleTransferRunsResponseIn"] = t.struct(
        {"runs": t.array(t.proxy(renames["TransferRunIn"])).optional()}
    ).named(renames["ScheduleTransferRunsResponseIn"])
    types["ScheduleTransferRunsResponseOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleTransferRunsResponseOut"])
    types["TimeRangeIn"] = t.struct(
        {"startTime": t.string().optional(), "endTime": t.string().optional()}
    ).named(renames["TimeRangeIn"])
    types["TimeRangeOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeRangeOut"])
    types["ListTransferConfigsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListTransferConfigsResponseIn"])
    types["ListTransferConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transferConfigs": t.array(
                t.proxy(renames["TransferConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTransferConfigsResponseOut"])
    types["ScheduleOptionsIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "disableAutoScheduling": t.boolean().optional(),
        }
    ).named(renames["ScheduleOptionsIn"])
    types["ScheduleOptionsOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "disableAutoScheduling": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOptionsOut"])
    types["TransferRunIn"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
            "runTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["TransferRunIn"])
    types["TransferRunOut"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "startTime": t.string().optional(),
            "destinationDatasetId": t.string().optional(),
            "schedule": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "dataSourceId": t.string().optional(),
            "runTime": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "name": t.string().optional(),
            "endTime": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferRunOut"])
    types["ListTransferRunsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListTransferRunsResponseIn"]
    )
    types["ListTransferRunsResponseOut"] = t.struct(
        {
            "transferRuns": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTransferRunsResponseOut"])
    types["StartManualTransferRunsRequestIn"] = t.struct(
        {
            "requestedRunTime": t.string().optional(),
            "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
        }
    ).named(renames["StartManualTransferRunsRequestIn"])
    types["StartManualTransferRunsRequestOut"] = t.struct(
        {
            "requestedRunTime": t.string().optional(),
            "requestedTimeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartManualTransferRunsRequestOut"])
    types["EnrollDataSourcesRequestIn"] = t.struct(
        {"dataSourceIds": t.array(t.string()).optional()}
    ).named(renames["EnrollDataSourcesRequestIn"])
    types["EnrollDataSourcesRequestOut"] = t.struct(
        {
            "dataSourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollDataSourcesRequestOut"])
    types["StartManualTransferRunsResponseIn"] = t.struct(
        {"runs": t.array(t.proxy(renames["TransferRunIn"])).optional()}
    ).named(renames["StartManualTransferRunsResponseIn"])
    types["StartManualTransferRunsResponseOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartManualTransferRunsResponseOut"])
    types["UserInfoIn"] = t.struct({"email": t.string().optional()}).named(
        renames["UserInfoIn"]
    )
    types["UserInfoOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["CheckValidCredsResponseIn"] = t.struct(
        {"hasValidCreds": t.boolean().optional()}
    ).named(renames["CheckValidCredsResponseIn"])
    types["CheckValidCredsResponseOut"] = t.struct(
        {
            "hasValidCreds": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckValidCredsResponseOut"])
    types["TransferMessageIn"] = t.struct(
        {
            "messageText": t.string().optional(),
            "messageTime": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["TransferMessageIn"])
    types["TransferMessageOut"] = t.struct(
        {
            "messageText": t.string().optional(),
            "messageTime": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferMessageOut"])
    types["CheckValidCredsRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CheckValidCredsRequestIn"]
    )
    types["CheckValidCredsRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CheckValidCredsRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["DataSourceIn"] = t.struct(
        {
            "defaultSchedule": t.string().optional(),
            "clientId": t.string().optional(),
            "dataRefreshType": t.string().optional(),
            "helpUrl": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "parameters": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "supportsCustomSchedule": t.boolean().optional(),
            "scopes": t.array(t.string()).optional(),
            "transferType": t.string().optional(),
            "displayName": t.string().optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "manualRunsDisabled": t.boolean().optional(),
            "supportsMultipleTransfers": t.boolean().optional(),
            "authorizationType": t.string().optional(),
            "description": t.string().optional(),
            "minimumScheduleInterval": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "defaultSchedule": t.string().optional(),
            "clientId": t.string().optional(),
            "name": t.string().optional(),
            "dataRefreshType": t.string().optional(),
            "helpUrl": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["DataSourceParameterOut"])
            ).optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "supportsCustomSchedule": t.boolean().optional(),
            "scopes": t.array(t.string()).optional(),
            "transferType": t.string().optional(),
            "displayName": t.string().optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "manualRunsDisabled": t.boolean().optional(),
            "supportsMultipleTransfers": t.boolean().optional(),
            "authorizationType": t.string().optional(),
            "description": t.string().optional(),
            "minimumScheduleInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["ListDataSourcesResponseIn"] = t.struct(
        {"dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional()}
    ).named(renames["ListDataSourcesResponseIn"])
    types["ListDataSourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "dataSources": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataSourcesResponseOut"])
    types["EmailPreferencesIn"] = t.struct(
        {"enableFailureEmail": t.boolean().optional()}
    ).named(renames["EmailPreferencesIn"])
    types["EmailPreferencesOut"] = t.struct(
        {
            "enableFailureEmail": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailPreferencesOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ScheduleTransferRunsRequestIn"] = t.struct(
        {"startTime": t.string(), "endTime": t.string()}
    ).named(renames["ScheduleTransferRunsRequestIn"])
    types["ScheduleTransferRunsRequestOut"] = t.struct(
        {
            "startTime": t.string(),
            "endTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleTransferRunsRequestOut"])
    types["ListTransferLogsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListTransferLogsResponseIn"]
    )
    types["ListTransferLogsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "transferMessages": t.array(
                t.proxy(renames["TransferMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTransferLogsResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["TransferConfigIn"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "schedule": t.string().optional(),
            "userId": t.string().optional(),
            "displayName": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
            "name": t.string().optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
            "destinationDatasetId": t.string().optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "disabled": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
        }
    ).named(renames["TransferConfigIn"])
    types["TransferConfigOut"] = t.struct(
        {
            "params": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "schedule": t.string().optional(),
            "nextRunTime": t.string().optional(),
            "userId": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "name": t.string().optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsOut"]).optional(),
            "destinationDatasetId": t.string().optional(),
            "datasetRegion": t.string().optional(),
            "ownerInfo": t.proxy(renames["UserInfoOut"]).optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "disabled": t.boolean().optional(),
            "dataSourceId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferConfigOut"])

    functions = {}
    functions["projectsEnrollDataSources"] = bigquerydatatransfer.post(
        "v1/{name}:enrollDataSources",
        t.struct(
            {
                "name": t.string().optional(),
                "dataSourceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = bigquerydatatransfer.post(
        "v1/{name}:enrollDataSources",
        t.struct(
            {
                "name": t.string().optional(),
                "dataSourceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = bigquerydatatransfer.post(
        "v1/{name}:enrollDataSources",
        t.struct(
            {
                "name": t.string().optional(),
                "dataSourceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnrollDataSources"] = bigquerydatatransfer.post(
        "v1/{name}:enrollDataSources",
        t.struct(
            {
                "name": t.string().optional(),
                "dataSourceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataSourcesCheckValidCreds"] = bigquerydatatransfer.get(
        "v1/{parent}/dataSources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataSourcesGet"] = bigquerydatatransfer.get(
        "v1/{parent}/dataSources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataSourcesList"] = bigquerydatatransfer.get(
        "v1/{parent}/dataSources",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsList"] = bigquerydatatransfer.post(
        "v1/{parent}:scheduleRuns",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScheduleTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsPatch"] = bigquerydatatransfer.post(
        "v1/{parent}:scheduleRuns",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScheduleTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsGet"] = bigquerydatatransfer.post(
        "v1/{parent}:scheduleRuns",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScheduleTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsStartManualRuns"
    ] = bigquerydatatransfer.post(
        "v1/{parent}:scheduleRuns",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScheduleTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsDelete"] = bigquerydatatransfer.post(
        "v1/{parent}:scheduleRuns",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScheduleTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsCreate"] = bigquerydatatransfer.post(
        "v1/{parent}:scheduleRuns",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScheduleTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsScheduleRuns"
    ] = bigquerydatatransfer.post(
        "v1/{parent}:scheduleRuns",
        t.struct(
            {
                "parent": t.string(),
                "startTime": t.string(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScheduleTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsDelete"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TransferRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsList"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TransferRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsGet"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TransferRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsRunsTransferLogsList"
    ] = bigquerydatatransfer.get(
        "v1/{parent}/transferLogs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "messageTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsDelete"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsScheduleRuns"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsStartManualRuns"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsGet"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsPatch"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsCreate"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsList"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsGet"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsList"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsDelete"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsTransferLogsList"] = bigquerydatatransfer.get(
        "v1/{parent}/transferLogs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "messageTypes": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDataSourcesCheckValidCreds"] = bigquerydatatransfer.get(
        "v1/{parent}/dataSources",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDataSourcesGet"] = bigquerydatatransfer.get(
        "v1/{parent}/dataSources",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDataSourcesList"] = bigquerydatatransfer.get(
        "v1/{parent}/dataSources",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigquerydatatransfer",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
