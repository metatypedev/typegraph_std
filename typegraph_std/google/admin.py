from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_admin():
    admin = HTTPRuntime("https://admin.googleapis.com/")

    renames = {
        "ErrorResponse": "_admin_1_ErrorResponse",
        "NestedParameterIn": "_admin_2_NestedParameterIn",
        "NestedParameterOut": "_admin_3_NestedParameterOut",
        "ChannelIn": "_admin_4_ChannelIn",
        "ChannelOut": "_admin_5_ChannelOut",
        "UsageReportsIn": "_admin_6_UsageReportsIn",
        "UsageReportsOut": "_admin_7_UsageReportsOut",
        "ActivitiesIn": "_admin_8_ActivitiesIn",
        "ActivitiesOut": "_admin_9_ActivitiesOut",
        "ActivityIn": "_admin_10_ActivityIn",
        "ActivityOut": "_admin_11_ActivityOut",
        "UsageReportIn": "_admin_12_UsageReportIn",
        "UsageReportOut": "_admin_13_UsageReportOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NestedParameterIn"] = t.struct(
        {
            "intValue": t.string().optional(),
            "value": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "name": t.string().optional(),
            "multiIntValue": t.array(t.string()).optional(),
            "multiBoolValue": t.array(t.boolean()).optional(),
            "multiValue": t.array(t.string()).optional(),
        }
    ).named(renames["NestedParameterIn"])
    types["NestedParameterOut"] = t.struct(
        {
            "intValue": t.string().optional(),
            "value": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "name": t.string().optional(),
            "multiIntValue": t.array(t.string()).optional(),
            "multiBoolValue": t.array(t.boolean()).optional(),
            "multiValue": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NestedParameterOut"])
    types["ChannelIn"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "address": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.boolean().optional(),
            "type": t.string().optional(),
            "resourceUri": t.string().optional(),
            "expiration": t.string().optional(),
            "token": t.string().optional(),
            "resourceId": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "address": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.boolean().optional(),
            "type": t.string().optional(),
            "resourceUri": t.string().optional(),
            "expiration": t.string().optional(),
            "token": t.string().optional(),
            "resourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["UsageReportsIn"] = t.struct(
        {
            "usageReports": t.array(t.proxy(renames["UsageReportIn"])).optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                    }
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["UsageReportsIn"])
    types["UsageReportsOut"] = t.struct(
        {
            "usageReports": t.array(t.proxy(renames["UsageReportOut"])).optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                    }
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageReportsOut"])
    types["ActivitiesIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ActivitiesIn"])
    types["ActivitiesOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["ActivityOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivitiesOut"])
    types["ActivityIn"] = t.struct(
        {
            "id": t.struct(
                {
                    "uniqueQualifier": t.string().optional(),
                    "applicationName": t.string().optional(),
                    "customerId": t.string().optional(),
                    "time": t.string().optional(),
                }
            ).optional(),
            "events": t.array(
                t.struct(
                    {
                        "parameters": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "multiIntValue": t.array(t.string()).optional(),
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
                                    "boolValue": t.boolean().optional(),
                                    "multiValue": t.array(t.string()).optional(),
                                    "messageValue": t.struct(
                                        {
                                            "parameter": t.array(
                                                t.proxy(renames["NestedParameterIn"])
                                            ).optional()
                                        }
                                    ).optional(),
                                    "intValue": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "ipAddress": t.string().optional(),
            "actor": t.struct(
                {
                    "callerType": t.string().optional(),
                    "email": t.string().optional(),
                    "profileId": t.string().optional(),
                    "key": t.string().optional(),
                }
            ).optional(),
            "ownerDomain": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["ActivityIn"])
    types["ActivityOut"] = t.struct(
        {
            "id": t.struct(
                {
                    "uniqueQualifier": t.string().optional(),
                    "applicationName": t.string().optional(),
                    "customerId": t.string().optional(),
                    "time": t.string().optional(),
                }
            ).optional(),
            "events": t.array(
                t.struct(
                    {
                        "parameters": t.array(
                            t.struct(
                                {
                                    "name": t.string().optional(),
                                    "multiIntValue": t.array(t.string()).optional(),
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
                                    "boolValue": t.boolean().optional(),
                                    "multiValue": t.array(t.string()).optional(),
                                    "messageValue": t.struct(
                                        {
                                            "parameter": t.array(
                                                t.proxy(renames["NestedParameterOut"])
                                            ).optional()
                                        }
                                    ).optional(),
                                    "intValue": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "name": t.string().optional(),
                        "type": t.string().optional(),
                    }
                )
            ).optional(),
            "kind": t.string().optional(),
            "ipAddress": t.string().optional(),
            "actor": t.struct(
                {
                    "callerType": t.string().optional(),
                    "email": t.string().optional(),
                    "profileId": t.string().optional(),
                    "key": t.string().optional(),
                }
            ).optional(),
            "ownerDomain": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActivityOut"])
    types["UsageReportIn"] = t.struct(
        {"etag": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["UsageReportIn"])
    types["UsageReportOut"] = t.struct(
        {
            "parameters": t.array(
                t.struct(
                    {
                        "stringValue": t.string().optional(),
                        "datetimeValue": t.string().optional(),
                        "msgValue": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "name": t.string().optional(),
                        "intValue": t.string().optional(),
                        "boolValue": t.boolean().optional(),
                    }
                )
            ).optional(),
            "date": t.string().optional(),
            "etag": t.string().optional(),
            "entity": t.struct(
                {
                    "profileId": t.string().optional(),
                    "userEmail": t.string().optional(),
                    "customerId": t.string().optional(),
                    "entityId": t.string().optional(),
                    "type": t.string().optional(),
                }
            ).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageReportOut"])

    functions = {}
    functions["entityUsageReportsGet"] = admin.get(
        "admin/reports/v1/usage/{entityType}/{entityKey}/dates/{date}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parameters": t.string().optional(),
                "filters": t.string().optional(),
                "date": t.string().optional(),
                "entityType": t.string().optional(),
                "entityKey": t.string().optional(),
                "maxResults": t.integer().optional(),
                "customerId": t.string().optional(),
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
                "parameters": t.string().optional(),
                "customerId": t.string().optional(),
                "pageToken": t.string().optional(),
                "date": t.string().optional(),
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
                "userKey": t.string().optional(),
                "parameters": t.string().optional(),
                "customerId": t.string().optional(),
                "filters": t.string().optional(),
                "date": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orgUnitID": t.string().optional(),
                "groupIdFilter": t.string().optional(),
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
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "type": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "token": t.string().optional(),
                "resourceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["activitiesWatch"] = admin.get(
        "admin/reports/v1/activity/users/{userKey}/applications/{applicationName}",
        t.struct(
            {
                "startTime": t.string().optional(),
                "customerId": t.string().optional(),
                "userKey": t.string().optional(),
                "actorIpAddress": t.string().optional(),
                "applicationName": t.string().optional(),
                "filters": t.string().optional(),
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "orgUnitID": t.string().optional(),
                "maxResults": t.integer().optional(),
                "groupIdFilter": t.string().optional(),
                "eventName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ActivitiesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["activitiesList"] = admin.get(
        "admin/reports/v1/activity/users/{userKey}/applications/{applicationName}",
        t.struct(
            {
                "startTime": t.string().optional(),
                "customerId": t.string().optional(),
                "userKey": t.string().optional(),
                "actorIpAddress": t.string().optional(),
                "applicationName": t.string().optional(),
                "filters": t.string().optional(),
                "endTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "orgUnitID": t.string().optional(),
                "maxResults": t.integer().optional(),
                "groupIdFilter": t.string().optional(),
                "eventName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ActivitiesOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="admin", renames=renames, types=Box(types), functions=Box(functions)
    )
