from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_calendar() -> Import:
    calendar = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_calendar_1_ErrorResponse",
        "FreeBusyResponseIn": "_calendar_2_FreeBusyResponseIn",
        "FreeBusyResponseOut": "_calendar_3_FreeBusyResponseOut",
        "FreeBusyRequestIn": "_calendar_4_FreeBusyRequestIn",
        "FreeBusyRequestOut": "_calendar_5_FreeBusyRequestOut",
        "FreeBusyCalendarIn": "_calendar_6_FreeBusyCalendarIn",
        "FreeBusyCalendarOut": "_calendar_7_FreeBusyCalendarOut",
        "CalendarIn": "_calendar_8_CalendarIn",
        "CalendarOut": "_calendar_9_CalendarOut",
        "FreeBusyRequestItemIn": "_calendar_10_FreeBusyRequestItemIn",
        "FreeBusyRequestItemOut": "_calendar_11_FreeBusyRequestItemOut",
        "ConferenceDataIn": "_calendar_12_ConferenceDataIn",
        "ConferenceDataOut": "_calendar_13_ConferenceDataOut",
        "EventAttachmentIn": "_calendar_14_EventAttachmentIn",
        "EventAttachmentOut": "_calendar_15_EventAttachmentOut",
        "EventDateTimeIn": "_calendar_16_EventDateTimeIn",
        "EventDateTimeOut": "_calendar_17_EventDateTimeOut",
        "CalendarNotificationIn": "_calendar_18_CalendarNotificationIn",
        "CalendarNotificationOut": "_calendar_19_CalendarNotificationOut",
        "EntryPointIn": "_calendar_20_EntryPointIn",
        "EntryPointOut": "_calendar_21_EntryPointOut",
        "ColorDefinitionIn": "_calendar_22_ColorDefinitionIn",
        "ColorDefinitionOut": "_calendar_23_ColorDefinitionOut",
        "ConferenceSolutionIn": "_calendar_24_ConferenceSolutionIn",
        "ConferenceSolutionOut": "_calendar_25_ConferenceSolutionOut",
        "CalendarListEntryIn": "_calendar_26_CalendarListEntryIn",
        "CalendarListEntryOut": "_calendar_27_CalendarListEntryOut",
        "FreeBusyGroupIn": "_calendar_28_FreeBusyGroupIn",
        "FreeBusyGroupOut": "_calendar_29_FreeBusyGroupOut",
        "ColorsIn": "_calendar_30_ColorsIn",
        "ColorsOut": "_calendar_31_ColorsOut",
        "SettingsIn": "_calendar_32_SettingsIn",
        "SettingsOut": "_calendar_33_SettingsOut",
        "CalendarListIn": "_calendar_34_CalendarListIn",
        "CalendarListOut": "_calendar_35_CalendarListOut",
        "ConferenceRequestStatusIn": "_calendar_36_ConferenceRequestStatusIn",
        "ConferenceRequestStatusOut": "_calendar_37_ConferenceRequestStatusOut",
        "TimePeriodIn": "_calendar_38_TimePeriodIn",
        "TimePeriodOut": "_calendar_39_TimePeriodOut",
        "ConferenceParametersAddOnParametersIn": "_calendar_40_ConferenceParametersAddOnParametersIn",
        "ConferenceParametersAddOnParametersOut": "_calendar_41_ConferenceParametersAddOnParametersOut",
        "ChannelIn": "_calendar_42_ChannelIn",
        "ChannelOut": "_calendar_43_ChannelOut",
        "ErrorIn": "_calendar_44_ErrorIn",
        "ErrorOut": "_calendar_45_ErrorOut",
        "SettingIn": "_calendar_46_SettingIn",
        "SettingOut": "_calendar_47_SettingOut",
        "EventWorkingLocationPropertiesIn": "_calendar_48_EventWorkingLocationPropertiesIn",
        "EventWorkingLocationPropertiesOut": "_calendar_49_EventWorkingLocationPropertiesOut",
        "EventIn": "_calendar_50_EventIn",
        "EventOut": "_calendar_51_EventOut",
        "CreateConferenceRequestIn": "_calendar_52_CreateConferenceRequestIn",
        "CreateConferenceRequestOut": "_calendar_53_CreateConferenceRequestOut",
        "AclIn": "_calendar_54_AclIn",
        "AclOut": "_calendar_55_AclOut",
        "ConferenceSolutionKeyIn": "_calendar_56_ConferenceSolutionKeyIn",
        "ConferenceSolutionKeyOut": "_calendar_57_ConferenceSolutionKeyOut",
        "EventAttendeeIn": "_calendar_58_EventAttendeeIn",
        "EventAttendeeOut": "_calendar_59_EventAttendeeOut",
        "ConferencePropertiesIn": "_calendar_60_ConferencePropertiesIn",
        "ConferencePropertiesOut": "_calendar_61_ConferencePropertiesOut",
        "AclRuleIn": "_calendar_62_AclRuleIn",
        "AclRuleOut": "_calendar_63_AclRuleOut",
        "ConferenceParametersIn": "_calendar_64_ConferenceParametersIn",
        "ConferenceParametersOut": "_calendar_65_ConferenceParametersOut",
        "EventReminderIn": "_calendar_66_EventReminderIn",
        "EventReminderOut": "_calendar_67_EventReminderOut",
        "EventsIn": "_calendar_68_EventsIn",
        "EventsOut": "_calendar_69_EventsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FreeBusyResponseIn"] = t.struct(
        {
            "groups": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "calendars": t.struct({"_": t.string().optional()}).optional(),
            "timeMin": t.string().optional(),
            "timeMax": t.string().optional(),
        }
    ).named(renames["FreeBusyResponseIn"])
    types["FreeBusyResponseOut"] = t.struct(
        {
            "groups": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "calendars": t.struct({"_": t.string().optional()}).optional(),
            "timeMin": t.string().optional(),
            "timeMax": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyResponseOut"])
    types["FreeBusyRequestIn"] = t.struct(
        {
            "calendarExpansionMax": t.integer().optional(),
            "timeMin": t.string().optional(),
            "timeZone": t.string().optional(),
            "groupExpansionMax": t.integer().optional(),
            "timeMax": t.string().optional(),
            "items": t.array(t.proxy(renames["FreeBusyRequestItemIn"])).optional(),
        }
    ).named(renames["FreeBusyRequestIn"])
    types["FreeBusyRequestOut"] = t.struct(
        {
            "calendarExpansionMax": t.integer().optional(),
            "timeMin": t.string().optional(),
            "timeZone": t.string().optional(),
            "groupExpansionMax": t.integer().optional(),
            "timeMax": t.string().optional(),
            "items": t.array(t.proxy(renames["FreeBusyRequestItemOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyRequestOut"])
    types["FreeBusyCalendarIn"] = t.struct(
        {
            "busy": t.array(t.proxy(renames["TimePeriodIn"])).optional(),
            "errors": t.array(t.proxy(renames["ErrorIn"])).optional(),
        }
    ).named(renames["FreeBusyCalendarIn"])
    types["FreeBusyCalendarOut"] = t.struct(
        {
            "busy": t.array(t.proxy(renames["TimePeriodOut"])).optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyCalendarOut"])
    types["CalendarIn"] = t.struct(
        {
            "id": t.string().optional(),
            "description": t.string().optional(),
            "timeZone": t.string().optional(),
            "kind": t.string().optional(),
            "summary": t.string().optional(),
            "location": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesIn"]
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CalendarIn"])
    types["CalendarOut"] = t.struct(
        {
            "id": t.string().optional(),
            "description": t.string().optional(),
            "timeZone": t.string().optional(),
            "kind": t.string().optional(),
            "summary": t.string().optional(),
            "location": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesOut"]
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarOut"])
    types["FreeBusyRequestItemIn"] = t.struct({"id": t.string().optional()}).named(
        renames["FreeBusyRequestItemIn"]
    )
    types["FreeBusyRequestItemOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyRequestItemOut"])
    types["ConferenceDataIn"] = t.struct(
        {
            "createRequest": t.proxy(renames["CreateConferenceRequestIn"]).optional(),
            "conferenceId": t.string().optional(),
            "parameters": t.proxy(renames["ConferenceParametersIn"]).optional(),
            "conferenceSolution": t.proxy(renames["ConferenceSolutionIn"]).optional(),
            "signature": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointIn"])).optional(),
            "notes": t.string().optional(),
        }
    ).named(renames["ConferenceDataIn"])
    types["ConferenceDataOut"] = t.struct(
        {
            "createRequest": t.proxy(renames["CreateConferenceRequestOut"]).optional(),
            "conferenceId": t.string().optional(),
            "parameters": t.proxy(renames["ConferenceParametersOut"]).optional(),
            "conferenceSolution": t.proxy(renames["ConferenceSolutionOut"]).optional(),
            "signature": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointOut"])).optional(),
            "notes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceDataOut"])
    types["EventAttachmentIn"] = t.struct(
        {
            "title": t.string().optional(),
            "fileUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
            "iconLink": t.string().optional(),
        }
    ).named(renames["EventAttachmentIn"])
    types["EventAttachmentOut"] = t.struct(
        {
            "title": t.string().optional(),
            "fileUrl": t.string().optional(),
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
            "iconLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventAttachmentOut"])
    types["EventDateTimeIn"] = t.struct(
        {
            "date": t.string().optional(),
            "timeZone": t.string().optional(),
            "dateTime": t.string().optional(),
        }
    ).named(renames["EventDateTimeIn"])
    types["EventDateTimeOut"] = t.struct(
        {
            "date": t.string().optional(),
            "timeZone": t.string().optional(),
            "dateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDateTimeOut"])
    types["CalendarNotificationIn"] = t.struct(
        {"method": t.string().optional(), "type": t.string().optional()}
    ).named(renames["CalendarNotificationIn"])
    types["CalendarNotificationOut"] = t.struct(
        {
            "method": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarNotificationOut"])
    types["EntryPointIn"] = t.struct(
        {
            "label": t.string().optional(),
            "accessCode": t.string().optional(),
            "entryPointFeatures": t.array(t.string()).optional(),
            "pin": t.string().optional(),
            "uri": t.string().optional(),
            "password": t.string().optional(),
            "entryPointType": t.string().optional(),
            "passcode": t.string().optional(),
            "meetingCode": t.string().optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["EntryPointIn"])
    types["EntryPointOut"] = t.struct(
        {
            "label": t.string().optional(),
            "accessCode": t.string().optional(),
            "entryPointFeatures": t.array(t.string()).optional(),
            "pin": t.string().optional(),
            "uri": t.string().optional(),
            "password": t.string().optional(),
            "entryPointType": t.string().optional(),
            "passcode": t.string().optional(),
            "meetingCode": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntryPointOut"])
    types["ColorDefinitionIn"] = t.struct(
        {"background": t.string().optional(), "foreground": t.string().optional()}
    ).named(renames["ColorDefinitionIn"])
    types["ColorDefinitionOut"] = t.struct(
        {
            "background": t.string().optional(),
            "foreground": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorDefinitionOut"])
    types["ConferenceSolutionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "iconUri": t.string().optional(),
            "key": t.proxy(renames["ConferenceSolutionKeyIn"]).optional(),
        }
    ).named(renames["ConferenceSolutionIn"])
    types["ConferenceSolutionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "iconUri": t.string().optional(),
            "key": t.proxy(renames["ConferenceSolutionKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceSolutionOut"])
    types["CalendarListEntryIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accessRole": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesIn"]
            ).optional(),
            "foregroundColor": t.string().optional(),
            "timeZone": t.string().optional(),
            "etag": t.string().optional(),
            "colorId": t.string().optional(),
            "summaryOverride": t.string().optional(),
            "hidden": t.boolean().optional(),
            "description": t.string().optional(),
            "summary": t.string().optional(),
            "id": t.string().optional(),
            "notificationSettings": t.struct(
                {
                    "notifications": t.array(
                        t.proxy(renames["CalendarNotificationIn"])
                    ).optional()
                }
            ).optional(),
            "backgroundColor": t.string().optional(),
            "defaultReminders": t.array(t.proxy(renames["EventReminderIn"])).optional(),
            "deleted": t.boolean().optional(),
            "primary": t.boolean().optional(),
            "selected": t.boolean().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["CalendarListEntryIn"])
    types["CalendarListEntryOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accessRole": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesOut"]
            ).optional(),
            "foregroundColor": t.string().optional(),
            "timeZone": t.string().optional(),
            "etag": t.string().optional(),
            "colorId": t.string().optional(),
            "summaryOverride": t.string().optional(),
            "hidden": t.boolean().optional(),
            "description": t.string().optional(),
            "summary": t.string().optional(),
            "id": t.string().optional(),
            "notificationSettings": t.struct(
                {
                    "notifications": t.array(
                        t.proxy(renames["CalendarNotificationOut"])
                    ).optional()
                }
            ).optional(),
            "backgroundColor": t.string().optional(),
            "defaultReminders": t.array(
                t.proxy(renames["EventReminderOut"])
            ).optional(),
            "deleted": t.boolean().optional(),
            "primary": t.boolean().optional(),
            "selected": t.boolean().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarListEntryOut"])
    types["FreeBusyGroupIn"] = t.struct(
        {
            "calendars": t.array(t.string()).optional(),
            "errors": t.array(t.proxy(renames["ErrorIn"])).optional(),
        }
    ).named(renames["FreeBusyGroupIn"])
    types["FreeBusyGroupOut"] = t.struct(
        {
            "calendars": t.array(t.string()).optional(),
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyGroupOut"])
    types["ColorsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "calendar": t.struct({"_": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "event": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ColorsIn"])
    types["ColorsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "calendar": t.struct({"_": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "event": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorsOut"])
    types["SettingsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SettingIn"])).optional(),
            "kind": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["SettingOut"])).optional(),
            "kind": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["CalendarListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CalendarListEntryIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CalendarListIn"])
    types["CalendarListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CalendarListEntryOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarListOut"])
    types["ConferenceRequestStatusIn"] = t.struct(
        {"statusCode": t.string().optional()}
    ).named(renames["ConferenceRequestStatusIn"])
    types["ConferenceRequestStatusOut"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceRequestStatusOut"])
    types["TimePeriodIn"] = t.struct(
        {"end": t.string().optional(), "start": t.string().optional()}
    ).named(renames["TimePeriodIn"])
    types["TimePeriodOut"] = t.struct(
        {
            "end": t.string().optional(),
            "start": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimePeriodOut"])
    types["ConferenceParametersAddOnParametersIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()})}
    ).named(renames["ConferenceParametersAddOnParametersIn"])
    types["ConferenceParametersAddOnParametersOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceParametersAddOnParametersOut"])
    types["ChannelIn"] = t.struct(
        {
            "id": t.string().optional(),
            "type": t.string().optional(),
            "resourceId": t.string().optional(),
            "address": t.string().optional(),
            "payload": t.boolean().optional(),
            "kind": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "token": t.string().optional(),
            "expiration": t.string().optional(),
            "resourceUri": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "id": t.string().optional(),
            "type": t.string().optional(),
            "resourceId": t.string().optional(),
            "address": t.string().optional(),
            "payload": t.boolean().optional(),
            "kind": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "token": t.string().optional(),
            "expiration": t.string().optional(),
            "resourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["ErrorIn"] = t.struct(
        {"domain": t.string().optional(), "reason": t.string().optional()}
    ).named(renames["ErrorIn"])
    types["ErrorOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorOut"])
    types["SettingIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["SettingIn"])
    types["SettingOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingOut"])
    types["EventWorkingLocationPropertiesIn"] = t.struct(
        {
            "customLocation": t.struct({"label": t.string().optional()}).optional(),
            "homeOffice": t.struct({"_": t.string().optional()}).optional(),
            "officeLocation": t.struct(
                {
                    "label": t.string().optional(),
                    "deskId": t.string().optional(),
                    "buildingId": t.string().optional(),
                    "floorSectionId": t.string().optional(),
                    "floorId": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["EventWorkingLocationPropertiesIn"])
    types["EventWorkingLocationPropertiesOut"] = t.struct(
        {
            "customLocation": t.struct({"label": t.string().optional()}).optional(),
            "homeOffice": t.struct({"_": t.string().optional()}).optional(),
            "officeLocation": t.struct(
                {
                    "label": t.string().optional(),
                    "deskId": t.string().optional(),
                    "buildingId": t.string().optional(),
                    "floorSectionId": t.string().optional(),
                    "floorId": t.string().optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventWorkingLocationPropertiesOut"])
    types["EventIn"] = t.struct(
        {
            "endTimeUnspecified": t.boolean().optional(),
            "colorId": t.string().optional(),
            "updated": t.string().optional(),
            "guestsCanSeeOtherGuests": t.boolean().optional(),
            "anyoneCanAddSelf": t.boolean().optional(),
            "attendeesOmitted": t.boolean().optional(),
            "gadget": t.struct(
                {
                    "display": t.string().optional(),
                    "width": t.integer().optional(),
                    "type": t.string().optional(),
                    "link": t.string().optional(),
                    "title": t.string().optional(),
                    "preferences": t.struct({"_": t.string().optional()}).optional(),
                    "height": t.integer().optional(),
                    "iconLink": t.string().optional(),
                }
            ).optional(),
            "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
            "sequence": t.integer().optional(),
            "guestsCanInviteOthers": t.boolean().optional(),
            "eventType": t.string().optional(),
            "attachments": t.array(t.proxy(renames["EventAttachmentIn"])).optional(),
            "creator": t.struct(
                {
                    "email": t.string().optional(),
                    "id": t.string().optional(),
                    "self": t.boolean().optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "recurrence": t.array(t.string()).optional(),
            "transparency": t.string().optional(),
            "source": t.struct(
                {"title": t.string().optional(), "url": t.string().optional()}
            ).optional(),
            "hangoutLink": t.string().optional(),
            "organizer": t.struct(
                {
                    "displayName": t.string().optional(),
                    "id": t.string().optional(),
                    "self": t.boolean().optional(),
                    "email": t.string().optional(),
                }
            ).optional(),
            "start": t.proxy(renames["EventDateTimeIn"]).optional(),
            "summary": t.string().optional(),
            "iCalUID": t.string().optional(),
            "reminders": t.struct(
                {
                    "overrides": t.array(
                        t.proxy(renames["EventReminderIn"])
                    ).optional(),
                    "useDefault": t.boolean().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
            "end": t.proxy(renames["EventDateTimeIn"]).optional(),
            "locked": t.boolean().optional(),
            "guestsCanModify": t.boolean().optional(),
            "recurringEventId": t.string().optional(),
            "workingLocationProperties": t.proxy(
                renames["EventWorkingLocationPropertiesIn"]
            ).optional(),
            "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
            "privateCopy": t.boolean().optional(),
            "etag": t.string().optional(),
            "htmlLink": t.string().optional(),
            "description": t.string().optional(),
            "created": t.string().optional(),
            "visibility": t.string().optional(),
            "extendedProperties": t.struct(
                {
                    "private": t.struct({"_": t.string().optional()}).optional(),
                    "shared": t.struct({"_": t.string().optional()}).optional(),
                }
            ).optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "endTimeUnspecified": t.boolean().optional(),
            "colorId": t.string().optional(),
            "updated": t.string().optional(),
            "guestsCanSeeOtherGuests": t.boolean().optional(),
            "anyoneCanAddSelf": t.boolean().optional(),
            "attendeesOmitted": t.boolean().optional(),
            "gadget": t.struct(
                {
                    "display": t.string().optional(),
                    "width": t.integer().optional(),
                    "type": t.string().optional(),
                    "link": t.string().optional(),
                    "title": t.string().optional(),
                    "preferences": t.struct({"_": t.string().optional()}).optional(),
                    "height": t.integer().optional(),
                    "iconLink": t.string().optional(),
                }
            ).optional(),
            "originalStartTime": t.proxy(renames["EventDateTimeOut"]).optional(),
            "sequence": t.integer().optional(),
            "guestsCanInviteOthers": t.boolean().optional(),
            "eventType": t.string().optional(),
            "attachments": t.array(t.proxy(renames["EventAttachmentOut"])).optional(),
            "creator": t.struct(
                {
                    "email": t.string().optional(),
                    "id": t.string().optional(),
                    "self": t.boolean().optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "recurrence": t.array(t.string()).optional(),
            "transparency": t.string().optional(),
            "source": t.struct(
                {"title": t.string().optional(), "url": t.string().optional()}
            ).optional(),
            "hangoutLink": t.string().optional(),
            "organizer": t.struct(
                {
                    "displayName": t.string().optional(),
                    "id": t.string().optional(),
                    "self": t.boolean().optional(),
                    "email": t.string().optional(),
                }
            ).optional(),
            "start": t.proxy(renames["EventDateTimeOut"]).optional(),
            "summary": t.string().optional(),
            "iCalUID": t.string().optional(),
            "reminders": t.struct(
                {
                    "overrides": t.array(
                        t.proxy(renames["EventReminderOut"])
                    ).optional(),
                    "useDefault": t.boolean().optional(),
                }
            ).optional(),
            "status": t.string().optional(),
            "kind": t.string().optional(),
            "end": t.proxy(renames["EventDateTimeOut"]).optional(),
            "locked": t.boolean().optional(),
            "guestsCanModify": t.boolean().optional(),
            "recurringEventId": t.string().optional(),
            "workingLocationProperties": t.proxy(
                renames["EventWorkingLocationPropertiesOut"]
            ).optional(),
            "conferenceData": t.proxy(renames["ConferenceDataOut"]).optional(),
            "location": t.string().optional(),
            "id": t.string().optional(),
            "attendees": t.array(t.proxy(renames["EventAttendeeOut"])).optional(),
            "privateCopy": t.boolean().optional(),
            "etag": t.string().optional(),
            "htmlLink": t.string().optional(),
            "description": t.string().optional(),
            "created": t.string().optional(),
            "visibility": t.string().optional(),
            "extendedProperties": t.struct(
                {
                    "private": t.struct({"_": t.string().optional()}).optional(),
                    "shared": t.struct({"_": t.string().optional()}).optional(),
                }
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["CreateConferenceRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "status": t.proxy(renames["ConferenceRequestStatusIn"]).optional(),
            "conferenceSolutionKey": t.proxy(
                renames["ConferenceSolutionKeyIn"]
            ).optional(),
        }
    ).named(renames["CreateConferenceRequestIn"])
    types["CreateConferenceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "status": t.proxy(renames["ConferenceRequestStatusOut"]).optional(),
            "conferenceSolutionKey": t.proxy(
                renames["ConferenceSolutionKeyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateConferenceRequestOut"])
    types["AclIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AclRuleIn"])).optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AclIn"])
    types["AclOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["AclRuleOut"])).optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclOut"])
    types["ConferenceSolutionKeyIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ConferenceSolutionKeyIn"]
    )
    types["ConferenceSolutionKeyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceSolutionKeyOut"])
    types["EventAttendeeIn"] = t.struct(
        {
            "responseStatus": t.string().optional(),
            "additionalGuests": t.integer().optional(),
            "email": t.string().optional(),
            "comment": t.string().optional(),
            "self": t.boolean().optional(),
            "resource": t.boolean().optional(),
            "id": t.string().optional(),
            "organizer": t.boolean().optional(),
            "displayName": t.string().optional(),
            "optional": t.boolean().optional(),
        }
    ).named(renames["EventAttendeeIn"])
    types["EventAttendeeOut"] = t.struct(
        {
            "responseStatus": t.string().optional(),
            "additionalGuests": t.integer().optional(),
            "email": t.string().optional(),
            "comment": t.string().optional(),
            "self": t.boolean().optional(),
            "resource": t.boolean().optional(),
            "id": t.string().optional(),
            "organizer": t.boolean().optional(),
            "displayName": t.string().optional(),
            "optional": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventAttendeeOut"])
    types["ConferencePropertiesIn"] = t.struct(
        {"allowedConferenceSolutionTypes": t.array(t.string()).optional()}
    ).named(renames["ConferencePropertiesIn"])
    types["ConferencePropertiesOut"] = t.struct(
        {
            "allowedConferenceSolutionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferencePropertiesOut"])
    types["AclRuleIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "scope": t.struct(
                {"type": t.string().optional(), "value": t.string().optional()}
            ).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["AclRuleIn"])
    types["AclRuleOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "scope": t.struct(
                {"type": t.string().optional(), "value": t.string().optional()}
            ).optional(),
            "id": t.string().optional(),
            "etag": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclRuleOut"])
    types["ConferenceParametersIn"] = t.struct(
        {
            "addOnParameters": t.proxy(
                renames["ConferenceParametersAddOnParametersIn"]
            ).optional()
        }
    ).named(renames["ConferenceParametersIn"])
    types["ConferenceParametersOut"] = t.struct(
        {
            "addOnParameters": t.proxy(
                renames["ConferenceParametersAddOnParametersOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceParametersOut"])
    types["EventReminderIn"] = t.struct(
        {"minutes": t.integer().optional(), "method": t.string().optional()}
    ).named(renames["EventReminderIn"])
    types["EventReminderOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventReminderOut"])
    types["EventsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "accessRole": t.string().optional(),
            "etag": t.string().optional(),
            "defaultReminders": t.array(t.proxy(renames["EventReminderIn"])).optional(),
            "summary": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "timeZone": t.string().optional(),
            "updated": t.string().optional(),
            "description": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "items": t.array(t.proxy(renames["EventIn"])).optional(),
        }
    ).named(renames["EventsIn"])
    types["EventsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "accessRole": t.string().optional(),
            "etag": t.string().optional(),
            "defaultReminders": t.array(
                t.proxy(renames["EventReminderOut"])
            ).optional(),
            "summary": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "timeZone": t.string().optional(),
            "updated": t.string().optional(),
            "description": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "items": t.array(t.proxy(renames["EventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventsOut"])

    functions = {}
    functions["eventsDelete"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsMove"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsInstances"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsPatch"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsList"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsImport"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsGet"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsQuickAdd"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsWatch"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsInsert"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsUpdate"] = calendar.put(
        "calendars/{calendarId}/events/{eventId}",
        t.struct(
            {
                "sendUpdates": t.string().optional(),
                "calendarId": t.string().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "sendNotifications": t.boolean().optional(),
                "eventId": t.string().optional(),
                "alwaysIncludeEmail": t.boolean().optional(),
                "supportsAttachments": t.boolean().optional(),
                "maxAttendees": t.integer().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "colorId": t.string().optional(),
                "updated": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "attendeesOmitted": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "width": t.integer().optional(),
                        "type": t.string().optional(),
                        "link": t.string().optional(),
                        "title": t.string().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "height": t.integer().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "sequence": t.integer().optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "eventType": t.string().optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "recurrence": t.array(t.string()).optional(),
                "transparency": t.string().optional(),
                "source": t.struct(
                    {"title": t.string().optional(), "url": t.string().optional()}
                ).optional(),
                "hangoutLink": t.string().optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "id": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                    }
                ).optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "summary": t.string().optional(),
                "iCalUID": t.string().optional(),
                "reminders": t.struct(
                    {
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                        "useDefault": t.boolean().optional(),
                    }
                ).optional(),
                "status": t.string().optional(),
                "kind": t.string().optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "guestsCanModify": t.boolean().optional(),
                "recurringEventId": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "location": t.string().optional(),
                "id": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "privateCopy": t.boolean().optional(),
                "etag": t.string().optional(),
                "htmlLink": t.string().optional(),
                "description": t.string().optional(),
                "created": t.string().optional(),
                "visibility": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "private": t.struct({"_": t.string().optional()}).optional(),
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["colorsGet"] = calendar.get(
        "colors",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["ColorsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["freebusyQuery"] = calendar.post(
        "freeBusy",
        t.struct(
            {
                "calendarExpansionMax": t.integer().optional(),
                "timeMin": t.string().optional(),
                "timeZone": t.string().optional(),
                "groupExpansionMax": t.integer().optional(),
                "timeMax": t.string().optional(),
                "items": t.array(t.proxy(renames["FreeBusyRequestItemIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FreeBusyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListList"] = calendar.get(
        "users/me/calendarList/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarListEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListWatch"] = calendar.get(
        "users/me/calendarList/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarListEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListInsert"] = calendar.get(
        "users/me/calendarList/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarListEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListUpdate"] = calendar.get(
        "users/me/calendarList/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarListEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListDelete"] = calendar.get(
        "users/me/calendarList/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarListEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListPatch"] = calendar.get(
        "users/me/calendarList/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarListEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListGet"] = calendar.get(
        "users/me/calendarList/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarListEntryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclPatch"] = calendar.post(
        "calendars/{calendarId}/acl",
        t.struct(
            {
                "sendNotifications": t.boolean().optional(),
                "calendarId": t.string().optional(),
                "kind": t.string().optional(),
                "scope": t.struct(
                    {"type": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AclRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclGet"] = calendar.post(
        "calendars/{calendarId}/acl",
        t.struct(
            {
                "sendNotifications": t.boolean().optional(),
                "calendarId": t.string().optional(),
                "kind": t.string().optional(),
                "scope": t.struct(
                    {"type": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AclRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclWatch"] = calendar.post(
        "calendars/{calendarId}/acl",
        t.struct(
            {
                "sendNotifications": t.boolean().optional(),
                "calendarId": t.string().optional(),
                "kind": t.string().optional(),
                "scope": t.struct(
                    {"type": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AclRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclUpdate"] = calendar.post(
        "calendars/{calendarId}/acl",
        t.struct(
            {
                "sendNotifications": t.boolean().optional(),
                "calendarId": t.string().optional(),
                "kind": t.string().optional(),
                "scope": t.struct(
                    {"type": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AclRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclDelete"] = calendar.post(
        "calendars/{calendarId}/acl",
        t.struct(
            {
                "sendNotifications": t.boolean().optional(),
                "calendarId": t.string().optional(),
                "kind": t.string().optional(),
                "scope": t.struct(
                    {"type": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AclRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclList"] = calendar.post(
        "calendars/{calendarId}/acl",
        t.struct(
            {
                "sendNotifications": t.boolean().optional(),
                "calendarId": t.string().optional(),
                "kind": t.string().optional(),
                "scope": t.struct(
                    {"type": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AclRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclInsert"] = calendar.post(
        "calendars/{calendarId}/acl",
        t.struct(
            {
                "sendNotifications": t.boolean().optional(),
                "calendarId": t.string().optional(),
                "kind": t.string().optional(),
                "scope": t.struct(
                    {"type": t.string().optional(), "value": t.string().optional()}
                ).optional(),
                "id": t.string().optional(),
                "etag": t.string().optional(),
                "role": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AclRuleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsStop"] = calendar.post(
        "channels/stop",
        t.struct(
            {
                "id": t.string().optional(),
                "type": t.string().optional(),
                "resourceId": t.string().optional(),
                "address": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "token": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsList"] = calendar.get(
        "users/me/settings/{setting}",
        t.struct({"setting": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsWatch"] = calendar.get(
        "users/me/settings/{setting}",
        t.struct({"setting": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsGet"] = calendar.get(
        "users/me/settings/{setting}",
        t.struct({"setting": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SettingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsInsert"] = calendar.delete(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsClear"] = calendar.delete(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsUpdate"] = calendar.delete(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsGet"] = calendar.delete(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsPatch"] = calendar.delete(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsDelete"] = calendar.delete(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="calendar", renames=renames, types=Box(types), functions=Box(functions)
    )
