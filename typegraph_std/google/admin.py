from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_admin() -> Import:
    admin = HTTPRuntime("https://admin.googleapis.com/")

    renames = {
        "ErrorResponse": "_admin_1_ErrorResponse",
        "ChannelIn": "_admin_2_ChannelIn",
        "ChannelOut": "_admin_3_ChannelOut",
        "NestedParameterIn": "_admin_4_NestedParameterIn",
        "NestedParameterOut": "_admin_5_NestedParameterOut",
        "UsageReportIn": "_admin_6_UsageReportIn",
        "UsageReportOut": "_admin_7_UsageReportOut",
        "ActivitiesIn": "_admin_8_ActivitiesIn",
        "ActivitiesOut": "_admin_9_ActivitiesOut",
        "ActivityIn": "_admin_10_ActivityIn",
        "ActivityOut": "_admin_11_ActivityOut",
        "UsageReportsIn": "_admin_12_UsageReportsIn",
        "UsageReportsOut": "_admin_13_UsageReportsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChannelIn"] = t.struct(
        {
            "address": t.string().optional(),
            "resourceId": t.string().optional(),
            "payload": t.boolean().optional(),
            "id": t.string().optional(),
            "resourceUri": t.string().optional(),
            "type": t.string().optional(),
            "expiration": t.string().optional(),
            "token": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "address": t.string().optional(),
            "resourceId": t.string().optional(),
            "payload": t.boolean().optional(),
            "id": t.string().optional(),
            "resourceUri": t.string().optional(),
            "type": t.string().optional(),
            "expiration": t.string().optional(),
            "token": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["NestedParameterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "intValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "multiIntValue": t.array(t.string()).optional(),
            "multiValue": t.array(t.string()).optional(),
            "multiBoolValue": t.array(t.boolean()).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["NestedParameterIn"])
    types["NestedParameterOut"] = t.struct(
        {
            "name": t.string().optional(),
            "intValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "multiIntValue": t.array(t.string()).optional(),
            "multiValue": t.array(t.string()).optional(),
            "multiBoolValue": t.array(t.boolean()).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestedParameterOut"])
    types["UsageReportIn"] = t.struct(
        {"kind": t.string().optional(), "etag": t.string().optional()}
    ).named(renames["UsageReportIn"])
    types["UsageReportOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "entity": t.struct(
                {
                    "type": t.string().optional(),
                    "customerId": t.string().optional(),
                    "profileId": t.string().optional(),
                    "entityId": t.string().optional(),
                    "userEmail": t.string().optional(),
                }
            ).optional(),
            "parameters": t.array(
                t.struct(
                    {
                        "boolValue": t.boolean().optional(),
                        "intValue": t.string().optional(),
                        "msgValue": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "stringValue": t.string().optional(),
                        "name": t.string().optional(),
                        "datetimeValue": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "date": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageReportOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityIn"])).optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["ActivityIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "actor": t.struct(
                {
                    "key": t.string().optional(),
                    "email": t.string().optional(),
                    "profileId": t.string().optional(),
                    "callerType": t.string().optional(),
                }
            ).optional(),
            "events": t.array(
                t.struct(
                    {
                        "type": t.string().optional(),
                        "parameters": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "boolValue": t.boolean().optional(),
                                    "multiMessageValue": t.array(
                                        t.struct(
                                            {
                                                "parameter": t.array(
                                                    t.proxy(
                                                        renames["NestedParameterIn"]
                                                    )
                                                ).optional()
                                            }
                                        )
                                    ).optional(),
                                    "intValue": t.string().optional(),
                                    "value": t.string().optional(),
                                    "multiIntValue": t.array(t.string()).optional(),
                                    "multiValue": t.array(t.string()).optional(),
                                    "messageValue": t.struct(
                                        {
                                            "parameter": t.array(
                                                t.proxy(renames["NestedParameterIn"])
                                            ).optional()
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "ipAddress": t.string().optional(),
            "ownerDomain": t.string().optional(),
            "id": t.struct(
                {
                    "uniqueQualifier": t.string().optional(),
                    "applicationName": t.string().optional(),
                    "customerId": t.string().optional(),
                    "time": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "actor": t.struct(
                {
                    "key": t.string().optional(),
                    "email": t.string().optional(),
                    "profileId": t.string().optional(),
                    "callerType": t.string().optional(),
                }
            ).optional(),
            "events": t.array(
                t.struct(
                    {
                        "type": t.string().optional(),
                        "parameters": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "boolValue": t.boolean().optional(),
                                    "multiMessageValue": t.array(
                                        t.struct(
                                            {
                                                "parameter": t.array(
                                                    t.proxy(
                                                        renames["NestedParameterOut"]
                                                    )
                                                ).optional()
                                            }
                                        )
                                    ).optional(),
                                    "intValue": t.string().optional(),
                                    "value": t.string().optional(),
                                    "multiIntValue": t.array(t.string()).optional(),
                                    "multiValue": t.array(t.string()).optional(),
                                    "messageValue": t.struct(
                                        {
                                            "parameter": t.array(
                                                t.proxy(renames["NestedParameterOut"])
                                            ).optional()
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional(),
                        "name": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "ipAddress": t.string().optional(),
            "ownerDomain": t.string().optional(),
            "id": t.struct(
                {
                    "uniqueQualifier": t.string().optional(),
                    "applicationName": t.string().optional(),
                    "customerId": t.string().optional(),
                    "time": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
    types["UsageReportsIn"] = t.struct(
        {
            "usageReports": t.array(t.proxy(renames["UsageReportIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                        "code": t.string().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["UsageReportsIn"])
    types["UsageReportsOut"] = t.struct(
        {
            "usageReports": t.array(t.proxy(renames["UsageReportOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                        "code": t.string().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageReportsOut"])

    functions = {}
    functions["activitiesList"] = admin.post(
        "admin/reports/v1/activity/users/{userKey}/applications/{applicationName}/watch",
        t.struct(
            {
                "eventName": t.string().optional(),
                "startTime": t.string().optional(),
                "actorIpAddress": t.string().optional(),
                "pageToken": t.string().optional(),
                "userKey": t.string().optional(),
                "endTime": t.string().optional(),
                "filters": t.string().optional(),
                "applicationName": t.string().optional(),
                "orgUnitID": t.string().optional(),
                "groupIdFilter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "customerId": t.string().optional(),
                "address": t.string().optional(),
                "resourceId": t.string().optional(),
                "payload": t.boolean().optional(),
                "id": t.string().optional(),
                "resourceUri": t.string().optional(),
                "type": t.string().optional(),
                "expiration": t.string().optional(),
                "token": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["activitiesWatch"] = admin.post(
        "admin/reports/v1/activity/users/{userKey}/applications/{applicationName}/watch",
        t.struct(
            {
                "eventName": t.string().optional(),
                "startTime": t.string().optional(),
                "actorIpAddress": t.string().optional(),
                "pageToken": t.string().optional(),
                "userKey": t.string().optional(),
                "endTime": t.string().optional(),
                "filters": t.string().optional(),
                "applicationName": t.string().optional(),
                "orgUnitID": t.string().optional(),
                "groupIdFilter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "customerId": t.string().optional(),
                "address": t.string().optional(),
                "resourceId": t.string().optional(),
                "payload": t.boolean().optional(),
                "id": t.string().optional(),
                "resourceUri": t.string().optional(),
                "type": t.string().optional(),
                "expiration": t.string().optional(),
                "token": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entityUsageReportsGet"] = admin.get(
        "admin/reports/v1/usage/{entityType}/{entityKey}/dates/{date}",
        t.struct(
            {
                "filters": t.string().optional(),
                "entityKey": t.string().optional(),
                "customerId": t.string().optional(),
                "parameters": t.string().optional(),
                "pageToken": t.string().optional(),
                "entityType": t.string().optional(),
                "maxResults": t.integer().optional(),
                "date": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsageReportsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customerUsageReportsGet"] = admin.get(
        "admin/reports/v1/usage/dates/{date}",
        t.struct(
            {
                "date": t.string().optional(),
                "parameters": t.string().optional(),
                "pageToken": t.string().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsageReportsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["userUsageReportGet"] = admin.get(
        "admin/reports/v1/usage/users/{userKey}/dates/{date}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filters": t.string().optional(),
                "parameters": t.string().optional(),
                "groupIdFilter": t.string().optional(),
                "orgUnitID": t.string().optional(),
                "maxResults": t.integer().optional(),
                "date": t.string().optional(),
                "userKey": t.string().optional(),
                "customerId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UsageReportsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsStop"] = admin.post(
        "admin/reports_v1/channels/stop",
        t.struct(
            {
                "address": t.string().optional(),
                "resourceId": t.string().optional(),
                "payload": t.boolean().optional(),
                "id": t.string().optional(),
                "resourceUri": t.string().optional(),
                "type": t.string().optional(),
                "expiration": t.string().optional(),
                "token": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "kind": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="admin", renames=renames, types=Box(types), functions=Box(functions)
    )
