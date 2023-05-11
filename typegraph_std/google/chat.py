from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_chat() -> Import:
    chat = HTTPRuntime("https://chat.googleapis.com/")

    renames = {
        "ErrorResponse": "_chat_1_ErrorResponse",
        "GoogleAppsCardV1SuggestionItemIn": "_chat_2_GoogleAppsCardV1SuggestionItemIn",
        "GoogleAppsCardV1SuggestionItemOut": "_chat_3_GoogleAppsCardV1SuggestionItemOut",
        "UserIn": "_chat_4_UserIn",
        "UserOut": "_chat_5_UserOut",
        "ImageButtonIn": "_chat_6_ImageButtonIn",
        "ImageButtonOut": "_chat_7_ImageButtonOut",
        "GoogleAppsCardV1ActionIn": "_chat_8_GoogleAppsCardV1ActionIn",
        "GoogleAppsCardV1ActionOut": "_chat_9_GoogleAppsCardV1ActionOut",
        "SpaceIn": "_chat_10_SpaceIn",
        "SpaceOut": "_chat_11_SpaceOut",
        "ActionStatusIn": "_chat_12_ActionStatusIn",
        "ActionStatusOut": "_chat_13_ActionStatusOut",
        "GoogleAppsCardV1CardHeaderIn": "_chat_14_GoogleAppsCardV1CardHeaderIn",
        "GoogleAppsCardV1CardHeaderOut": "_chat_15_GoogleAppsCardV1CardHeaderOut",
        "DateTimeInputIn": "_chat_16_DateTimeInputIn",
        "DateTimeInputOut": "_chat_17_DateTimeInputOut",
        "DeprecatedEventIn": "_chat_18_DeprecatedEventIn",
        "DeprecatedEventOut": "_chat_19_DeprecatedEventOut",
        "GoogleAppsCardV1SuggestionsIn": "_chat_20_GoogleAppsCardV1SuggestionsIn",
        "GoogleAppsCardV1SuggestionsOut": "_chat_21_GoogleAppsCardV1SuggestionsOut",
        "CardWithIdIn": "_chat_22_CardWithIdIn",
        "CardWithIdOut": "_chat_23_CardWithIdOut",
        "AttachmentDataRefIn": "_chat_24_AttachmentDataRefIn",
        "AttachmentDataRefOut": "_chat_25_AttachmentDataRefOut",
        "AttachmentIn": "_chat_26_AttachmentIn",
        "AttachmentOut": "_chat_27_AttachmentOut",
        "DriveDataRefIn": "_chat_28_DriveDataRefIn",
        "DriveDataRefOut": "_chat_29_DriveDataRefOut",
        "TimeInputIn": "_chat_30_TimeInputIn",
        "TimeInputOut": "_chat_31_TimeInputOut",
        "ActionResponseIn": "_chat_32_ActionResponseIn",
        "ActionResponseOut": "_chat_33_ActionResponseOut",
        "WidgetMarkupIn": "_chat_34_WidgetMarkupIn",
        "WidgetMarkupOut": "_chat_35_WidgetMarkupOut",
        "ThreadIn": "_chat_36_ThreadIn",
        "ThreadOut": "_chat_37_ThreadOut",
        "GoogleAppsCardV1BorderStyleIn": "_chat_38_GoogleAppsCardV1BorderStyleIn",
        "GoogleAppsCardV1BorderStyleOut": "_chat_39_GoogleAppsCardV1BorderStyleOut",
        "SlashCommandMetadataIn": "_chat_40_SlashCommandMetadataIn",
        "SlashCommandMetadataOut": "_chat_41_SlashCommandMetadataOut",
        "GoogleAppsCardV1CardActionIn": "_chat_42_GoogleAppsCardV1CardActionIn",
        "GoogleAppsCardV1CardActionOut": "_chat_43_GoogleAppsCardV1CardActionOut",
        "GoogleAppsCardV1DividerIn": "_chat_44_GoogleAppsCardV1DividerIn",
        "GoogleAppsCardV1DividerOut": "_chat_45_GoogleAppsCardV1DividerOut",
        "GoogleAppsCardV1SectionIn": "_chat_46_GoogleAppsCardV1SectionIn",
        "GoogleAppsCardV1SectionOut": "_chat_47_GoogleAppsCardV1SectionOut",
        "UserMentionMetadataIn": "_chat_48_UserMentionMetadataIn",
        "UserMentionMetadataOut": "_chat_49_UserMentionMetadataOut",
        "StringInputsIn": "_chat_50_StringInputsIn",
        "StringInputsOut": "_chat_51_StringInputsOut",
        "StatusIn": "_chat_52_StatusIn",
        "StatusOut": "_chat_53_StatusOut",
        "GoogleAppsCardV1OpenLinkIn": "_chat_54_GoogleAppsCardV1OpenLinkIn",
        "GoogleAppsCardV1OpenLinkOut": "_chat_55_GoogleAppsCardV1OpenLinkOut",
        "EmptyIn": "_chat_56_EmptyIn",
        "EmptyOut": "_chat_57_EmptyOut",
        "MediaIn": "_chat_58_MediaIn",
        "MediaOut": "_chat_59_MediaOut",
        "GoogleAppsCardV1CardIn": "_chat_60_GoogleAppsCardV1CardIn",
        "GoogleAppsCardV1CardOut": "_chat_61_GoogleAppsCardV1CardOut",
        "MessageIn": "_chat_62_MessageIn",
        "MessageOut": "_chat_63_MessageOut",
        "CardHeaderIn": "_chat_64_CardHeaderIn",
        "CardHeaderOut": "_chat_65_CardHeaderOut",
        "ChatAppLogEntryIn": "_chat_66_ChatAppLogEntryIn",
        "ChatAppLogEntryOut": "_chat_67_ChatAppLogEntryOut",
        "DialogActionIn": "_chat_68_DialogActionIn",
        "DialogActionOut": "_chat_69_DialogActionOut",
        "ListMembershipsResponseIn": "_chat_70_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_chat_71_ListMembershipsResponseOut",
        "GoogleAppsCardV1TextParagraphIn": "_chat_72_GoogleAppsCardV1TextParagraphIn",
        "GoogleAppsCardV1TextParagraphOut": "_chat_73_GoogleAppsCardV1TextParagraphOut",
        "MatchedUrlIn": "_chat_74_MatchedUrlIn",
        "MatchedUrlOut": "_chat_75_MatchedUrlOut",
        "GoogleAppsCardV1IconIn": "_chat_76_GoogleAppsCardV1IconIn",
        "GoogleAppsCardV1IconOut": "_chat_77_GoogleAppsCardV1IconOut",
        "GoogleAppsCardV1DateTimePickerIn": "_chat_78_GoogleAppsCardV1DateTimePickerIn",
        "GoogleAppsCardV1DateTimePickerOut": "_chat_79_GoogleAppsCardV1DateTimePickerOut",
        "DialogIn": "_chat_80_DialogIn",
        "DialogOut": "_chat_81_DialogOut",
        "SlashCommandIn": "_chat_82_SlashCommandIn",
        "SlashCommandOut": "_chat_83_SlashCommandOut",
        "GoogleAppsCardV1ImageComponentIn": "_chat_84_GoogleAppsCardV1ImageComponentIn",
        "GoogleAppsCardV1ImageComponentOut": "_chat_85_GoogleAppsCardV1ImageComponentOut",
        "SectionIn": "_chat_86_SectionIn",
        "SectionOut": "_chat_87_SectionOut",
        "GoogleAppsCardV1ActionParameterIn": "_chat_88_GoogleAppsCardV1ActionParameterIn",
        "GoogleAppsCardV1ActionParameterOut": "_chat_89_GoogleAppsCardV1ActionParameterOut",
        "GoogleAppsCardV1ButtonIn": "_chat_90_GoogleAppsCardV1ButtonIn",
        "GoogleAppsCardV1ButtonOut": "_chat_91_GoogleAppsCardV1ButtonOut",
        "MembershipIn": "_chat_92_MembershipIn",
        "MembershipOut": "_chat_93_MembershipOut",
        "ListSpacesResponseIn": "_chat_94_ListSpacesResponseIn",
        "ListSpacesResponseOut": "_chat_95_ListSpacesResponseOut",
        "OpenLinkIn": "_chat_96_OpenLinkIn",
        "OpenLinkOut": "_chat_97_OpenLinkOut",
        "GoogleAppsCardV1SelectionItemIn": "_chat_98_GoogleAppsCardV1SelectionItemIn",
        "GoogleAppsCardV1SelectionItemOut": "_chat_99_GoogleAppsCardV1SelectionItemOut",
        "GoogleAppsCardV1SwitchControlIn": "_chat_100_GoogleAppsCardV1SwitchControlIn",
        "GoogleAppsCardV1SwitchControlOut": "_chat_101_GoogleAppsCardV1SwitchControlOut",
        "GoogleAppsCardV1OnClickIn": "_chat_102_GoogleAppsCardV1OnClickIn",
        "GoogleAppsCardV1OnClickOut": "_chat_103_GoogleAppsCardV1OnClickOut",
        "GoogleAppsCardV1GridItemIn": "_chat_104_GoogleAppsCardV1GridItemIn",
        "GoogleAppsCardV1GridItemOut": "_chat_105_GoogleAppsCardV1GridItemOut",
        "FormActionIn": "_chat_106_FormActionIn",
        "FormActionOut": "_chat_107_FormActionOut",
        "GoogleAppsCardV1TextInputIn": "_chat_108_GoogleAppsCardV1TextInputIn",
        "GoogleAppsCardV1TextInputOut": "_chat_109_GoogleAppsCardV1TextInputOut",
        "DateInputIn": "_chat_110_DateInputIn",
        "DateInputOut": "_chat_111_DateInputOut",
        "AnnotationIn": "_chat_112_AnnotationIn",
        "AnnotationOut": "_chat_113_AnnotationOut",
        "TextButtonIn": "_chat_114_TextButtonIn",
        "TextButtonOut": "_chat_115_TextButtonOut",
        "GoogleAppsCardV1ImageIn": "_chat_116_GoogleAppsCardV1ImageIn",
        "GoogleAppsCardV1ImageOut": "_chat_117_GoogleAppsCardV1ImageOut",
        "OnClickIn": "_chat_118_OnClickIn",
        "OnClickOut": "_chat_119_OnClickOut",
        "ColorIn": "_chat_120_ColorIn",
        "ColorOut": "_chat_121_ColorOut",
        "TextParagraphIn": "_chat_122_TextParagraphIn",
        "TextParagraphOut": "_chat_123_TextParagraphOut",
        "CardActionIn": "_chat_124_CardActionIn",
        "CardActionOut": "_chat_125_CardActionOut",
        "GoogleAppsCardV1WidgetIn": "_chat_126_GoogleAppsCardV1WidgetIn",
        "GoogleAppsCardV1WidgetOut": "_chat_127_GoogleAppsCardV1WidgetOut",
        "ActionParameterIn": "_chat_128_ActionParameterIn",
        "ActionParameterOut": "_chat_129_ActionParameterOut",
        "SpaceDetailsIn": "_chat_130_SpaceDetailsIn",
        "SpaceDetailsOut": "_chat_131_SpaceDetailsOut",
        "GoogleAppsCardV1SelectionInputIn": "_chat_132_GoogleAppsCardV1SelectionInputIn",
        "GoogleAppsCardV1SelectionInputOut": "_chat_133_GoogleAppsCardV1SelectionInputOut",
        "InputsIn": "_chat_134_InputsIn",
        "InputsOut": "_chat_135_InputsOut",
        "KeyValueIn": "_chat_136_KeyValueIn",
        "KeyValueOut": "_chat_137_KeyValueOut",
        "GoogleAppsCardV1GridIn": "_chat_138_GoogleAppsCardV1GridIn",
        "GoogleAppsCardV1GridOut": "_chat_139_GoogleAppsCardV1GridOut",
        "ButtonIn": "_chat_140_ButtonIn",
        "ButtonOut": "_chat_141_ButtonOut",
        "GoogleAppsCardV1ImageCropStyleIn": "_chat_142_GoogleAppsCardV1ImageCropStyleIn",
        "GoogleAppsCardV1ImageCropStyleOut": "_chat_143_GoogleAppsCardV1ImageCropStyleOut",
        "TimeZoneIn": "_chat_144_TimeZoneIn",
        "TimeZoneOut": "_chat_145_TimeZoneOut",
        "CommonEventObjectIn": "_chat_146_CommonEventObjectIn",
        "CommonEventObjectOut": "_chat_147_CommonEventObjectOut",
        "ImageIn": "_chat_148_ImageIn",
        "ImageOut": "_chat_149_ImageOut",
        "CardIn": "_chat_150_CardIn",
        "CardOut": "_chat_151_CardOut",
        "GoogleAppsCardV1CardFixedFooterIn": "_chat_152_GoogleAppsCardV1CardFixedFooterIn",
        "GoogleAppsCardV1CardFixedFooterOut": "_chat_153_GoogleAppsCardV1CardFixedFooterOut",
        "GoogleAppsCardV1DecoratedTextIn": "_chat_154_GoogleAppsCardV1DecoratedTextIn",
        "GoogleAppsCardV1DecoratedTextOut": "_chat_155_GoogleAppsCardV1DecoratedTextOut",
        "GoogleAppsCardV1ButtonListIn": "_chat_156_GoogleAppsCardV1ButtonListIn",
        "GoogleAppsCardV1ButtonListOut": "_chat_157_GoogleAppsCardV1ButtonListOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleAppsCardV1SuggestionItemIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1SuggestionItemIn"])
    types["GoogleAppsCardV1SuggestionItemOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SuggestionItemOut"])
    types["UserIn"] = t.struct(
        {
            "type": t.string().optional(),
            "domainId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "domainId": t.string().optional(),
            "name": t.string().optional(),
            "isAnonymous": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["ImageButtonIn"] = t.struct(
        {
            "name": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "icon": t.string().optional(),
        }
    ).named(renames["ImageButtonIn"])
    types["ImageButtonOut"] = t.struct(
        {
            "name": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "icon": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageButtonOut"])
    types["GoogleAppsCardV1ActionIn"] = t.struct(
        {
            "function": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterIn"])
            ).optional(),
            "interaction": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "loadIndicator": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionIn"])
    types["GoogleAppsCardV1ActionOut"] = t.struct(
        {
            "function": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterOut"])
            ).optional(),
            "interaction": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "loadIndicator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionOut"])
    types["SpaceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "singleUserBotDm": t.boolean().optional(),
            "spaceDetails": t.proxy(renames["SpaceDetailsIn"]).optional(),
        }
    ).named(renames["SpaceIn"])
    types["SpaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "spaceThreadingState": t.string().optional(),
            "adminInstalled": t.boolean().optional(),
            "threaded": t.boolean().optional(),
            "singleUserBotDm": t.boolean().optional(),
            "spaceDetails": t.proxy(renames["SpaceDetailsOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceOut"])
    types["ActionStatusIn"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "userFacingMessage": t.string().optional(),
        }
    ).named(renames["ActionStatusIn"])
    types["ActionStatusOut"] = t.struct(
        {
            "statusCode": t.string().optional(),
            "userFacingMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionStatusOut"])
    types["GoogleAppsCardV1CardHeaderIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "title": t.string(),
            "imageAltText": t.string().optional(),
            "imageType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderIn"])
    types["GoogleAppsCardV1CardHeaderOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "title": t.string(),
            "imageAltText": t.string().optional(),
            "imageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderOut"])
    types["DateTimeInputIn"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "hasDate": t.boolean().optional(),
            "hasTime": t.boolean().optional(),
        }
    ).named(renames["DateTimeInputIn"])
    types["DateTimeInputOut"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "hasDate": t.boolean().optional(),
            "hasTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeInputOut"])
    types["DeprecatedEventIn"] = t.struct(
        {
            "type": t.string().optional(),
            "dialogEventType": t.string().optional(),
            "isDialogEvent": t.boolean().optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "token": t.string().optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
            "eventTime": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "threadKey": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectIn"]).optional(),
            "action": t.proxy(renames["FormActionIn"]).optional(),
        }
    ).named(renames["DeprecatedEventIn"])
    types["DeprecatedEventOut"] = t.struct(
        {
            "type": t.string().optional(),
            "dialogEventType": t.string().optional(),
            "isDialogEvent": t.boolean().optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "token": t.string().optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "eventTime": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "threadKey": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectOut"]).optional(),
            "action": t.proxy(renames["FormActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeprecatedEventOut"])
    types["GoogleAppsCardV1SuggestionsIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SuggestionItemIn"])
            ).optional()
        }
    ).named(renames["GoogleAppsCardV1SuggestionsIn"])
    types["GoogleAppsCardV1SuggestionsOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SuggestionItemOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SuggestionsOut"])
    types["CardWithIdIn"] = t.struct(
        {
            "cardId": t.string(),
            "card": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional(),
        }
    ).named(renames["CardWithIdIn"])
    types["CardWithIdOut"] = t.struct(
        {
            "cardId": t.string(),
            "card": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardWithIdOut"])
    types["AttachmentDataRefIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["AttachmentDataRefIn"])
    types["AttachmentDataRefOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentDataRefOut"])
    types["AttachmentIn"] = t.struct(
        {
            "contentName": t.string().optional(),
            "source": t.string().optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefIn"]).optional(),
            "name": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefIn"]).optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "contentName": t.string().optional(),
            "downloadUri": t.string().optional(),
            "source": t.string().optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefOut"]).optional(),
            "thumbnailUri": t.string().optional(),
            "name": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefOut"]).optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["DriveDataRefIn"] = t.struct({"driveFileId": t.string().optional()}).named(
        renames["DriveDataRefIn"]
    )
    types["DriveDataRefOut"] = t.struct(
        {
            "driveFileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveDataRefOut"])
    types["TimeInputIn"] = t.struct(
        {"hours": t.integer().optional(), "minutes": t.integer().optional()}
    ).named(renames["TimeInputIn"])
    types["TimeInputOut"] = t.struct(
        {
            "hours": t.integer().optional(),
            "minutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeInputOut"])
    types["ActionResponseIn"] = t.struct(
        {
            "type": t.string().optional(),
            "url": t.string().optional(),
            "dialogAction": t.proxy(renames["DialogActionIn"]).optional(),
        }
    ).named(renames["ActionResponseIn"])
    types["ActionResponseOut"] = t.struct(
        {
            "type": t.string().optional(),
            "url": t.string().optional(),
            "dialogAction": t.proxy(renames["DialogActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionResponseOut"])
    types["WidgetMarkupIn"] = t.struct(
        {
            "buttons": t.array(t.proxy(renames["ButtonIn"])).optional(),
            "textParagraph": t.proxy(renames["TextParagraphIn"]).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "keyValue": t.proxy(renames["KeyValueIn"]).optional(),
        }
    ).named(renames["WidgetMarkupIn"])
    types["WidgetMarkupOut"] = t.struct(
        {
            "buttons": t.array(t.proxy(renames["ButtonOut"])).optional(),
            "textParagraph": t.proxy(renames["TextParagraphOut"]).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "keyValue": t.proxy(renames["KeyValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WidgetMarkupOut"])
    types["ThreadIn"] = t.struct(
        {"name": t.string().optional(), "threadKey": t.string().optional()}
    ).named(renames["ThreadIn"])
    types["ThreadOut"] = t.struct(
        {
            "name": t.string().optional(),
            "threadKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadOut"])
    types["GoogleAppsCardV1BorderStyleIn"] = t.struct(
        {
            "strokeColor": t.proxy(renames["ColorIn"]).optional(),
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1BorderStyleIn"])
    types["GoogleAppsCardV1BorderStyleOut"] = t.struct(
        {
            "strokeColor": t.proxy(renames["ColorOut"]).optional(),
            "cornerRadius": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1BorderStyleOut"])
    types["SlashCommandMetadataIn"] = t.struct(
        {
            "triggersDialog": t.boolean().optional(),
            "commandId": t.string().optional(),
            "commandName": t.string().optional(),
            "bot": t.proxy(renames["UserIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SlashCommandMetadataIn"])
    types["SlashCommandMetadataOut"] = t.struct(
        {
            "triggersDialog": t.boolean().optional(),
            "commandId": t.string().optional(),
            "commandName": t.string().optional(),
            "bot": t.proxy(renames["UserOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandMetadataOut"])
    types["GoogleAppsCardV1CardActionIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "actionLabel": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1CardActionIn"])
    types["GoogleAppsCardV1CardActionOut"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "actionLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardActionOut"])
    types["GoogleAppsCardV1DividerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsCardV1DividerIn"]
    )
    types["GoogleAppsCardV1DividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCardV1DividerOut"])
    types["GoogleAppsCardV1SectionIn"] = t.struct(
        {
            "collapsible": t.boolean().optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "widgets": t.array(t.proxy(renames["GoogleAppsCardV1WidgetIn"])).optional(),
            "header": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SectionIn"])
    types["GoogleAppsCardV1SectionOut"] = t.struct(
        {
            "collapsible": t.boolean().optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "widgets": t.array(
                t.proxy(renames["GoogleAppsCardV1WidgetOut"])
            ).optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SectionOut"])
    types["UserMentionMetadataIn"] = t.struct(
        {"user": t.proxy(renames["UserIn"]).optional(), "type": t.string().optional()}
    ).named(renames["UserMentionMetadataIn"])
    types["UserMentionMetadataOut"] = t.struct(
        {
            "user": t.proxy(renames["UserOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionMetadataOut"])
    types["StringInputsIn"] = t.struct({"value": t.array(t.string()).optional()}).named(
        renames["StringInputsIn"]
    )
    types["StringInputsOut"] = t.struct(
        {
            "value": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringInputsOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleAppsCardV1OpenLinkIn"] = t.struct(
        {
            "openAs": t.string().optional(),
            "url": t.string().optional(),
            "onClose": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1OpenLinkIn"])
    types["GoogleAppsCardV1OpenLinkOut"] = t.struct(
        {
            "openAs": t.string().optional(),
            "url": t.string().optional(),
            "onClose": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OpenLinkOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["GoogleAppsCardV1CardIn"] = t.struct(
        {
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterIn"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionIn"])
            ).optional(),
            "displayStyle": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionIn"])
            ).optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderIn"]).optional(),
            "name": t.string().optional(),
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardIn"])
    types["GoogleAppsCardV1CardOut"] = t.struct(
        {
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterOut"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionOut"])
            ).optional(),
            "displayStyle": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionOut"])
            ).optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderOut"]).optional(),
            "name": t.string().optional(),
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardOut"])
    types["MessageIn"] = t.struct(
        {
            "thread": t.proxy(renames["ThreadIn"]).optional(),
            "name": t.string().optional(),
            "text": t.string().optional(),
            "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "clientAssignedMessageId": t.string().optional(),
            "fallbackText": t.string().optional(),
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "cards": t.array(t.proxy(renames["CardIn"])).optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
            "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "thread": t.proxy(renames["ThreadOut"]).optional(),
            "sender": t.proxy(renames["UserOut"]).optional(),
            "name": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "threadReply": t.boolean().optional(),
            "text": t.string().optional(),
            "matchedUrl": t.proxy(renames["MatchedUrlOut"]).optional(),
            "attachment": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "slashCommand": t.proxy(renames["SlashCommandOut"]).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "clientAssignedMessageId": t.string().optional(),
            "fallbackText": t.string().optional(),
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "cards": t.array(t.proxy(renames["CardOut"])).optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdOut"])).optional(),
            "createTime": t.string().optional(),
            "actionResponse": t.proxy(renames["ActionResponseOut"]).optional(),
            "argumentText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["CardHeaderIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["CardHeaderIn"])
    types["CardHeaderOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardHeaderOut"])
    types["ChatAppLogEntryIn"] = t.struct(
        {
            "deploymentFunction": t.string().optional(),
            "deployment": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ChatAppLogEntryIn"])
    types["ChatAppLogEntryOut"] = t.struct(
        {
            "deploymentFunction": t.string().optional(),
            "deployment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatAppLogEntryOut"])
    types["DialogActionIn"] = t.struct(
        {
            "dialog": t.proxy(renames["DialogIn"]).optional(),
            "actionStatus": t.proxy(renames["ActionStatusIn"]).optional(),
        }
    ).named(renames["DialogActionIn"])
    types["DialogActionOut"] = t.struct(
        {
            "dialog": t.proxy(renames["DialogOut"]).optional(),
            "actionStatus": t.proxy(renames["ActionStatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DialogActionOut"])
    types["ListMembershipsResponseIn"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMembershipsResponseIn"])
    types["ListMembershipsResponseOut"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipsResponseOut"])
    types["GoogleAppsCardV1TextParagraphIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1TextParagraphIn"])
    types["GoogleAppsCardV1TextParagraphOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextParagraphOut"])
    types["MatchedUrlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatchedUrlIn"]
    )
    types["MatchedUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchedUrlOut"])
    types["GoogleAppsCardV1IconIn"] = t.struct(
        {
            "knownIcon": t.string().optional(),
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1IconIn"])
    types["GoogleAppsCardV1IconOut"] = t.struct(
        {
            "knownIcon": t.string().optional(),
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1IconOut"])
    types["GoogleAppsCardV1DateTimePickerIn"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerIn"])
    types["GoogleAppsCardV1DateTimePickerOut"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerOut"])
    types["DialogIn"] = t.struct(
        {"body": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional()}
    ).named(renames["DialogIn"])
    types["DialogOut"] = t.struct(
        {
            "body": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DialogOut"])
    types["SlashCommandIn"] = t.struct({"commandId": t.string().optional()}).named(
        renames["SlashCommandIn"]
    )
    types["SlashCommandOut"] = t.struct(
        {
            "commandId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandOut"])
    types["GoogleAppsCardV1ImageComponentIn"] = t.struct(
        {
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "cropStyle": t.proxy(
                renames["GoogleAppsCardV1ImageCropStyleIn"]
            ).optional(),
            "imageUri": t.string().optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageComponentIn"])
    types["GoogleAppsCardV1ImageComponentOut"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["GoogleAppsCardV1BorderStyleOut"]
            ).optional(),
            "cropStyle": t.proxy(
                renames["GoogleAppsCardV1ImageCropStyleOut"]
            ).optional(),
            "imageUri": t.string().optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageComponentOut"])
    types["SectionIn"] = t.struct(
        {
            "widgets": t.array(t.proxy(renames["WidgetMarkupIn"])).optional(),
            "header": t.string().optional(),
        }
    ).named(renames["SectionIn"])
    types["SectionOut"] = t.struct(
        {
            "widgets": t.array(t.proxy(renames["WidgetMarkupOut"])).optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SectionOut"])
    types["GoogleAppsCardV1ActionParameterIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleAppsCardV1ActionParameterIn"])
    types["GoogleAppsCardV1ActionParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionParameterOut"])
    types["GoogleAppsCardV1ButtonIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]),
            "text": t.string().optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "altText": t.string().optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonIn"])
    types["GoogleAppsCardV1ButtonOut"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]),
            "text": t.string().optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "altText": t.string().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonOut"])
    types["MembershipIn"] = t.struct(
        {"name": t.string().optional(), "member": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "name": t.string().optional(),
            "member": t.proxy(renames["UserOut"]).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["ListSpacesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "spaces": t.array(t.proxy(renames["SpaceIn"])).optional(),
        }
    ).named(renames["ListSpacesResponseIn"])
    types["ListSpacesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "spaces": t.array(t.proxy(renames["SpaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSpacesResponseOut"])
    types["OpenLinkIn"] = t.struct({"url": t.string().optional()}).named(
        renames["OpenLinkIn"]
    )
    types["OpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenLinkOut"])
    types["GoogleAppsCardV1SelectionItemIn"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemIn"])
    types["GoogleAppsCardV1SelectionItemOut"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemOut"])
    types["GoogleAppsCardV1SwitchControlIn"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "controlType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlIn"])
    types["GoogleAppsCardV1SwitchControlOut"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "controlType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlOut"])
    types["GoogleAppsCardV1OnClickIn"] = t.struct(
        {
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkIn"]).optional(),
            "action": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickIn"])
    types["GoogleAppsCardV1OnClickOut"] = t.struct(
        {
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkOut"]).optional(),
            "action": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickOut"])
    types["GoogleAppsCardV1GridItemIn"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "layout": t.string().optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemIn"])
    types["GoogleAppsCardV1GridItemOut"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "layout": t.string().optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemOut"])
    types["FormActionIn"] = t.struct(
        {
            "actionMethodName": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ActionParameterIn"])).optional(),
        }
    ).named(renames["FormActionIn"])
    types["FormActionOut"] = t.struct(
        {
            "actionMethodName": t.string().optional(),
            "parameters": t.array(t.proxy(renames["ActionParameterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormActionOut"])
    types["GoogleAppsCardV1TextInputIn"] = t.struct(
        {
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
            "value": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsIn"]
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "hintText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputIn"])
    types["GoogleAppsCardV1TextInputOut"] = t.struct(
        {
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "value": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsOut"]
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "hintText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputOut"])
    types["DateInputIn"] = t.struct({"msSinceEpoch": t.string().optional()}).named(
        renames["DateInputIn"]
    )
    types["DateInputOut"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateInputOut"])
    types["AnnotationIn"] = t.struct(
        {
            "length": t.integer().optional(),
            "userMention": t.proxy(renames["UserMentionMetadataIn"]).optional(),
            "slashCommand": t.proxy(renames["SlashCommandMetadataIn"]).optional(),
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "length": t.integer().optional(),
            "userMention": t.proxy(renames["UserMentionMetadataOut"]).optional(),
            "slashCommand": t.proxy(renames["SlashCommandMetadataOut"]).optional(),
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["TextButtonIn"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "text": t.string().optional(),
        }
    ).named(renames["TextButtonIn"])
    types["TextButtonOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextButtonOut"])
    types["GoogleAppsCardV1ImageIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageIn"])
    types["GoogleAppsCardV1ImageOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageOut"])
    types["OnClickIn"] = t.struct(
        {
            "openLink": t.proxy(renames["OpenLinkIn"]).optional(),
            "action": t.proxy(renames["FormActionIn"]).optional(),
        }
    ).named(renames["OnClickIn"])
    types["OnClickOut"] = t.struct(
        {
            "openLink": t.proxy(renames["OpenLinkOut"]).optional(),
            "action": t.proxy(renames["FormActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnClickOut"])
    types["ColorIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "green": t.number().optional(),
            "blue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["TextParagraphIn"] = t.struct({"text": t.string()}).named(
        renames["TextParagraphIn"]
    )
    types["TextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextParagraphOut"])
    types["CardActionIn"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
        }
    ).named(renames["CardActionIn"])
    types["CardActionOut"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardActionOut"])
    types["GoogleAppsCardV1WidgetIn"] = t.struct(
        {
            "grid": t.proxy(renames["GoogleAppsCardV1GridIn"]).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextIn"]
            ).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerIn"]).optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageIn"]).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphIn"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputIn"]
            ).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputIn"]).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListIn"]).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetIn"])
    types["GoogleAppsCardV1WidgetOut"] = t.struct(
        {
            "grid": t.proxy(renames["GoogleAppsCardV1GridOut"]).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextOut"]
            ).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerOut"]).optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageOut"]).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphOut"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputOut"]
            ).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputOut"]).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListOut"]).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetOut"])
    types["ActionParameterIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["ActionParameterIn"])
    types["ActionParameterOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionParameterOut"])
    types["SpaceDetailsIn"] = t.struct(
        {"guidelines": t.string().optional(), "description": t.string().optional()}
    ).named(renames["SpaceDetailsIn"])
    types["SpaceDetailsOut"] = t.struct(
        {
            "guidelines": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceDetailsOut"])
    types["GoogleAppsCardV1SelectionInputIn"] = t.struct(
        {
            "name": t.string().optional(),
            "label": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemIn"])
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputIn"])
    types["GoogleAppsCardV1SelectionInputOut"] = t.struct(
        {
            "name": t.string().optional(),
            "label": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemOut"])
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputOut"])
    types["InputsIn"] = t.struct(
        {
            "dateTimeInput": t.proxy(renames["DateTimeInputIn"]).optional(),
            "stringInputs": t.proxy(renames["StringInputsIn"]).optional(),
            "dateInput": t.proxy(renames["DateInputIn"]).optional(),
            "timeInput": t.proxy(renames["TimeInputIn"]).optional(),
        }
    ).named(renames["InputsIn"])
    types["InputsOut"] = t.struct(
        {
            "dateTimeInput": t.proxy(renames["DateTimeInputOut"]).optional(),
            "stringInputs": t.proxy(renames["StringInputsOut"]).optional(),
            "dateInput": t.proxy(renames["DateInputOut"]).optional(),
            "timeInput": t.proxy(renames["TimeInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputsOut"])
    types["KeyValueIn"] = t.struct(
        {
            "content": t.string().optional(),
            "topLabel": t.string().optional(),
            "icon": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "button": t.proxy(renames["ButtonIn"]).optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "iconUrl": t.string().optional(),
            "bottomLabel": t.string().optional(),
        }
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "content": t.string().optional(),
            "topLabel": t.string().optional(),
            "icon": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "button": t.proxy(renames["ButtonOut"]).optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "iconUrl": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["GoogleAppsCardV1GridIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GoogleAppsCardV1GridItemIn"])).optional(),
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "title": t.string().optional(),
            "columnCount": t.integer().optional(),
        }
    ).named(renames["GoogleAppsCardV1GridIn"])
    types["GoogleAppsCardV1GridOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1GridItemOut"])
            ).optional(),
            "borderStyle": t.proxy(
                renames["GoogleAppsCardV1BorderStyleOut"]
            ).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "title": t.string().optional(),
            "columnCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridOut"])
    types["ButtonIn"] = t.struct(
        {
            "imageButton": t.proxy(renames["ImageButtonIn"]).optional(),
            "textButton": t.proxy(renames["TextButtonIn"]).optional(),
        }
    ).named(renames["ButtonIn"])
    types["ButtonOut"] = t.struct(
        {
            "imageButton": t.proxy(renames["ImageButtonOut"]).optional(),
            "textButton": t.proxy(renames["TextButtonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ButtonOut"])
    types["GoogleAppsCardV1ImageCropStyleIn"] = t.struct(
        {"aspectRatio": t.number().optional(), "type": t.string().optional()}
    ).named(renames["GoogleAppsCardV1ImageCropStyleIn"])
    types["GoogleAppsCardV1ImageCropStyleOut"] = t.struct(
        {
            "aspectRatio": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageCropStyleOut"])
    types["TimeZoneIn"] = t.struct(
        {"id": t.string().optional(), "offset": t.integer().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "id": t.string().optional(),
            "offset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["CommonEventObjectIn"] = t.struct(
        {
            "hostApp": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "invokedFunction": t.string().optional(),
            "userLocale": t.string().optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
            "platform": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
        }
    ).named(renames["CommonEventObjectIn"])
    types["CommonEventObjectOut"] = t.struct(
        {
            "hostApp": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "invokedFunction": t.string().optional(),
            "userLocale": t.string().optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
            "platform": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonEventObjectOut"])
    types["ImageIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "aspectRatio": t.number().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["CardIn"] = t.struct(
        {
            "sections": t.array(t.proxy(renames["SectionIn"])).optional(),
            "header": t.proxy(renames["CardHeaderIn"]).optional(),
            "cardActions": t.array(t.proxy(renames["CardActionIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CardIn"])
    types["CardOut"] = t.struct(
        {
            "sections": t.array(t.proxy(renames["SectionOut"])).optional(),
            "header": t.proxy(renames["CardHeaderOut"]).optional(),
            "cardActions": t.array(t.proxy(renames["CardActionOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardOut"])
    types["GoogleAppsCardV1CardFixedFooterIn"] = t.struct(
        {
            "primaryButton": t.proxy(renames["GoogleAppsCardV1ButtonIn"]).optional(),
            "secondaryButton": t.proxy(renames["GoogleAppsCardV1ButtonIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardFixedFooterIn"])
    types["GoogleAppsCardV1CardFixedFooterOut"] = t.struct(
        {
            "primaryButton": t.proxy(renames["GoogleAppsCardV1ButtonOut"]).optional(),
            "secondaryButton": t.proxy(renames["GoogleAppsCardV1ButtonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardFixedFooterOut"])
    types["GoogleAppsCardV1DecoratedTextIn"] = t.struct(
        {
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlIn"]
            ).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "bottomLabel": t.string().optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonIn"]).optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "text": t.string(),
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "wrapText": t.boolean().optional(),
            "topLabel": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextIn"])
    types["GoogleAppsCardV1DecoratedTextOut"] = t.struct(
        {
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlOut"]
            ).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "bottomLabel": t.string().optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonOut"]).optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "text": t.string(),
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "wrapText": t.boolean().optional(),
            "topLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextOut"])
    types["GoogleAppsCardV1ButtonListIn"] = t.struct(
        {"buttons": t.array(t.proxy(renames["GoogleAppsCardV1ButtonIn"])).optional()}
    ).named(renames["GoogleAppsCardV1ButtonListIn"])
    types["GoogleAppsCardV1ButtonListOut"] = t.struct(
        {
            "buttons": t.array(
                t.proxy(renames["GoogleAppsCardV1ButtonOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonListOut"])

    functions = {}
    functions["spacesGet"] = chat.get(
        "v1/spaces",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSpacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesList"] = chat.get(
        "v1/spaces",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSpacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesPatch"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesCreate"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesUpdate"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesGet"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesDelete"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesAttachmentsGet"] = chat.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AttachmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMembersGet"] = chat.get(
        "v1/{parent}/members",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMembersList"] = chat.get(
        "v1/{parent}/members",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = chat.get(
        "v1/media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="chat", renames=renames, types=types, functions=functions)
