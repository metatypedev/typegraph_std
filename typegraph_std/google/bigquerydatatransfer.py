from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_bigquerydatatransfer() -> Import:
    bigquerydatatransfer = HTTPRuntime("https://bigquerydatatransfer.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigquerydatatransfer_1_ErrorResponse",
        "ListTransferLogsResponseIn": "_bigquerydatatransfer_2_ListTransferLogsResponseIn",
        "ListTransferLogsResponseOut": "_bigquerydatatransfer_3_ListTransferLogsResponseOut",
        "ScheduleTransferRunsRequestIn": "_bigquerydatatransfer_4_ScheduleTransferRunsRequestIn",
        "ScheduleTransferRunsRequestOut": "_bigquerydatatransfer_5_ScheduleTransferRunsRequestOut",
        "ListLocationsResponseIn": "_bigquerydatatransfer_6_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_bigquerydatatransfer_7_ListLocationsResponseOut",
        "TransferRunIn": "_bigquerydatatransfer_8_TransferRunIn",
        "TransferRunOut": "_bigquerydatatransfer_9_TransferRunOut",
        "UserInfoIn": "_bigquerydatatransfer_10_UserInfoIn",
        "UserInfoOut": "_bigquerydatatransfer_11_UserInfoOut",
        "DataSourceIn": "_bigquerydatatransfer_12_DataSourceIn",
        "DataSourceOut": "_bigquerydatatransfer_13_DataSourceOut",
        "StartManualTransferRunsRequestIn": "_bigquerydatatransfer_14_StartManualTransferRunsRequestIn",
        "StartManualTransferRunsRequestOut": "_bigquerydatatransfer_15_StartManualTransferRunsRequestOut",
        "ListDataSourcesResponseIn": "_bigquerydatatransfer_16_ListDataSourcesResponseIn",
        "ListDataSourcesResponseOut": "_bigquerydatatransfer_17_ListDataSourcesResponseOut",
        "LocationIn": "_bigquerydatatransfer_18_LocationIn",
        "LocationOut": "_bigquerydatatransfer_19_LocationOut",
        "EnrollDataSourcesRequestIn": "_bigquerydatatransfer_20_EnrollDataSourcesRequestIn",
        "EnrollDataSourcesRequestOut": "_bigquerydatatransfer_21_EnrollDataSourcesRequestOut",
        "ScheduleTransferRunsResponseIn": "_bigquerydatatransfer_22_ScheduleTransferRunsResponseIn",
        "ScheduleTransferRunsResponseOut": "_bigquerydatatransfer_23_ScheduleTransferRunsResponseOut",
        "StatusIn": "_bigquerydatatransfer_24_StatusIn",
        "StatusOut": "_bigquerydatatransfer_25_StatusOut",
        "TransferConfigIn": "_bigquerydatatransfer_26_TransferConfigIn",
        "TransferConfigOut": "_bigquerydatatransfer_27_TransferConfigOut",
        "CheckValidCredsRequestIn": "_bigquerydatatransfer_28_CheckValidCredsRequestIn",
        "CheckValidCredsRequestOut": "_bigquerydatatransfer_29_CheckValidCredsRequestOut",
        "EmailPreferencesIn": "_bigquerydatatransfer_30_EmailPreferencesIn",
        "EmailPreferencesOut": "_bigquerydatatransfer_31_EmailPreferencesOut",
        "ListTransferRunsResponseIn": "_bigquerydatatransfer_32_ListTransferRunsResponseIn",
        "ListTransferRunsResponseOut": "_bigquerydatatransfer_33_ListTransferRunsResponseOut",
        "DataSourceParameterIn": "_bigquerydatatransfer_34_DataSourceParameterIn",
        "DataSourceParameterOut": "_bigquerydatatransfer_35_DataSourceParameterOut",
        "ScheduleOptionsIn": "_bigquerydatatransfer_36_ScheduleOptionsIn",
        "ScheduleOptionsOut": "_bigquerydatatransfer_37_ScheduleOptionsOut",
        "TransferMessageIn": "_bigquerydatatransfer_38_TransferMessageIn",
        "TransferMessageOut": "_bigquerydatatransfer_39_TransferMessageOut",
        "ListTransferConfigsResponseIn": "_bigquerydatatransfer_40_ListTransferConfigsResponseIn",
        "ListTransferConfigsResponseOut": "_bigquerydatatransfer_41_ListTransferConfigsResponseOut",
        "EmptyIn": "_bigquerydatatransfer_42_EmptyIn",
        "EmptyOut": "_bigquerydatatransfer_43_EmptyOut",
        "StartManualTransferRunsResponseIn": "_bigquerydatatransfer_44_StartManualTransferRunsResponseIn",
        "StartManualTransferRunsResponseOut": "_bigquerydatatransfer_45_StartManualTransferRunsResponseOut",
        "TimeRangeIn": "_bigquerydatatransfer_46_TimeRangeIn",
        "TimeRangeOut": "_bigquerydatatransfer_47_TimeRangeOut",
        "CheckValidCredsResponseIn": "_bigquerydatatransfer_48_CheckValidCredsResponseIn",
        "CheckValidCredsResponseOut": "_bigquerydatatransfer_49_CheckValidCredsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ScheduleTransferRunsRequestIn"] = t.struct(
        {"endTime": t.string(), "startTime": t.string()}
    ).named(renames["ScheduleTransferRunsRequestIn"])
    types["ScheduleTransferRunsRequestOut"] = t.struct(
        {
            "endTime": t.string(),
            "startTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleTransferRunsRequestOut"])
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
    types["TransferRunIn"] = t.struct(
        {
            "runTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "userId": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["TransferRunIn"])
    types["TransferRunOut"] = t.struct(
        {
            "notificationPubsubTopic": t.string().optional(),
            "startTime": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "runTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "userId": t.string().optional(),
            "updateTime": t.string().optional(),
            "endTime": t.string().optional(),
            "schedule": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "destinationDatasetId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferRunOut"])
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
            "supportsMultipleTransfers": t.boolean().optional(),
            "defaultSchedule": t.string().optional(),
            "dataRefreshType": t.string().optional(),
            "description": t.string().optional(),
            "manualRunsDisabled": t.boolean().optional(),
            "helpUrl": t.string().optional(),
            "minimumScheduleInterval": t.string().optional(),
            "displayName": t.string().optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "scopes": t.array(t.string()).optional(),
            "parameters": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "dataSourceId": t.string().optional(),
            "clientId": t.string().optional(),
            "transferType": t.string().optional(),
            "authorizationType": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "supportsCustomSchedule": t.boolean().optional(),
            "supportsMultipleTransfers": t.boolean().optional(),
            "defaultSchedule": t.string().optional(),
            "dataRefreshType": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "manualRunsDisabled": t.boolean().optional(),
            "helpUrl": t.string().optional(),
            "minimumScheduleInterval": t.string().optional(),
            "displayName": t.string().optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "scopes": t.array(t.string()).optional(),
            "parameters": t.array(
                t.proxy(renames["DataSourceParameterOut"])
            ).optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "dataSourceId": t.string().optional(),
            "clientId": t.string().optional(),
            "transferType": t.string().optional(),
            "authorizationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
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
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EnrollDataSourcesRequestIn"] = t.struct(
        {"dataSourceIds": t.array(t.string()).optional()}
    ).named(renames["EnrollDataSourcesRequestIn"])
    types["EnrollDataSourcesRequestOut"] = t.struct(
        {
            "dataSourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollDataSourcesRequestOut"])
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
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["TransferConfigIn"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "schedule": t.string().optional(),
            "destinationDatasetId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
            "dataSourceId": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["TransferConfigIn"])
    types["TransferConfigOut"] = t.struct(
        {
            "disabled": t.boolean().optional(),
            "schedule": t.string().optional(),
            "destinationDatasetId": t.string().optional(),
            "datasetRegion": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsOut"]).optional(),
            "name": t.string().optional(),
            "nextRunTime": t.string().optional(),
            "displayName": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "state": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "userId": t.string().optional(),
            "updateTime": t.string().optional(),
            "ownerInfo": t.proxy(renames["UserInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferConfigOut"])
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
    types["DataSourceParameterIn"] = t.struct(
        {
            "recurse": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "repeated": t.boolean().optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "minValue": t.number().optional(),
            "description": t.string().optional(),
            "validationHelpUrl": t.string().optional(),
            "maxValue": t.number().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "validationDescription": t.string().optional(),
            "paramId": t.string().optional(),
            "required": t.boolean().optional(),
            "immutable": t.boolean().optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "recurse": t.boolean().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "repeated": t.boolean().optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterOut"])).optional(),
            "minValue": t.number().optional(),
            "description": t.string().optional(),
            "validationHelpUrl": t.string().optional(),
            "maxValue": t.number().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "validationDescription": t.string().optional(),
            "paramId": t.string().optional(),
            "required": t.boolean().optional(),
            "immutable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["StartManualTransferRunsResponseIn"] = t.struct(
        {"runs": t.array(t.proxy(renames["TransferRunIn"])).optional()}
    ).named(renames["StartManualTransferRunsResponseIn"])
    types["StartManualTransferRunsResponseOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartManualTransferRunsResponseOut"])
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
    types["CheckValidCredsResponseIn"] = t.struct(
        {"hasValidCreds": t.boolean().optional()}
    ).named(renames["CheckValidCredsResponseIn"])
    types["CheckValidCredsResponseOut"] = t.struct(
        {
            "hasValidCreds": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckValidCredsResponseOut"])

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
    functions["projectsDataSourcesCheckValidCreds"] = bigquerydatatransfer.get(
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
    functions["projectsDataSourcesGet"] = bigquerydatatransfer.get(
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
    functions["projectsDataSourcesList"] = bigquerydatatransfer.get(
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
    functions["projectsLocationsDataSourcesGet"] = bigquerydatatransfer.get(
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
    functions["projectsLocationsDataSourcesCheckValidCreds"] = bigquerydatatransfer.get(
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
    functions["projectsLocationsDataSourcesList"] = bigquerydatatransfer.get(
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
    functions[
        "projectsLocationsTransferConfigsScheduleRuns"
    ] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "disabled": t.boolean().optional(),
                "schedule": t.string().optional(),
                "destinationDatasetId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsStartManualRuns"
    ] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "disabled": t.boolean().optional(),
                "schedule": t.string().optional(),
                "destinationDatasetId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsDelete"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "disabled": t.boolean().optional(),
                "schedule": t.string().optional(),
                "destinationDatasetId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsGet"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "disabled": t.boolean().optional(),
                "schedule": t.string().optional(),
                "destinationDatasetId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsList"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "disabled": t.boolean().optional(),
                "schedule": t.string().optional(),
                "destinationDatasetId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsCreate"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "disabled": t.boolean().optional(),
                "schedule": t.string().optional(),
                "destinationDatasetId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsPatch"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "disabled": t.boolean().optional(),
                "schedule": t.string().optional(),
                "destinationDatasetId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "displayName": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsGet"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsList"] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsRunsDelete"
    ] = bigquerydatatransfer.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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
                "pageSize": t.integer().optional(),
                "messageTypes": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsScheduleRuns"] = bigquerydatatransfer.post(
        "v1/{parent}:startManualRuns",
        t.struct(
            {
                "parent": t.string().optional(),
                "requestedRunTime": t.string().optional(),
                "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartManualTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsCreate"] = bigquerydatatransfer.post(
        "v1/{parent}:startManualRuns",
        t.struct(
            {
                "parent": t.string().optional(),
                "requestedRunTime": t.string().optional(),
                "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartManualTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsList"] = bigquerydatatransfer.post(
        "v1/{parent}:startManualRuns",
        t.struct(
            {
                "parent": t.string().optional(),
                "requestedRunTime": t.string().optional(),
                "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartManualTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsPatch"] = bigquerydatatransfer.post(
        "v1/{parent}:startManualRuns",
        t.struct(
            {
                "parent": t.string().optional(),
                "requestedRunTime": t.string().optional(),
                "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartManualTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsGet"] = bigquerydatatransfer.post(
        "v1/{parent}:startManualRuns",
        t.struct(
            {
                "parent": t.string().optional(),
                "requestedRunTime": t.string().optional(),
                "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartManualTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsDelete"] = bigquerydatatransfer.post(
        "v1/{parent}:startManualRuns",
        t.struct(
            {
                "parent": t.string().optional(),
                "requestedRunTime": t.string().optional(),
                "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartManualTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsStartManualRuns"] = bigquerydatatransfer.post(
        "v1/{parent}:startManualRuns",
        t.struct(
            {
                "parent": t.string().optional(),
                "requestedRunTime": t.string().optional(),
                "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StartManualTransferRunsResponseOut"]),
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
                "messageTypes": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferLogsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="bigquerydatatransfer",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
