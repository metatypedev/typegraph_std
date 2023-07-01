from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_calendar():
    calendar = HTTPRuntime("https://www.googleapis.com/")

    renames = {
        "ErrorResponse": "_calendar_1_ErrorResponse",
        "TimePeriodIn": "_calendar_2_TimePeriodIn",
        "TimePeriodOut": "_calendar_3_TimePeriodOut",
        "ConferenceParametersAddOnParametersIn": "_calendar_4_ConferenceParametersAddOnParametersIn",
        "ConferenceParametersAddOnParametersOut": "_calendar_5_ConferenceParametersAddOnParametersOut",
        "FreeBusyGroupIn": "_calendar_6_FreeBusyGroupIn",
        "FreeBusyGroupOut": "_calendar_7_FreeBusyGroupOut",
        "EventAttendeeIn": "_calendar_8_EventAttendeeIn",
        "EventAttendeeOut": "_calendar_9_EventAttendeeOut",
        "EntryPointIn": "_calendar_10_EntryPointIn",
        "EntryPointOut": "_calendar_11_EntryPointOut",
        "CalendarNotificationIn": "_calendar_12_CalendarNotificationIn",
        "CalendarNotificationOut": "_calendar_13_CalendarNotificationOut",
        "ConferencePropertiesIn": "_calendar_14_ConferencePropertiesIn",
        "ConferencePropertiesOut": "_calendar_15_ConferencePropertiesOut",
        "SettingIn": "_calendar_16_SettingIn",
        "SettingOut": "_calendar_17_SettingOut",
        "EventsIn": "_calendar_18_EventsIn",
        "EventsOut": "_calendar_19_EventsOut",
        "ChannelIn": "_calendar_20_ChannelIn",
        "ChannelOut": "_calendar_21_ChannelOut",
        "ConferenceRequestStatusIn": "_calendar_22_ConferenceRequestStatusIn",
        "ConferenceRequestStatusOut": "_calendar_23_ConferenceRequestStatusOut",
        "AclRuleIn": "_calendar_24_AclRuleIn",
        "AclRuleOut": "_calendar_25_AclRuleOut",
        "CalendarIn": "_calendar_26_CalendarIn",
        "CalendarOut": "_calendar_27_CalendarOut",
        "EventReminderIn": "_calendar_28_EventReminderIn",
        "EventReminderOut": "_calendar_29_EventReminderOut",
        "FreeBusyRequestItemIn": "_calendar_30_FreeBusyRequestItemIn",
        "FreeBusyRequestItemOut": "_calendar_31_FreeBusyRequestItemOut",
        "EventIn": "_calendar_32_EventIn",
        "EventOut": "_calendar_33_EventOut",
        "ConferenceDataIn": "_calendar_34_ConferenceDataIn",
        "ConferenceDataOut": "_calendar_35_ConferenceDataOut",
        "CalendarListEntryIn": "_calendar_36_CalendarListEntryIn",
        "CalendarListEntryOut": "_calendar_37_CalendarListEntryOut",
        "FreeBusyResponseIn": "_calendar_38_FreeBusyResponseIn",
        "FreeBusyResponseOut": "_calendar_39_FreeBusyResponseOut",
        "ColorsIn": "_calendar_40_ColorsIn",
        "ColorsOut": "_calendar_41_ColorsOut",
        "ErrorIn": "_calendar_42_ErrorIn",
        "ErrorOut": "_calendar_43_ErrorOut",
        "FreeBusyRequestIn": "_calendar_44_FreeBusyRequestIn",
        "FreeBusyRequestOut": "_calendar_45_FreeBusyRequestOut",
        "ConferenceSolutionKeyIn": "_calendar_46_ConferenceSolutionKeyIn",
        "ConferenceSolutionKeyOut": "_calendar_47_ConferenceSolutionKeyOut",
        "EventAttachmentIn": "_calendar_48_EventAttachmentIn",
        "EventAttachmentOut": "_calendar_49_EventAttachmentOut",
        "CalendarListIn": "_calendar_50_CalendarListIn",
        "CalendarListOut": "_calendar_51_CalendarListOut",
        "AclIn": "_calendar_52_AclIn",
        "AclOut": "_calendar_53_AclOut",
        "EventDateTimeIn": "_calendar_54_EventDateTimeIn",
        "EventDateTimeOut": "_calendar_55_EventDateTimeOut",
        "CreateConferenceRequestIn": "_calendar_56_CreateConferenceRequestIn",
        "CreateConferenceRequestOut": "_calendar_57_CreateConferenceRequestOut",
        "ConferenceParametersIn": "_calendar_58_ConferenceParametersIn",
        "ConferenceParametersOut": "_calendar_59_ConferenceParametersOut",
        "FreeBusyCalendarIn": "_calendar_60_FreeBusyCalendarIn",
        "FreeBusyCalendarOut": "_calendar_61_FreeBusyCalendarOut",
        "EventWorkingLocationPropertiesIn": "_calendar_62_EventWorkingLocationPropertiesIn",
        "EventWorkingLocationPropertiesOut": "_calendar_63_EventWorkingLocationPropertiesOut",
        "ColorDefinitionIn": "_calendar_64_ColorDefinitionIn",
        "ColorDefinitionOut": "_calendar_65_ColorDefinitionOut",
        "SettingsIn": "_calendar_66_SettingsIn",
        "SettingsOut": "_calendar_67_SettingsOut",
        "ConferenceSolutionIn": "_calendar_68_ConferenceSolutionIn",
        "ConferenceSolutionOut": "_calendar_69_ConferenceSolutionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["FreeBusyGroupIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ErrorIn"])).optional(),
            "calendars": t.array(t.string()).optional(),
        }
    ).named(renames["FreeBusyGroupIn"])
    types["FreeBusyGroupOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["ErrorOut"])).optional(),
            "calendars": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyGroupOut"])
    types["EventAttendeeIn"] = t.struct(
        {
            "additionalGuests": t.integer().optional(),
            "id": t.string().optional(),
            "comment": t.string().optional(),
            "optional": t.boolean().optional(),
            "email": t.string().optional(),
            "responseStatus": t.string().optional(),
            "resource": t.boolean().optional(),
            "self": t.boolean().optional(),
            "organizer": t.boolean().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["EventAttendeeIn"])
    types["EventAttendeeOut"] = t.struct(
        {
            "additionalGuests": t.integer().optional(),
            "id": t.string().optional(),
            "comment": t.string().optional(),
            "optional": t.boolean().optional(),
            "email": t.string().optional(),
            "responseStatus": t.string().optional(),
            "resource": t.boolean().optional(),
            "self": t.boolean().optional(),
            "organizer": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventAttendeeOut"])
    types["EntryPointIn"] = t.struct(
        {
            "meetingCode": t.string().optional(),
            "entryPointType": t.string().optional(),
            "pin": t.string().optional(),
            "accessCode": t.string().optional(),
            "uri": t.string().optional(),
            "password": t.string().optional(),
            "passcode": t.string().optional(),
            "entryPointFeatures": t.array(t.string()).optional(),
            "label": t.string().optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["EntryPointIn"])
    types["EntryPointOut"] = t.struct(
        {
            "meetingCode": t.string().optional(),
            "entryPointType": t.string().optional(),
            "pin": t.string().optional(),
            "accessCode": t.string().optional(),
            "uri": t.string().optional(),
            "password": t.string().optional(),
            "passcode": t.string().optional(),
            "entryPointFeatures": t.array(t.string()).optional(),
            "label": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntryPointOut"])
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
    types["ConferencePropertiesIn"] = t.struct(
        {"allowedConferenceSolutionTypes": t.array(t.string()).optional()}
    ).named(renames["ConferencePropertiesIn"])
    types["ConferencePropertiesOut"] = t.struct(
        {
            "allowedConferenceSolutionTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferencePropertiesOut"])
    types["SettingIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["SettingIn"])
    types["SettingOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingOut"])
    types["EventsIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "summary": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "defaultReminders": t.array(t.proxy(renames["EventReminderIn"])).optional(),
            "nextSyncToken": t.string().optional(),
            "items": t.array(t.proxy(renames["EventIn"])).optional(),
            "accessRole": t.string().optional(),
            "timeZone": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["EventsIn"])
    types["EventsOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "summary": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "updated": t.string().optional(),
            "kind": t.string().optional(),
            "defaultReminders": t.array(
                t.proxy(renames["EventReminderOut"])
            ).optional(),
            "nextSyncToken": t.string().optional(),
            "items": t.array(t.proxy(renames["EventOut"])).optional(),
            "accessRole": t.string().optional(),
            "timeZone": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventsOut"])
    types["ChannelIn"] = t.struct(
        {
            "token": t.string().optional(),
            "payload": t.boolean().optional(),
            "kind": t.string().optional(),
            "address": t.string().optional(),
            "resourceUri": t.string().optional(),
            "expiration": t.string().optional(),
            "resourceId": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "token": t.string().optional(),
            "payload": t.boolean().optional(),
            "kind": t.string().optional(),
            "address": t.string().optional(),
            "resourceUri": t.string().optional(),
            "expiration": t.string().optional(),
            "resourceId": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["ConferenceRequestStatusIn"] = t.struct(
        {"statusCode": t.string().optional()}
    ).named(renames["ConferenceRequestStatusIn"])
    types["ConferenceRequestStatusOut"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceRequestStatusOut"])
    types["AclRuleIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "role": t.string().optional(),
            "scope": t.struct(
                {"type": t.string().optional(), "value": t.string().optional()}
            ).optional(),
        }
    ).named(renames["AclRuleIn"])
    types["AclRuleOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "role": t.string().optional(),
            "scope": t.struct(
                {"type": t.string().optional(), "value": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclRuleOut"])
    types["CalendarIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "description": t.string().optional(),
            "summary": t.string().optional(),
            "location": t.string().optional(),
            "kind": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesIn"]
            ).optional(),
            "timeZone": t.string().optional(),
        }
    ).named(renames["CalendarIn"])
    types["CalendarOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "description": t.string().optional(),
            "summary": t.string().optional(),
            "location": t.string().optional(),
            "kind": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesOut"]
            ).optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarOut"])
    types["EventReminderIn"] = t.struct(
        {"method": t.string().optional(), "minutes": t.integer().optional()}
    ).named(renames["EventReminderIn"])
    types["EventReminderOut"] = t.struct(
        {
            "method": t.string().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventReminderOut"])
    types["FreeBusyRequestItemIn"] = t.struct({"id": t.string().optional()}).named(
        renames["FreeBusyRequestItemIn"]
    )
    types["FreeBusyRequestItemOut"] = t.struct(
        {
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyRequestItemOut"])
    types["EventIn"] = t.struct(
        {
            "hangoutLink": t.string().optional(),
            "htmlLink": t.string().optional(),
            "updated": t.string().optional(),
            "reminders": t.struct(
                {
                    "useDefault": t.boolean().optional(),
                    "overrides": t.array(
                        t.proxy(renames["EventReminderIn"])
                    ).optional(),
                }
            ).optional(),
            "etag": t.string().optional(),
            "privateCopy": t.boolean().optional(),
            "kind": t.string().optional(),
            "workingLocationProperties": t.proxy(
                renames["EventWorkingLocationPropertiesIn"]
            ).optional(),
            "recurringEventId": t.string().optional(),
            "eventType": t.string().optional(),
            "description": t.string().optional(),
            "status": t.string().optional(),
            "extendedProperties": t.struct(
                {
                    "shared": t.struct({"_": t.string().optional()}).optional(),
                    "private": t.struct({"_": t.string().optional()}).optional(),
                }
            ).optional(),
            "attendeesOmitted": t.boolean().optional(),
            "endTimeUnspecified": t.boolean().optional(),
            "summary": t.string().optional(),
            "start": t.proxy(renames["EventDateTimeIn"]).optional(),
            "recurrence": t.array(t.string()).optional(),
            "iCalUID": t.string().optional(),
            "created": t.string().optional(),
            "source": t.struct(
                {"url": t.string().optional(), "title": t.string().optional()}
            ).optional(),
            "guestsCanInviteOthers": t.boolean().optional(),
            "creator": t.struct(
                {
                    "email": t.string().optional(),
                    "self": t.boolean().optional(),
                    "id": t.string().optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "end": t.proxy(renames["EventDateTimeIn"]).optional(),
            "organizer": t.struct(
                {
                    "displayName": t.string().optional(),
                    "self": t.boolean().optional(),
                    "email": t.string().optional(),
                    "id": t.string().optional(),
                }
            ).optional(),
            "attachments": t.array(t.proxy(renames["EventAttachmentIn"])).optional(),
            "location": t.string().optional(),
            "anyoneCanAddSelf": t.boolean().optional(),
            "gadget": t.struct(
                {
                    "display": t.string().optional(),
                    "type": t.string().optional(),
                    "height": t.integer().optional(),
                    "link": t.string().optional(),
                    "width": t.integer().optional(),
                    "preferences": t.struct({"_": t.string().optional()}).optional(),
                    "title": t.string().optional(),
                    "iconLink": t.string().optional(),
                }
            ).optional(),
            "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
            "locked": t.boolean().optional(),
            "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
            "guestsCanModify": t.boolean().optional(),
            "transparency": t.string().optional(),
            "sequence": t.integer().optional(),
            "id": t.string().optional(),
            "visibility": t.string().optional(),
            "guestsCanSeeOtherGuests": t.boolean().optional(),
            "colorId": t.string().optional(),
            "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
        }
    ).named(renames["EventIn"])
    types["EventOut"] = t.struct(
        {
            "hangoutLink": t.string().optional(),
            "htmlLink": t.string().optional(),
            "updated": t.string().optional(),
            "reminders": t.struct(
                {
                    "useDefault": t.boolean().optional(),
                    "overrides": t.array(
                        t.proxy(renames["EventReminderOut"])
                    ).optional(),
                }
            ).optional(),
            "etag": t.string().optional(),
            "privateCopy": t.boolean().optional(),
            "kind": t.string().optional(),
            "workingLocationProperties": t.proxy(
                renames["EventWorkingLocationPropertiesOut"]
            ).optional(),
            "recurringEventId": t.string().optional(),
            "eventType": t.string().optional(),
            "description": t.string().optional(),
            "status": t.string().optional(),
            "extendedProperties": t.struct(
                {
                    "shared": t.struct({"_": t.string().optional()}).optional(),
                    "private": t.struct({"_": t.string().optional()}).optional(),
                }
            ).optional(),
            "attendeesOmitted": t.boolean().optional(),
            "endTimeUnspecified": t.boolean().optional(),
            "summary": t.string().optional(),
            "start": t.proxy(renames["EventDateTimeOut"]).optional(),
            "recurrence": t.array(t.string()).optional(),
            "iCalUID": t.string().optional(),
            "created": t.string().optional(),
            "source": t.struct(
                {"url": t.string().optional(), "title": t.string().optional()}
            ).optional(),
            "guestsCanInviteOthers": t.boolean().optional(),
            "creator": t.struct(
                {
                    "email": t.string().optional(),
                    "self": t.boolean().optional(),
                    "id": t.string().optional(),
                    "displayName": t.string().optional(),
                }
            ).optional(),
            "end": t.proxy(renames["EventDateTimeOut"]).optional(),
            "organizer": t.struct(
                {
                    "displayName": t.string().optional(),
                    "self": t.boolean().optional(),
                    "email": t.string().optional(),
                    "id": t.string().optional(),
                }
            ).optional(),
            "attachments": t.array(t.proxy(renames["EventAttachmentOut"])).optional(),
            "location": t.string().optional(),
            "anyoneCanAddSelf": t.boolean().optional(),
            "gadget": t.struct(
                {
                    "display": t.string().optional(),
                    "type": t.string().optional(),
                    "height": t.integer().optional(),
                    "link": t.string().optional(),
                    "width": t.integer().optional(),
                    "preferences": t.struct({"_": t.string().optional()}).optional(),
                    "title": t.string().optional(),
                    "iconLink": t.string().optional(),
                }
            ).optional(),
            "originalStartTime": t.proxy(renames["EventDateTimeOut"]).optional(),
            "locked": t.boolean().optional(),
            "conferenceData": t.proxy(renames["ConferenceDataOut"]).optional(),
            "guestsCanModify": t.boolean().optional(),
            "transparency": t.string().optional(),
            "sequence": t.integer().optional(),
            "id": t.string().optional(),
            "visibility": t.string().optional(),
            "guestsCanSeeOtherGuests": t.boolean().optional(),
            "colorId": t.string().optional(),
            "attendees": t.array(t.proxy(renames["EventAttendeeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventOut"])
    types["ConferenceDataIn"] = t.struct(
        {
            "conferenceId": t.string().optional(),
            "signature": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointIn"])).optional(),
            "conferenceSolution": t.proxy(renames["ConferenceSolutionIn"]).optional(),
            "notes": t.string().optional(),
            "createRequest": t.proxy(renames["CreateConferenceRequestIn"]).optional(),
            "parameters": t.proxy(renames["ConferenceParametersIn"]).optional(),
        }
    ).named(renames["ConferenceDataIn"])
    types["ConferenceDataOut"] = t.struct(
        {
            "conferenceId": t.string().optional(),
            "signature": t.string().optional(),
            "entryPoints": t.array(t.proxy(renames["EntryPointOut"])).optional(),
            "conferenceSolution": t.proxy(renames["ConferenceSolutionOut"]).optional(),
            "notes": t.string().optional(),
            "createRequest": t.proxy(renames["CreateConferenceRequestOut"]).optional(),
            "parameters": t.proxy(renames["ConferenceParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceDataOut"])
    types["CalendarListEntryIn"] = t.struct(
        {
            "id": t.string().optional(),
            "description": t.string().optional(),
            "colorId": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesIn"]
            ).optional(),
            "primary": t.boolean().optional(),
            "backgroundColor": t.string().optional(),
            "accessRole": t.string().optional(),
            "location": t.string().optional(),
            "defaultReminders": t.array(t.proxy(renames["EventReminderIn"])).optional(),
            "summary": t.string().optional(),
            "etag": t.string().optional(),
            "summaryOverride": t.string().optional(),
            "timeZone": t.string().optional(),
            "deleted": t.boolean().optional(),
            "notificationSettings": t.struct(
                {
                    "notifications": t.array(
                        t.proxy(renames["CalendarNotificationIn"])
                    ).optional()
                }
            ).optional(),
            "hidden": t.boolean().optional(),
            "kind": t.string().optional(),
            "foregroundColor": t.string().optional(),
            "selected": t.boolean().optional(),
        }
    ).named(renames["CalendarListEntryIn"])
    types["CalendarListEntryOut"] = t.struct(
        {
            "id": t.string().optional(),
            "description": t.string().optional(),
            "colorId": t.string().optional(),
            "conferenceProperties": t.proxy(
                renames["ConferencePropertiesOut"]
            ).optional(),
            "primary": t.boolean().optional(),
            "backgroundColor": t.string().optional(),
            "accessRole": t.string().optional(),
            "location": t.string().optional(),
            "defaultReminders": t.array(
                t.proxy(renames["EventReminderOut"])
            ).optional(),
            "summary": t.string().optional(),
            "etag": t.string().optional(),
            "summaryOverride": t.string().optional(),
            "timeZone": t.string().optional(),
            "deleted": t.boolean().optional(),
            "notificationSettings": t.struct(
                {
                    "notifications": t.array(
                        t.proxy(renames["CalendarNotificationOut"])
                    ).optional()
                }
            ).optional(),
            "hidden": t.boolean().optional(),
            "kind": t.string().optional(),
            "foregroundColor": t.string().optional(),
            "selected": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarListEntryOut"])
    types["FreeBusyResponseIn"] = t.struct(
        {
            "groups": t.struct({"_": t.string().optional()}).optional(),
            "timeMin": t.string().optional(),
            "kind": t.string().optional(),
            "timeMax": t.string().optional(),
            "calendars": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FreeBusyResponseIn"])
    types["FreeBusyResponseOut"] = t.struct(
        {
            "groups": t.struct({"_": t.string().optional()}).optional(),
            "timeMin": t.string().optional(),
            "kind": t.string().optional(),
            "timeMax": t.string().optional(),
            "calendars": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyResponseOut"])
    types["ColorsIn"] = t.struct(
        {
            "event": t.struct({"_": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "calendar": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ColorsIn"])
    types["ColorsOut"] = t.struct(
        {
            "event": t.struct({"_": t.string().optional()}).optional(),
            "updated": t.string().optional(),
            "calendar": t.struct({"_": t.string().optional()}).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorsOut"])
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
    types["FreeBusyRequestIn"] = t.struct(
        {
            "timeMax": t.string().optional(),
            "groupExpansionMax": t.integer().optional(),
            "calendarExpansionMax": t.integer().optional(),
            "items": t.array(t.proxy(renames["FreeBusyRequestItemIn"])).optional(),
            "timeMin": t.string().optional(),
            "timeZone": t.string().optional(),
        }
    ).named(renames["FreeBusyRequestIn"])
    types["FreeBusyRequestOut"] = t.struct(
        {
            "timeMax": t.string().optional(),
            "groupExpansionMax": t.integer().optional(),
            "calendarExpansionMax": t.integer().optional(),
            "items": t.array(t.proxy(renames["FreeBusyRequestItemOut"])).optional(),
            "timeMin": t.string().optional(),
            "timeZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreeBusyRequestOut"])
    types["ConferenceSolutionKeyIn"] = t.struct({"type": t.string().optional()}).named(
        renames["ConferenceSolutionKeyIn"]
    )
    types["ConferenceSolutionKeyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceSolutionKeyOut"])
    types["EventAttachmentIn"] = t.struct(
        {
            "title": t.string().optional(),
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
            "iconLink": t.string().optional(),
            "fileUrl": t.string().optional(),
        }
    ).named(renames["EventAttachmentIn"])
    types["EventAttachmentOut"] = t.struct(
        {
            "title": t.string().optional(),
            "mimeType": t.string().optional(),
            "fileId": t.string().optional(),
            "iconLink": t.string().optional(),
            "fileUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventAttachmentOut"])
    types["CalendarListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CalendarListEntryIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["CalendarListIn"])
    types["CalendarListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "items": t.array(t.proxy(renames["CalendarListEntryOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CalendarListOut"])
    types["AclIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AclRuleIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["AclIn"])
    types["AclOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "nextSyncToken": t.string().optional(),
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["AclRuleOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AclOut"])
    types["EventDateTimeIn"] = t.struct(
        {
            "dateTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "date": t.string().optional(),
        }
    ).named(renames["EventDateTimeIn"])
    types["EventDateTimeOut"] = t.struct(
        {
            "dateTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "date": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventDateTimeOut"])
    types["CreateConferenceRequestIn"] = t.struct(
        {
            "conferenceSolutionKey": t.proxy(
                renames["ConferenceSolutionKeyIn"]
            ).optional(),
            "requestId": t.string().optional(),
            "status": t.proxy(renames["ConferenceRequestStatusIn"]).optional(),
        }
    ).named(renames["CreateConferenceRequestIn"])
    types["CreateConferenceRequestOut"] = t.struct(
        {
            "conferenceSolutionKey": t.proxy(
                renames["ConferenceSolutionKeyOut"]
            ).optional(),
            "requestId": t.string().optional(),
            "status": t.proxy(renames["ConferenceRequestStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateConferenceRequestOut"])
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
    types["EventWorkingLocationPropertiesIn"] = t.struct(
        {
            "homeOffice": t.struct({"_": t.string().optional()}).optional(),
            "officeLocation": t.struct(
                {
                    "floorId": t.string().optional(),
                    "floorSectionId": t.string().optional(),
                    "label": t.string().optional(),
                    "buildingId": t.string().optional(),
                    "deskId": t.string().optional(),
                }
            ).optional(),
            "type": t.string().optional(),
            "customLocation": t.struct({"label": t.string().optional()}).optional(),
        }
    ).named(renames["EventWorkingLocationPropertiesIn"])
    types["EventWorkingLocationPropertiesOut"] = t.struct(
        {
            "homeOffice": t.struct({"_": t.string().optional()}).optional(),
            "officeLocation": t.struct(
                {
                    "floorId": t.string().optional(),
                    "floorSectionId": t.string().optional(),
                    "label": t.string().optional(),
                    "buildingId": t.string().optional(),
                    "deskId": t.string().optional(),
                }
            ).optional(),
            "type": t.string().optional(),
            "customLocation": t.struct({"label": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventWorkingLocationPropertiesOut"])
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
    types["SettingsIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["SettingIn"])).optional(),
            "nextSyncToken": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SettingsIn"])
    types["SettingsOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "items": t.array(t.proxy(renames["SettingOut"])).optional(),
            "nextSyncToken": t.string().optional(),
            "etag": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SettingsOut"])
    types["ConferenceSolutionIn"] = t.struct(
        {
            "iconUri": t.string().optional(),
            "key": t.proxy(renames["ConferenceSolutionKeyIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ConferenceSolutionIn"])
    types["ConferenceSolutionOut"] = t.struct(
        {
            "iconUri": t.string().optional(),
            "key": t.proxy(renames["ConferenceSolutionKeyOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConferenceSolutionOut"])

    functions = {}
    functions["aclPatch"] = calendar.post(
        "calendars/{calendarId}/acl/watch",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "calendarId": t.string().optional(),
                "syncToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclDelete"] = calendar.post(
        "calendars/{calendarId}/acl/watch",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "calendarId": t.string().optional(),
                "syncToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclGet"] = calendar.post(
        "calendars/{calendarId}/acl/watch",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "calendarId": t.string().optional(),
                "syncToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclUpdate"] = calendar.post(
        "calendars/{calendarId}/acl/watch",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "calendarId": t.string().optional(),
                "syncToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclInsert"] = calendar.post(
        "calendars/{calendarId}/acl/watch",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "calendarId": t.string().optional(),
                "syncToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclList"] = calendar.post(
        "calendars/{calendarId}/acl/watch",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "calendarId": t.string().optional(),
                "syncToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["aclWatch"] = calendar.post(
        "calendars/{calendarId}/acl/watch",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "calendarId": t.string().optional(),
                "syncToken": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListDelete"] = calendar.get(
        "users/me/calendarList",
        t.struct(
            {
                "showHidden": t.boolean().optional(),
                "minAccessRole": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "syncToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CalendarListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListUpdate"] = calendar.get(
        "users/me/calendarList",
        t.struct(
            {
                "showHidden": t.boolean().optional(),
                "minAccessRole": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "syncToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CalendarListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListGet"] = calendar.get(
        "users/me/calendarList",
        t.struct(
            {
                "showHidden": t.boolean().optional(),
                "minAccessRole": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "syncToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CalendarListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListPatch"] = calendar.get(
        "users/me/calendarList",
        t.struct(
            {
                "showHidden": t.boolean().optional(),
                "minAccessRole": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "syncToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CalendarListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListInsert"] = calendar.get(
        "users/me/calendarList",
        t.struct(
            {
                "showHidden": t.boolean().optional(),
                "minAccessRole": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "syncToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CalendarListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListWatch"] = calendar.get(
        "users/me/calendarList",
        t.struct(
            {
                "showHidden": t.boolean().optional(),
                "minAccessRole": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "syncToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CalendarListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarListList"] = calendar.get(
        "users/me/calendarList",
        t.struct(
            {
                "showHidden": t.boolean().optional(),
                "minAccessRole": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "syncToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CalendarListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["freebusyQuery"] = calendar.post(
        "freeBusy",
        t.struct(
            {
                "timeMax": t.string().optional(),
                "groupExpansionMax": t.integer().optional(),
                "calendarExpansionMax": t.integer().optional(),
                "items": t.array(t.proxy(renames["FreeBusyRequestItemIn"])).optional(),
                "timeMin": t.string().optional(),
                "timeZone": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FreeBusyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsStop"] = calendar.post(
        "channels/stop",
        t.struct(
            {
                "token": t.string().optional(),
                "payload": t.boolean().optional(),
                "kind": t.string().optional(),
                "address": t.string().optional(),
                "resourceUri": t.string().optional(),
                "expiration": t.string().optional(),
                "resourceId": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsUpdate"] = calendar.get(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsPatch"] = calendar.get(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsClear"] = calendar.get(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsInsert"] = calendar.get(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsDelete"] = calendar.get(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["calendarsGet"] = calendar.get(
        "calendars/{calendarId}",
        t.struct({"calendarId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["CalendarOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsWatch"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsList"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsMove"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsDelete"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsGet"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsQuickAdd"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsPatch"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsImport"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsUpdate"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsInstances"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EventOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["eventsInsert"] = calendar.post(
        "calendars/{calendarId}/events",
        t.struct(
            {
                "calendarId": t.string().optional(),
                "maxAttendees": t.integer().optional(),
                "conferenceDataVersion": t.integer().optional(),
                "supportsAttachments": t.boolean().optional(),
                "sendUpdates": t.string().optional(),
                "sendNotifications": t.boolean().optional(),
                "hangoutLink": t.string().optional(),
                "htmlLink": t.string().optional(),
                "updated": t.string().optional(),
                "reminders": t.struct(
                    {
                        "useDefault": t.boolean().optional(),
                        "overrides": t.array(
                            t.proxy(renames["EventReminderIn"])
                        ).optional(),
                    }
                ).optional(),
                "etag": t.string().optional(),
                "privateCopy": t.boolean().optional(),
                "kind": t.string().optional(),
                "workingLocationProperties": t.proxy(
                    renames["EventWorkingLocationPropertiesIn"]
                ).optional(),
                "recurringEventId": t.string().optional(),
                "eventType": t.string().optional(),
                "description": t.string().optional(),
                "status": t.string().optional(),
                "extendedProperties": t.struct(
                    {
                        "shared": t.struct({"_": t.string().optional()}).optional(),
                        "private": t.struct({"_": t.string().optional()}).optional(),
                    }
                ).optional(),
                "attendeesOmitted": t.boolean().optional(),
                "endTimeUnspecified": t.boolean().optional(),
                "summary": t.string().optional(),
                "start": t.proxy(renames["EventDateTimeIn"]).optional(),
                "recurrence": t.array(t.string()).optional(),
                "iCalUID": t.string().optional(),
                "created": t.string().optional(),
                "source": t.struct(
                    {"url": t.string().optional(), "title": t.string().optional()}
                ).optional(),
                "guestsCanInviteOthers": t.boolean().optional(),
                "creator": t.struct(
                    {
                        "email": t.string().optional(),
                        "self": t.boolean().optional(),
                        "id": t.string().optional(),
                        "displayName": t.string().optional(),
                    }
                ).optional(),
                "end": t.proxy(renames["EventDateTimeIn"]).optional(),
                "organizer": t.struct(
                    {
                        "displayName": t.string().optional(),
                        "self": t.boolean().optional(),
                        "email": t.string().optional(),
                        "id": t.string().optional(),
                    }
                ).optional(),
                "attachments": t.array(
                    t.proxy(renames["EventAttachmentIn"])
                ).optional(),
                "location": t.string().optional(),
                "anyoneCanAddSelf": t.boolean().optional(),
                "gadget": t.struct(
                    {
                        "display": t.string().optional(),
                        "type": t.string().optional(),
                        "height": t.integer().optional(),
                        "link": t.string().optional(),
                        "width": t.integer().optional(),
                        "preferences": t.struct(
                            {"_": t.string().optional()}
                        ).optional(),
                        "title": t.string().optional(),
                        "iconLink": t.string().optional(),
                    }
                ).optional(),
                "originalStartTime": t.proxy(renames["EventDateTimeIn"]).optional(),
                "locked": t.boolean().optional(),
                "conferenceData": t.proxy(renames["ConferenceDataIn"]).optional(),
                "guestsCanModify": t.boolean().optional(),
                "transparency": t.string().optional(),
                "sequence": t.integer().optional(),
                "id": t.string().optional(),
                "visibility": t.string().optional(),
                "guestsCanSeeOtherGuests": t.boolean().optional(),
                "colorId": t.string().optional(),
                "attendees": t.array(t.proxy(renames["EventAttendeeIn"])).optional(),
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
    functions["settingsWatch"] = calendar.get(
        "users/me/settings",
        t.struct(
            {
                "syncToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsGet"] = calendar.get(
        "users/me/settings",
        t.struct(
            {
                "syncToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["settingsList"] = calendar.get(
        "users/me/settings",
        t.struct(
            {
                "syncToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SettingsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="calendar", renames=renames, types=Box(types), functions=Box(functions)
    )
