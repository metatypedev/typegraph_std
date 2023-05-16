from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_bigquerydatatransfer() -> Import:
    bigquerydatatransfer = HTTPRuntime("https://bigquerydatatransfer.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigquerydatatransfer_1_ErrorResponse",
        "TimeRangeIn": "_bigquerydatatransfer_2_TimeRangeIn",
        "TimeRangeOut": "_bigquerydatatransfer_3_TimeRangeOut",
        "StartManualTransferRunsRequestIn": "_bigquerydatatransfer_4_StartManualTransferRunsRequestIn",
        "StartManualTransferRunsRequestOut": "_bigquerydatatransfer_5_StartManualTransferRunsRequestOut",
        "ScheduleTransferRunsRequestIn": "_bigquerydatatransfer_6_ScheduleTransferRunsRequestIn",
        "ScheduleTransferRunsRequestOut": "_bigquerydatatransfer_7_ScheduleTransferRunsRequestOut",
        "TransferConfigIn": "_bigquerydatatransfer_8_TransferConfigIn",
        "TransferConfigOut": "_bigquerydatatransfer_9_TransferConfigOut",
        "StartManualTransferRunsResponseIn": "_bigquerydatatransfer_10_StartManualTransferRunsResponseIn",
        "StartManualTransferRunsResponseOut": "_bigquerydatatransfer_11_StartManualTransferRunsResponseOut",
        "ListDataSourcesResponseIn": "_bigquerydatatransfer_12_ListDataSourcesResponseIn",
        "ListDataSourcesResponseOut": "_bigquerydatatransfer_13_ListDataSourcesResponseOut",
        "UserInfoIn": "_bigquerydatatransfer_14_UserInfoIn",
        "UserInfoOut": "_bigquerydatatransfer_15_UserInfoOut",
        "DataSourceIn": "_bigquerydatatransfer_16_DataSourceIn",
        "DataSourceOut": "_bigquerydatatransfer_17_DataSourceOut",
        "CheckValidCredsResponseIn": "_bigquerydatatransfer_18_CheckValidCredsResponseIn",
        "CheckValidCredsResponseOut": "_bigquerydatatransfer_19_CheckValidCredsResponseOut",
        "DataSourceParameterIn": "_bigquerydatatransfer_20_DataSourceParameterIn",
        "DataSourceParameterOut": "_bigquerydatatransfer_21_DataSourceParameterOut",
        "CheckValidCredsRequestIn": "_bigquerydatatransfer_22_CheckValidCredsRequestIn",
        "CheckValidCredsRequestOut": "_bigquerydatatransfer_23_CheckValidCredsRequestOut",
        "EmailPreferencesIn": "_bigquerydatatransfer_24_EmailPreferencesIn",
        "EmailPreferencesOut": "_bigquerydatatransfer_25_EmailPreferencesOut",
        "ListTransferConfigsResponseIn": "_bigquerydatatransfer_26_ListTransferConfigsResponseIn",
        "ListTransferConfigsResponseOut": "_bigquerydatatransfer_27_ListTransferConfigsResponseOut",
        "ScheduleOptionsIn": "_bigquerydatatransfer_28_ScheduleOptionsIn",
        "ScheduleOptionsOut": "_bigquerydatatransfer_29_ScheduleOptionsOut",
        "TransferRunIn": "_bigquerydatatransfer_30_TransferRunIn",
        "TransferRunOut": "_bigquerydatatransfer_31_TransferRunOut",
        "ListLocationsResponseIn": "_bigquerydatatransfer_32_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_bigquerydatatransfer_33_ListLocationsResponseOut",
        "TransferMessageIn": "_bigquerydatatransfer_34_TransferMessageIn",
        "TransferMessageOut": "_bigquerydatatransfer_35_TransferMessageOut",
        "ScheduleTransferRunsResponseIn": "_bigquerydatatransfer_36_ScheduleTransferRunsResponseIn",
        "ScheduleTransferRunsResponseOut": "_bigquerydatatransfer_37_ScheduleTransferRunsResponseOut",
        "StatusIn": "_bigquerydatatransfer_38_StatusIn",
        "StatusOut": "_bigquerydatatransfer_39_StatusOut",
        "EnrollDataSourcesRequestIn": "_bigquerydatatransfer_40_EnrollDataSourcesRequestIn",
        "EnrollDataSourcesRequestOut": "_bigquerydatatransfer_41_EnrollDataSourcesRequestOut",
        "ListTransferLogsResponseIn": "_bigquerydatatransfer_42_ListTransferLogsResponseIn",
        "ListTransferLogsResponseOut": "_bigquerydatatransfer_43_ListTransferLogsResponseOut",
        "ListTransferRunsResponseIn": "_bigquerydatatransfer_44_ListTransferRunsResponseIn",
        "ListTransferRunsResponseOut": "_bigquerydatatransfer_45_ListTransferRunsResponseOut",
        "LocationIn": "_bigquerydatatransfer_46_LocationIn",
        "LocationOut": "_bigquerydatatransfer_47_LocationOut",
        "EmptyIn": "_bigquerydatatransfer_48_EmptyIn",
        "EmptyOut": "_bigquerydatatransfer_49_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TransferConfigIn"] = t.struct(
        {
            "schedule": t.string().optional(),
            "disabled": t.boolean().optional(),
            "displayName": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "notificationPubsubTopic": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
            "userId": t.string().optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "name": t.string().optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
            "destinationDatasetId": t.string().optional(),
            "dataSourceId": t.string().optional(),
        }
    ).named(renames["TransferConfigIn"])
    types["TransferConfigOut"] = t.struct(
        {
            "datasetRegion": t.string().optional(),
            "schedule": t.string().optional(),
            "disabled": t.boolean().optional(),
            "displayName": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "notificationPubsubTopic": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "userId": t.string().optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "name": t.string().optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsOut"]).optional(),
            "destinationDatasetId": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "updateTime": t.string().optional(),
            "ownerInfo": t.proxy(renames["UserInfoOut"]).optional(),
            "nextRunTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferConfigOut"])
    types["StartManualTransferRunsResponseIn"] = t.struct(
        {"runs": t.array(t.proxy(renames["TransferRunIn"])).optional()}
    ).named(renames["StartManualTransferRunsResponseIn"])
    types["StartManualTransferRunsResponseOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartManualTransferRunsResponseOut"])
    types["ListDataSourcesResponseIn"] = t.struct(
        {"dataSources": t.array(t.proxy(renames["DataSourceIn"])).optional()}
    ).named(renames["ListDataSourcesResponseIn"])
    types["ListDataSourcesResponseOut"] = t.struct(
        {
            "dataSources": t.array(t.proxy(renames["DataSourceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDataSourcesResponseOut"])
    types["UserInfoIn"] = t.struct({"email": t.string().optional()}).named(
        renames["UserInfoIn"]
    )
    types["UserInfoOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
    types["DataSourceIn"] = t.struct(
        {
            "supportsCustomSchedule": t.boolean().optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "supportsMultipleTransfers": t.boolean().optional(),
            "scopes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "parameters": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "helpUrl": t.string().optional(),
            "clientId": t.string().optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "transferType": t.string().optional(),
            "authorizationType": t.string().optional(),
            "manualRunsDisabled": t.boolean().optional(),
            "minimumScheduleInterval": t.string().optional(),
            "dataRefreshType": t.string().optional(),
            "description": t.string().optional(),
            "defaultSchedule": t.string().optional(),
            "dataSourceId": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "supportsCustomSchedule": t.boolean().optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "supportsMultipleTransfers": t.boolean().optional(),
            "scopes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["DataSourceParameterOut"])
            ).optional(),
            "helpUrl": t.string().optional(),
            "clientId": t.string().optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "transferType": t.string().optional(),
            "authorizationType": t.string().optional(),
            "manualRunsDisabled": t.boolean().optional(),
            "minimumScheduleInterval": t.string().optional(),
            "dataRefreshType": t.string().optional(),
            "description": t.string().optional(),
            "defaultSchedule": t.string().optional(),
            "name": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["CheckValidCredsResponseIn"] = t.struct(
        {"hasValidCreds": t.boolean().optional()}
    ).named(renames["CheckValidCredsResponseIn"])
    types["CheckValidCredsResponseOut"] = t.struct(
        {
            "hasValidCreds": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckValidCredsResponseOut"])
    types["DataSourceParameterIn"] = t.struct(
        {
            "validationHelpUrl": t.string().optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "displayName": t.string().optional(),
            "immutable": t.boolean().optional(),
            "type": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "recurse": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "required": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "paramId": t.string().optional(),
            "minValue": t.number().optional(),
            "validationDescription": t.string().optional(),
            "maxValue": t.number().optional(),
            "description": t.string().optional(),
            "repeated": t.boolean().optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "validationHelpUrl": t.string().optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterOut"])).optional(),
            "displayName": t.string().optional(),
            "immutable": t.boolean().optional(),
            "type": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "recurse": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "required": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "paramId": t.string().optional(),
            "minValue": t.number().optional(),
            "validationDescription": t.string().optional(),
            "maxValue": t.number().optional(),
            "description": t.string().optional(),
            "repeated": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
    types["CheckValidCredsRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CheckValidCredsRequestIn"]
    )
    types["CheckValidCredsRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CheckValidCredsRequestOut"])
    types["EmailPreferencesIn"] = t.struct(
        {"enableFailureEmail": t.boolean().optional()}
    ).named(renames["EmailPreferencesIn"])
    types["EmailPreferencesOut"] = t.struct(
        {
            "enableFailureEmail": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailPreferencesOut"])
    types["ListTransferConfigsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListTransferConfigsResponseIn"])
    types["ListTransferConfigsResponseOut"] = t.struct(
        {
            "transferConfigs": t.array(
                t.proxy(renames["TransferConfigOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTransferConfigsResponseOut"])
    types["ScheduleOptionsIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "disableAutoScheduling": t.boolean().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ScheduleOptionsIn"])
    types["ScheduleOptionsOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "disableAutoScheduling": t.boolean().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOptionsOut"])
    types["TransferRunIn"] = t.struct(
        {
            "name": t.string().optional(),
            "runTime": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
            "userId": t.string().optional(),
            "state": t.string().optional(),
            "scheduleTime": t.string().optional(),
        }
    ).named(renames["TransferRunIn"])
    types["TransferRunOut"] = t.struct(
        {
            "name": t.string().optional(),
            "runTime": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "destinationDatasetId": t.string().optional(),
            "endTime": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "startTime": t.string().optional(),
            "userId": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "schedule": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferRunOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["TransferMessageIn"] = t.struct(
        {
            "messageTime": t.string().optional(),
            "messageText": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["TransferMessageIn"])
    types["TransferMessageOut"] = t.struct(
        {
            "messageTime": t.string().optional(),
            "messageText": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferMessageOut"])
    types["ScheduleTransferRunsResponseIn"] = t.struct(
        {"runs": t.array(t.proxy(renames["TransferRunIn"])).optional()}
    ).named(renames["ScheduleTransferRunsResponseIn"])
    types["ScheduleTransferRunsResponseOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleTransferRunsResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EnrollDataSourcesRequestIn"] = t.struct(
        {"dataSourceIds": t.array(t.string()).optional()}
    ).named(renames["EnrollDataSourcesRequestIn"])
    types["EnrollDataSourcesRequestOut"] = t.struct(
        {
            "dataSourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollDataSourcesRequestOut"])
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
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

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
    functions["projectsTransferConfigsCreate"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsDelete"] = bigquerydatatransfer.get(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "dataSourceIds": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsList"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TransferRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsDelete"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TransferRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsGet"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TransferRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsTransferLogsList"] = bigquerydatatransfer.get(
        "v1/{parent}/transferLogs",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "messageTypes": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferLogsResponseOut"]),
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
    functions[
        "projectsLocationsTransferConfigsScheduleRuns"
    ] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsList"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsCreate"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsGet"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsStartManualRuns"
    ] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsPatch"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsDelete"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
    functions["projectsLocationsTransferConfigsRunsDelete"] = bigquerydatatransfer.get(
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
                "parent": t.string(),
                "messageTypes": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataSourcesCheckValidCreds"] = bigquerydatatransfer.get(
        "v1/{parent}/dataSources",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDataSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDataSourcesCheckValidCreds"] = bigquerydatatransfer.get(
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
    functions["projectsDataSourcesGet"] = bigquerydatatransfer.get(
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
    functions["projectsDataSourcesList"] = bigquerydatatransfer.get(
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

    return Import(
        importer="bigquerydatatransfer",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
