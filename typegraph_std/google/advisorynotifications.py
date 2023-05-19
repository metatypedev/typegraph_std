from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_advisorynotifications() -> Import:
    advisorynotifications = HTTPRuntime("https://advisorynotifications.googleapis.com/")

    renames = {
        "ErrorResponse": "_advisorynotifications_1_ErrorResponse",
        "GoogleCloudAdvisorynotificationsV1MessageBodyIn": "_advisorynotifications_2_GoogleCloudAdvisorynotificationsV1MessageBodyIn",
        "GoogleCloudAdvisorynotificationsV1MessageBodyOut": "_advisorynotifications_3_GoogleCloudAdvisorynotificationsV1MessageBodyOut",
        "GoogleCloudAdvisorynotificationsV1TextIn": "_advisorynotifications_4_GoogleCloudAdvisorynotificationsV1TextIn",
        "GoogleCloudAdvisorynotificationsV1TextOut": "_advisorynotifications_5_GoogleCloudAdvisorynotificationsV1TextOut",
        "GoogleCloudAdvisorynotificationsV1CsvIn": "_advisorynotifications_6_GoogleCloudAdvisorynotificationsV1CsvIn",
        "GoogleCloudAdvisorynotificationsV1CsvOut": "_advisorynotifications_7_GoogleCloudAdvisorynotificationsV1CsvOut",
        "GoogleCloudAdvisorynotificationsV1MessageIn": "_advisorynotifications_8_GoogleCloudAdvisorynotificationsV1MessageIn",
        "GoogleCloudAdvisorynotificationsV1MessageOut": "_advisorynotifications_9_GoogleCloudAdvisorynotificationsV1MessageOut",
        "GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn": "_advisorynotifications_10_GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn",
        "GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut": "_advisorynotifications_11_GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut",
        "GoogleCloudAdvisorynotificationsV1NotificationIn": "_advisorynotifications_12_GoogleCloudAdvisorynotificationsV1NotificationIn",
        "GoogleCloudAdvisorynotificationsV1NotificationOut": "_advisorynotifications_13_GoogleCloudAdvisorynotificationsV1NotificationOut",
        "GoogleCloudAdvisorynotificationsV1AttachmentIn": "_advisorynotifications_14_GoogleCloudAdvisorynotificationsV1AttachmentIn",
        "GoogleCloudAdvisorynotificationsV1AttachmentOut": "_advisorynotifications_15_GoogleCloudAdvisorynotificationsV1AttachmentOut",
        "GoogleCloudAdvisorynotificationsV1SubjectIn": "_advisorynotifications_16_GoogleCloudAdvisorynotificationsV1SubjectIn",
        "GoogleCloudAdvisorynotificationsV1SubjectOut": "_advisorynotifications_17_GoogleCloudAdvisorynotificationsV1SubjectOut",
        "GoogleCloudAdvisorynotificationsV1CsvCsvRowIn": "_advisorynotifications_18_GoogleCloudAdvisorynotificationsV1CsvCsvRowIn",
        "GoogleCloudAdvisorynotificationsV1CsvCsvRowOut": "_advisorynotifications_19_GoogleCloudAdvisorynotificationsV1CsvCsvRowOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleCloudAdvisorynotificationsV1TextIn"] = t.struct(
        {
            "localizedText": t.string().optional(),
            "localizationState": t.string().optional(),
            "enText": t.string().optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1TextIn"])
    types["GoogleCloudAdvisorynotificationsV1TextOut"] = t.struct(
        {
            "localizedText": t.string().optional(),
            "localizationState": t.string().optional(),
            "enText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1TextOut"])
    types["GoogleCloudAdvisorynotificationsV1CsvIn"] = t.struct(
        {
            "dataRows": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowIn"])
            ).optional(),
            "headers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvIn"])
    types["GoogleCloudAdvisorynotificationsV1CsvOut"] = t.struct(
        {
            "dataRows": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowOut"])
            ).optional(),
            "headers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvOut"])
    types["GoogleCloudAdvisorynotificationsV1MessageIn"] = t.struct(
        {
            "localizationTime": t.string().optional(),
            "body": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1MessageBodyIn"]
            ).optional(),
            "attachments": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1AttachmentIn"])
            ).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1MessageIn"])
    types["GoogleCloudAdvisorynotificationsV1MessageOut"] = t.struct(
        {
            "localizationTime": t.string().optional(),
            "body": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1MessageBodyOut"]
            ).optional(),
            "attachments": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1AttachmentOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1MessageOut"])
    types["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "notifications": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1NotificationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn"])
    types["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "notifications": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1NotificationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut"])
    types["GoogleCloudAdvisorynotificationsV1NotificationIn"] = t.struct(
        {
            "notificationType": t.string().optional(),
            "name": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1MessageIn"])
            ).optional(),
            "subject": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1SubjectIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1NotificationIn"])
    types["GoogleCloudAdvisorynotificationsV1NotificationOut"] = t.struct(
        {
            "notificationType": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "messages": t.array(
                t.proxy(renames["GoogleCloudAdvisorynotificationsV1MessageOut"])
            ).optional(),
            "subject": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1SubjectOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1NotificationOut"])
    types["GoogleCloudAdvisorynotificationsV1AttachmentIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "csv": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1CsvIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1AttachmentIn"])
    types["GoogleCloudAdvisorynotificationsV1AttachmentOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "csv": t.proxy(
                renames["GoogleCloudAdvisorynotificationsV1CsvOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1AttachmentOut"])
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
    types["GoogleCloudAdvisorynotificationsV1CsvCsvRowIn"] = t.struct(
        {"entries": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowIn"])
    types["GoogleCloudAdvisorynotificationsV1CsvCsvRowOut"] = t.struct(
        {
            "entries": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAdvisorynotificationsV1CsvCsvRowOut"])

    functions = {}
    functions["organizationsLocationsNotificationsList"] = advisorynotifications.get(
        "v1/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAdvisorynotificationsV1NotificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsNotificationsGet"] = advisorynotifications.get(
        "v1/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAdvisorynotificationsV1NotificationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="advisorynotifications",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
