from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1SubjectIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1SubjectOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1MessageBodyIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1MessageBodyOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1NotificationIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1NotificationOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1CsvCsvRowIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1CsvCsvRowOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1ListNotificationsResponseIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1ListNotificationsResponseOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1TextIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1TextOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1MessageIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1MessageOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1AttachmentIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1AttachmentOut: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1CsvIn: t.typedef = ...
    GoogleCloudAdvisorynotificationsV1CsvOut: t.typedef = ...

class FuncList:
    organizationsLocationsNotificationsList: t.func = ...
    organizationsLocationsNotificationsGet: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_advisorynotifications() -> Import: ...
