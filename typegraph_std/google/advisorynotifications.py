from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_advisorynotifications() -> Import:
    advisorynotifications = HTTPRuntime("https://advisorynotifications.googleapis.com/")

    renames = {
        "ErrorResponse": "_advisorynotifications_1_ErrorResponse",
        "GoogleCloudAdvisorynotificationsV1SubjectIn": "_advisorynotifications_2_GoogleCloudAdvisorynotificationsV1SubjectIn",
        "GoogleCloudAdvisorynotificationsV1SubjectOut": "_advisorynotifications_3_GoogleCloudAdvisorynotificationsV1SubjectOut",
        "GoogleCloudAdvisorynotificationsV1MessageIn": "_advisorynotifications_4_GoogleCloudAdvisorynotificationsV1MessageIn",
        "GoogleCloudAdvisorynotificationsV1MessageOut": "_advisorynotifications_5_GoogleCloudAdvisorynotificationsV1MessageOut",
        "GoogleCloudAdvisorynotificationsV1CsvCsvRowIn": "_advisorynotifications_6_GoogleCloudAdvisorynotificationsV1CsvCsvRowIn",
        "GoogleCloudAdvisorynotificationsV1CsvCsvRowOut": "_advisorynotifications_7_GoogleCloudAdvisorynotificationsV1CsvCsvRowOut",
        "GoogleCloudAdvisorynotificationsV1NotificationIn": "_advisorynotifications_8_GoogleCloudAdvisorynotificationsV1NotificationIn",
        "GoogleCloudAdvisorynotificationsV1NotificationOut": "_advisorynotifications_9_GoogleCloudAdvisorynotificationsV1NotificationOut",
        "GoogleCloudAdvisorynotificationsV1TextIn": "_advisorynotifications_10_GoogleCloudAdvisorynotificationsV1TextIn",
        "GoogleCloudAdvisorynotificationsV1TextOut": "_advisorynotifications_11_GoogleCloudAdvisorynotificationsV1TextOut",
        "GoogleCloudAdvisorynotificationsV1CsvIn": "_advisorynotifications_12_GoogleCloudAdvisorynotificationsV1CsvIn",
        "GoogleCloudAdvisorynotificationsV1CsvOut": "_advisorynotifications_13_GoogleCloudAdvisorynotificationsV1CsvOut",
        "GoogleCloudAdvisorynotificationsV1MessageBodyIn": "_advisorynotifications_14_GoogleCloudAdvisorynotificationsV1MessageBodyIn",
        "GoogleCloudAdvisorynotificationsV1MessageBodyOut": "_advisorynotifications_15_GoogleCloudAdvisorynotificationsV1MessageBodyOut",
        "GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn": "_advisorynotifications_16_GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn",
        "GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut": "_advisorynotifications_17_GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut",
        "GoogleCloudAdvisorynotificationsV1AttachmentIn": "_advisorynotifications_18_GoogleCloudAdvisorynotificationsV1AttachmentIn",
        "GoogleCloudAdvisorynotificationsV1AttachmentOut": "_advisorynotifications_19_GoogleCloudAdvisorynotificationsV1AttachmentOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudAdvisorynotificationsV1SubjectIn"] = t.struct(
        {
            "text": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1TextIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1SubjectIn"])
    types["GoogleCloudAdvisorynotificationsV1SubjectOut"] = t.struct(
        {
            "text": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1TextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1SubjectOut"])
    types["GoogleCloudAdvisorynotificationsV1MessageIn"] = t.struct(
        {
            "localizationTime": t.string().optional(),
            "attachments": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1AttachmentIn"])
            ).optional(),
            "createTime": t.string().optional(),
            "body": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1MessageBodyIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1MessageIn"])
    types["GoogleCloudAdvisorynotificationsV1MessageOut"] = t.struct(
        {
            "localizationTime": t.string().optional(),
            "attachments": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1AttachmentOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "body": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1MessageBodyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1MessageOut"])
    types["GoogleCloudAdvisorynotificationsV1CsvCsvRowIn"] = t.struct(
        {"entries": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowIn"])
    types["GoogleCloudAdvisorynotificationsV1CsvCsvRowOut"] = t.struct(
        {
            "entries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowOut"])
    types["GoogleCloudAdvisorynotificationsV1NotificationIn"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1MessageIn"])
            ).optional(),
            "name": t.string().optional(),
            "subject": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1SubjectIn"]
            ).optional(),
            "notificationType": t.string().optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1NotificationIn"])
    types["GoogleCloudAdvisorynotificationsV1NotificationOut"] = t.struct(
        {
            "messages": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1MessageOut"])
            ).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "subject": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1SubjectOut"]
            ).optional(),
            "notificationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1NotificationOut"])
    types["GoogleCloudAdvisorynotificationsV1TextIn"] = t.struct(
        {
            "localizedText": t.string().optional(),
            "enText": t.string().optional(),
            "localizationState": t.string().optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1TextIn"])
    types["GoogleCloudAdvisorynotificationsV1TextOut"] = t.struct(
        {
            "localizedText": t.string().optional(),
            "enText": t.string().optional(),
            "localizationState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1TextOut"])
    types["GoogleCloudAdvisorynotificationsV1CsvIn"] = t.struct(
        {
            "headers": t.array(t.string()).optional(),
            "dataRows": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvIn"])
    types["GoogleCloudAdvisorynotificationsV1CsvOut"] = t.struct(
        {
            "headers": t.array(t.string()).optional(),
            "dataRows": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvOut"])
    types["GoogleCloudAdvisorynotificationsV1MessageBodyIn"] = t.struct(
        {
            "text": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1TextIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1MessageBodyIn"])
    types["GoogleCloudAdvisorynotificationsV1MessageBodyOut"] = t.struct(
        {
            "text": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1TextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1MessageBodyOut"])
    types["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "notifications": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1NotificationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn"])
    types["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "notifications": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1NotificationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut"])
    types["GoogleCloudAdvisorynotificationsV1AttachmentIn"] = t.struct(
        {
            "csv": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1CsvIn"]
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1AttachmentIn"])
    types["GoogleCloudAdvisorynotificationsV1AttachmentOut"] = t.struct(
        {
            "csv": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1CsvOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1AttachmentOut"])

    functions = {}
    functions["organizationsLocationsNotificationsGet"] = advisorynotifications.get(
        "v1/{parent}/notifications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsNotificationsList"] = advisorynotifications.get(
        "v1/{parent}/notifications",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "view": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="advisorynotifications",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
