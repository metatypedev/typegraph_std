from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_bigquerydatatransfer() -> Import:
    bigquerydatatransfer = HTTPRuntime("https://bigquerydatatransfer.googleapis.com/")

    renames = {
        "ErrorResponse": "_bigquerydatatransfer_1_ErrorResponse",
        "StatusIn": "_bigquerydatatransfer_2_StatusIn",
        "StatusOut": "_bigquerydatatransfer_3_StatusOut",
        "EmptyIn": "_bigquerydatatransfer_4_EmptyIn",
        "EmptyOut": "_bigquerydatatransfer_5_EmptyOut",
        "EnrollDataSourcesRequestIn": "_bigquerydatatransfer_6_EnrollDataSourcesRequestIn",
        "EnrollDataSourcesRequestOut": "_bigquerydatatransfer_7_EnrollDataSourcesRequestOut",
        "StartManualTransferRunsRequestIn": "_bigquerydatatransfer_8_StartManualTransferRunsRequestIn",
        "StartManualTransferRunsRequestOut": "_bigquerydatatransfer_9_StartManualTransferRunsRequestOut",
        "ListTransferLogsResponseIn": "_bigquerydatatransfer_10_ListTransferLogsResponseIn",
        "ListTransferLogsResponseOut": "_bigquerydatatransfer_11_ListTransferLogsResponseOut",
        "CheckValidCredsRequestIn": "_bigquerydatatransfer_12_CheckValidCredsRequestIn",
        "CheckValidCredsRequestOut": "_bigquerydatatransfer_13_CheckValidCredsRequestOut",
        "TransferMessageIn": "_bigquerydatatransfer_14_TransferMessageIn",
        "TransferMessageOut": "_bigquerydatatransfer_15_TransferMessageOut",
        "DataSourceIn": "_bigquerydatatransfer_16_DataSourceIn",
        "DataSourceOut": "_bigquerydatatransfer_17_DataSourceOut",
        "LocationIn": "_bigquerydatatransfer_18_LocationIn",
        "LocationOut": "_bigquerydatatransfer_19_LocationOut",
        "EmailPreferencesIn": "_bigquerydatatransfer_20_EmailPreferencesIn",
        "EmailPreferencesOut": "_bigquerydatatransfer_21_EmailPreferencesOut",
        "UserInfoIn": "_bigquerydatatransfer_22_UserInfoIn",
        "UserInfoOut": "_bigquerydatatransfer_23_UserInfoOut",
        "ListTransferRunsResponseIn": "_bigquerydatatransfer_24_ListTransferRunsResponseIn",
        "ListTransferRunsResponseOut": "_bigquerydatatransfer_25_ListTransferRunsResponseOut",
        "ScheduleTransferRunsResponseIn": "_bigquerydatatransfer_26_ScheduleTransferRunsResponseIn",
        "ScheduleTransferRunsResponseOut": "_bigquerydatatransfer_27_ScheduleTransferRunsResponseOut",
        "TransferConfigIn": "_bigquerydatatransfer_28_TransferConfigIn",
        "TransferConfigOut": "_bigquerydatatransfer_29_TransferConfigOut",
        "TimeRangeIn": "_bigquerydatatransfer_30_TimeRangeIn",
        "TimeRangeOut": "_bigquerydatatransfer_31_TimeRangeOut",
        "CheckValidCredsResponseIn": "_bigquerydatatransfer_32_CheckValidCredsResponseIn",
        "CheckValidCredsResponseOut": "_bigquerydatatransfer_33_CheckValidCredsResponseOut",
        "ListTransferConfigsResponseIn": "_bigquerydatatransfer_34_ListTransferConfigsResponseIn",
        "ListTransferConfigsResponseOut": "_bigquerydatatransfer_35_ListTransferConfigsResponseOut",
        "ScheduleOptionsIn": "_bigquerydatatransfer_36_ScheduleOptionsIn",
        "ScheduleOptionsOut": "_bigquerydatatransfer_37_ScheduleOptionsOut",
        "ListDataSourcesResponseIn": "_bigquerydatatransfer_38_ListDataSourcesResponseIn",
        "ListDataSourcesResponseOut": "_bigquerydatatransfer_39_ListDataSourcesResponseOut",
        "DataSourceParameterIn": "_bigquerydatatransfer_40_DataSourceParameterIn",
        "DataSourceParameterOut": "_bigquerydatatransfer_41_DataSourceParameterOut",
        "ScheduleTransferRunsRequestIn": "_bigquerydatatransfer_42_ScheduleTransferRunsRequestIn",
        "ScheduleTransferRunsRequestOut": "_bigquerydatatransfer_43_ScheduleTransferRunsRequestOut",
        "TransferRunIn": "_bigquerydatatransfer_44_TransferRunIn",
        "TransferRunOut": "_bigquerydatatransfer_45_TransferRunOut",
        "StartManualTransferRunsResponseIn": "_bigquerydatatransfer_46_StartManualTransferRunsResponseIn",
        "StartManualTransferRunsResponseOut": "_bigquerydatatransfer_47_StartManualTransferRunsResponseOut",
        "ListLocationsResponseIn": "_bigquerydatatransfer_48_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_bigquerydatatransfer_49_ListLocationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["EnrollDataSourcesRequestIn"] = t.struct(
        {"dataSourceIds": t.array(t.string()).optional()}
    ).named(renames["EnrollDataSourcesRequestIn"])
    types["EnrollDataSourcesRequestOut"] = t.struct(
        {
            "dataSourceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollDataSourcesRequestOut"])
    types["StartManualTransferRunsRequestIn"] = t.struct(
        {
            "requestedTimeRange": t.proxy(renames["TimeRangeIn"]).optional(),
            "requestedRunTime": t.string().optional(),
        }
    ).named(renames["StartManualTransferRunsRequestIn"])
    types["StartManualTransferRunsRequestOut"] = t.struct(
        {
            "requestedTimeRange": t.proxy(renames["TimeRangeOut"]).optional(),
            "requestedRunTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartManualTransferRunsRequestOut"])
    types["ListTransferLogsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListTransferLogsResponseIn"]
    )
    types["ListTransferLogsResponseOut"] = t.struct(
        {
            "transferMessages": t.array(
                t.proxy(renames["TransferMessageOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTransferLogsResponseOut"])
    types["CheckValidCredsRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CheckValidCredsRequestIn"]
    )
    types["CheckValidCredsRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CheckValidCredsRequestOut"])
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
    types["DataSourceIn"] = t.struct(
        {
            "manualRunsDisabled": t.boolean().optional(),
            "supportsCustomSchedule": t.boolean().optional(),
            "defaultSchedule": t.string().optional(),
            "helpUrl": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "supportsMultipleTransfers": t.boolean().optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "scopes": t.array(t.string()).optional(),
            "dataRefreshType": t.string().optional(),
            "minimumScheduleInterval": t.string().optional(),
            "parameters": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "clientId": t.string().optional(),
            "transferType": t.string().optional(),
            "authorizationType": t.string().optional(),
        }
    ).named(renames["DataSourceIn"])
    types["DataSourceOut"] = t.struct(
        {
            "manualRunsDisabled": t.boolean().optional(),
            "supportsCustomSchedule": t.boolean().optional(),
            "defaultSchedule": t.string().optional(),
            "helpUrl": t.string().optional(),
            "dataSourceId": t.string().optional(),
            "name": t.string().optional(),
            "defaultDataRefreshWindowDays": t.integer().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "supportsMultipleTransfers": t.boolean().optional(),
            "updateDeadlineSeconds": t.integer().optional(),
            "scopes": t.array(t.string()).optional(),
            "dataRefreshType": t.string().optional(),
            "minimumScheduleInterval": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["DataSourceParameterOut"])
            ).optional(),
            "clientId": t.string().optional(),
            "transferType": t.string().optional(),
            "authorizationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmailPreferencesIn"] = t.struct(
        {"enableFailureEmail": t.boolean().optional()}
    ).named(renames["EmailPreferencesIn"])
    types["EmailPreferencesOut"] = t.struct(
        {
            "enableFailureEmail": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmailPreferencesOut"])
    types["UserInfoIn"] = t.struct({"email": t.string().optional()}).named(
        renames["UserInfoIn"]
    )
    types["UserInfoOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserInfoOut"])
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
    types["ScheduleTransferRunsResponseIn"] = t.struct(
        {"runs": t.array(t.proxy(renames["TransferRunIn"])).optional()}
    ).named(renames["ScheduleTransferRunsResponseIn"])
    types["ScheduleTransferRunsResponseOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleTransferRunsResponseOut"])
    types["TransferConfigIn"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
            "userId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "displayName": t.string().optional(),
            "schedule": t.string().optional(),
            "name": t.string().optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "disabled": t.boolean().optional(),
            "destinationDatasetId": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
        }
    ).named(renames["TransferConfigIn"])
    types["TransferConfigOut"] = t.struct(
        {
            "dataSourceId": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "scheduleOptions": t.proxy(renames["ScheduleOptionsOut"]).optional(),
            "nextRunTime": t.string().optional(),
            "userId": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "displayName": t.string().optional(),
            "schedule": t.string().optional(),
            "name": t.string().optional(),
            "datasetRegion": t.string().optional(),
            "ownerInfo": t.proxy(renames["UserInfoOut"]).optional(),
            "dataRefreshWindowDays": t.integer().optional(),
            "state": t.string().optional(),
            "disabled": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "destinationDatasetId": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferConfigOut"])
    types["TimeRangeIn"] = t.struct(
        {"endTime": t.string().optional(), "startTime": t.string().optional()}
    ).named(renames["TimeRangeIn"])
    types["TimeRangeOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
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
            "disableAutoScheduling": t.boolean().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ScheduleOptionsIn"])
    types["ScheduleOptionsOut"] = t.struct(
        {
            "disableAutoScheduling": t.boolean().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOptionsOut"])
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
    types["DataSourceParameterIn"] = t.struct(
        {
            "validationHelpUrl": t.string().optional(),
            "validationDescription": t.string().optional(),
            "repeated": t.boolean().optional(),
            "maxValue": t.number().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterIn"])).optional(),
            "description": t.string().optional(),
            "immutable": t.boolean().optional(),
            "required": t.boolean().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "recurse": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "minValue": t.number().optional(),
            "paramId": t.string().optional(),
        }
    ).named(renames["DataSourceParameterIn"])
    types["DataSourceParameterOut"] = t.struct(
        {
            "validationHelpUrl": t.string().optional(),
            "validationDescription": t.string().optional(),
            "repeated": t.boolean().optional(),
            "maxValue": t.number().optional(),
            "allowedValues": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["DataSourceParameterOut"])).optional(),
            "description": t.string().optional(),
            "immutable": t.boolean().optional(),
            "required": t.boolean().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "recurse": t.boolean().optional(),
            "validationRegex": t.string().optional(),
            "deprecated": t.boolean().optional(),
            "minValue": t.number().optional(),
            "paramId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DataSourceParameterOut"])
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
    types["TransferRunIn"] = t.struct(
        {
            "state": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusIn"]).optional(),
            "runTime": t.string().optional(),
            "name": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["TransferRunIn"])
    types["TransferRunOut"] = t.struct(
        {
            "state": t.string().optional(),
            "schedule": t.string().optional(),
            "scheduleTime": t.string().optional(),
            "notificationPubsubTopic": t.string().optional(),
            "updateTime": t.string().optional(),
            "endTime": t.string().optional(),
            "errorStatus": t.proxy(renames["StatusOut"]).optional(),
            "runTime": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "destinationDatasetId": t.string().optional(),
            "name": t.string().optional(),
            "userId": t.string().optional(),
            "emailPreferences": t.proxy(renames["EmailPreferencesOut"]).optional(),
            "dataSourceId": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferRunOut"])
    types["StartManualTransferRunsResponseIn"] = t.struct(
        {"runs": t.array(t.proxy(renames["TransferRunIn"])).optional()}
    ).named(renames["StartManualTransferRunsResponseIn"])
    types["StartManualTransferRunsResponseOut"] = t.struct(
        {
            "runs": t.array(t.proxy(renames["TransferRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StartManualTransferRunsResponseOut"])
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
    functions["projectsTransferConfigsStartManualRuns"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsScheduleRuns"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsCreate"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsList"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsDelete"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsGet"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsPatch"] = bigquerydatatransfer.patch(
        "v1/{name}",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "updateMask": t.string(),
                "versionInfo": t.string().optional(),
                "name": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsGet"] = bigquerydatatransfer.get(
        "v1/{parent}/runs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "runAttempt": t.string().optional(),
                "pageToken": t.string().optional(),
                "states": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsDelete"] = bigquerydatatransfer.get(
        "v1/{parent}/runs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "runAttempt": t.string().optional(),
                "pageToken": t.string().optional(),
                "states": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsList"] = bigquerydatatransfer.get(
        "v1/{parent}/runs",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "runAttempt": t.string().optional(),
                "pageToken": t.string().optional(),
                "states": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTransferConfigsRunsTransferLogsList"] = bigquerydatatransfer.get(
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
    functions["projectsLocationsList"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsEnrollDataSources"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataSourcesCheckValidCreds"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataSourcesList"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsDataSourcesGet"] = bigquerydatatransfer.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DataSourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsList"] = bigquerydatatransfer.post(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "parent": t.string(),
                "versionInfo": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsGet"] = bigquerydatatransfer.post(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "parent": t.string(),
                "versionInfo": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsStartManualRuns"
    ] = bigquerydatatransfer.post(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "parent": t.string(),
                "versionInfo": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsDelete"] = bigquerydatatransfer.post(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "parent": t.string(),
                "versionInfo": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsPatch"] = bigquerydatatransfer.post(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "parent": t.string(),
                "versionInfo": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsScheduleRuns"
    ] = bigquerydatatransfer.post(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "parent": t.string(),
                "versionInfo": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsCreate"] = bigquerydatatransfer.post(
        "v1/{parent}/transferConfigs",
        t.struct(
            {
                "authorizationCode": t.string().optional(),
                "serviceAccountName": t.string().optional(),
                "parent": t.string(),
                "versionInfo": t.string().optional(),
                "dataSourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "scheduleOptions": t.proxy(renames["ScheduleOptionsIn"]).optional(),
                "userId": t.string().optional(),
                "notificationPubsubTopic": t.string().optional(),
                "displayName": t.string().optional(),
                "schedule": t.string().optional(),
                "name": t.string().optional(),
                "dataRefreshWindowDays": t.integer().optional(),
                "disabled": t.boolean().optional(),
                "destinationDatasetId": t.string().optional(),
                "emailPreferences": t.proxy(renames["EmailPreferencesIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TransferConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsGet"] = bigquerydatatransfer.get(
        "v1/{parent}/runs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "runAttempt": t.string().optional(),
                "states": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsDelete"] = bigquerydatatransfer.get(
        "v1/{parent}/runs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "runAttempt": t.string().optional(),
                "states": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTransferConfigsRunsList"] = bigquerydatatransfer.get(
        "v1/{parent}/runs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "runAttempt": t.string().optional(),
                "states": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTransferRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsTransferConfigsRunsTransferLogsList"
    ] = bigquerydatatransfer.get(
        "v1/{parent}/transferLogs",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "messageTypes": t.string().optional(),
                "parent": t.string(),
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
        types=types,
        functions=functions,
    )
