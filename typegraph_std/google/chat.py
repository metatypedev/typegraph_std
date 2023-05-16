from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_chat() -> Import:
    chat = HTTPRuntime("https://chat.googleapis.com/")

    renames = {
        "ErrorResponse": "_chat_1_ErrorResponse",
        "MediaIn": "_chat_2_MediaIn",
        "MediaOut": "_chat_3_MediaOut",
        "CommonEventObjectIn": "_chat_4_CommonEventObjectIn",
        "CommonEventObjectOut": "_chat_5_CommonEventObjectOut",
        "DialogIn": "_chat_6_DialogIn",
        "DialogOut": "_chat_7_DialogOut",
        "GoogleAppsCardV1TextInputIn": "_chat_8_GoogleAppsCardV1TextInputIn",
        "GoogleAppsCardV1TextInputOut": "_chat_9_GoogleAppsCardV1TextInputOut",
        "GoogleAppsCardV1OnClickIn": "_chat_10_GoogleAppsCardV1OnClickIn",
        "GoogleAppsCardV1OnClickOut": "_chat_11_GoogleAppsCardV1OnClickOut",
        "CardIn": "_chat_12_CardIn",
        "CardOut": "_chat_13_CardOut",
        "DateTimeInputIn": "_chat_14_DateTimeInputIn",
        "DateTimeInputOut": "_chat_15_DateTimeInputOut",
        "WidgetMarkupIn": "_chat_16_WidgetMarkupIn",
        "WidgetMarkupOut": "_chat_17_WidgetMarkupOut",
        "TimeInputIn": "_chat_18_TimeInputIn",
        "TimeInputOut": "_chat_19_TimeInputOut",
        "TextParagraphIn": "_chat_20_TextParagraphIn",
        "TextParagraphOut": "_chat_21_TextParagraphOut",
        "SlashCommandMetadataIn": "_chat_22_SlashCommandMetadataIn",
        "SlashCommandMetadataOut": "_chat_23_SlashCommandMetadataOut",
        "ActionResponseIn": "_chat_24_ActionResponseIn",
        "ActionResponseOut": "_chat_25_ActionResponseOut",
        "ActionParameterIn": "_chat_26_ActionParameterIn",
        "ActionParameterOut": "_chat_27_ActionParameterOut",
        "GoogleAppsCardV1ImageIn": "_chat_28_GoogleAppsCardV1ImageIn",
        "GoogleAppsCardV1ImageOut": "_chat_29_GoogleAppsCardV1ImageOut",
        "GoogleAppsCardV1GridItemIn": "_chat_30_GoogleAppsCardV1GridItemIn",
        "GoogleAppsCardV1GridItemOut": "_chat_31_GoogleAppsCardV1GridItemOut",
        "TimeZoneIn": "_chat_32_TimeZoneIn",
        "TimeZoneOut": "_chat_33_TimeZoneOut",
        "GoogleAppsCardV1ActionIn": "_chat_34_GoogleAppsCardV1ActionIn",
        "GoogleAppsCardV1ActionOut": "_chat_35_GoogleAppsCardV1ActionOut",
        "ThreadIn": "_chat_36_ThreadIn",
        "ThreadOut": "_chat_37_ThreadOut",
        "GoogleAppsCardV1SuggestionsIn": "_chat_38_GoogleAppsCardV1SuggestionsIn",
        "GoogleAppsCardV1SuggestionsOut": "_chat_39_GoogleAppsCardV1SuggestionsOut",
        "GoogleAppsCardV1SwitchControlIn": "_chat_40_GoogleAppsCardV1SwitchControlIn",
        "GoogleAppsCardV1SwitchControlOut": "_chat_41_GoogleAppsCardV1SwitchControlOut",
        "MatchedUrlIn": "_chat_42_MatchedUrlIn",
        "MatchedUrlOut": "_chat_43_MatchedUrlOut",
        "ActionStatusIn": "_chat_44_ActionStatusIn",
        "ActionStatusOut": "_chat_45_ActionStatusOut",
        "KeyValueIn": "_chat_46_KeyValueIn",
        "KeyValueOut": "_chat_47_KeyValueOut",
        "UserIn": "_chat_48_UserIn",
        "UserOut": "_chat_49_UserOut",
        "GoogleAppsCardV1ButtonListIn": "_chat_50_GoogleAppsCardV1ButtonListIn",
        "GoogleAppsCardV1ButtonListOut": "_chat_51_GoogleAppsCardV1ButtonListOut",
        "DeprecatedEventIn": "_chat_52_DeprecatedEventIn",
        "DeprecatedEventOut": "_chat_53_DeprecatedEventOut",
        "DialogActionIn": "_chat_54_DialogActionIn",
        "DialogActionOut": "_chat_55_DialogActionOut",
        "AnnotationIn": "_chat_56_AnnotationIn",
        "AnnotationOut": "_chat_57_AnnotationOut",
        "GoogleAppsCardV1GridIn": "_chat_58_GoogleAppsCardV1GridIn",
        "GoogleAppsCardV1GridOut": "_chat_59_GoogleAppsCardV1GridOut",
        "GoogleAppsCardV1BorderStyleIn": "_chat_60_GoogleAppsCardV1BorderStyleIn",
        "GoogleAppsCardV1BorderStyleOut": "_chat_61_GoogleAppsCardV1BorderStyleOut",
        "GoogleAppsCardV1ButtonIn": "_chat_62_GoogleAppsCardV1ButtonIn",
        "GoogleAppsCardV1ButtonOut": "_chat_63_GoogleAppsCardV1ButtonOut",
        "GoogleAppsCardV1SuggestionItemIn": "_chat_64_GoogleAppsCardV1SuggestionItemIn",
        "GoogleAppsCardV1SuggestionItemOut": "_chat_65_GoogleAppsCardV1SuggestionItemOut",
        "OpenLinkIn": "_chat_66_OpenLinkIn",
        "OpenLinkOut": "_chat_67_OpenLinkOut",
        "StringInputsIn": "_chat_68_StringInputsIn",
        "StringInputsOut": "_chat_69_StringInputsOut",
        "GoogleAppsCardV1SelectionItemIn": "_chat_70_GoogleAppsCardV1SelectionItemIn",
        "GoogleAppsCardV1SelectionItemOut": "_chat_71_GoogleAppsCardV1SelectionItemOut",
        "GoogleAppsCardV1TextParagraphIn": "_chat_72_GoogleAppsCardV1TextParagraphIn",
        "GoogleAppsCardV1TextParagraphOut": "_chat_73_GoogleAppsCardV1TextParagraphOut",
        "ListSpacesResponseIn": "_chat_74_ListSpacesResponseIn",
        "ListSpacesResponseOut": "_chat_75_ListSpacesResponseOut",
        "SlashCommandIn": "_chat_76_SlashCommandIn",
        "SlashCommandOut": "_chat_77_SlashCommandOut",
        "DateInputIn": "_chat_78_DateInputIn",
        "DateInputOut": "_chat_79_DateInputOut",
        "GoogleAppsCardV1IconIn": "_chat_80_GoogleAppsCardV1IconIn",
        "GoogleAppsCardV1IconOut": "_chat_81_GoogleAppsCardV1IconOut",
        "GoogleAppsCardV1CardFixedFooterIn": "_chat_82_GoogleAppsCardV1CardFixedFooterIn",
        "GoogleAppsCardV1CardFixedFooterOut": "_chat_83_GoogleAppsCardV1CardFixedFooterOut",
        "TextButtonIn": "_chat_84_TextButtonIn",
        "TextButtonOut": "_chat_85_TextButtonOut",
        "SectionIn": "_chat_86_SectionIn",
        "SectionOut": "_chat_87_SectionOut",
        "GoogleAppsCardV1SectionIn": "_chat_88_GoogleAppsCardV1SectionIn",
        "GoogleAppsCardV1SectionOut": "_chat_89_GoogleAppsCardV1SectionOut",
        "GoogleAppsCardV1OpenLinkIn": "_chat_90_GoogleAppsCardV1OpenLinkIn",
        "GoogleAppsCardV1OpenLinkOut": "_chat_91_GoogleAppsCardV1OpenLinkOut",
        "AttachmentIn": "_chat_92_AttachmentIn",
        "AttachmentOut": "_chat_93_AttachmentOut",
        "GoogleAppsCardV1ActionParameterIn": "_chat_94_GoogleAppsCardV1ActionParameterIn",
        "GoogleAppsCardV1ActionParameterOut": "_chat_95_GoogleAppsCardV1ActionParameterOut",
        "GoogleAppsCardV1DividerIn": "_chat_96_GoogleAppsCardV1DividerIn",
        "GoogleAppsCardV1DividerOut": "_chat_97_GoogleAppsCardV1DividerOut",
        "EmptyIn": "_chat_98_EmptyIn",
        "EmptyOut": "_chat_99_EmptyOut",
        "GoogleAppsCardV1SelectionInputIn": "_chat_100_GoogleAppsCardV1SelectionInputIn",
        "GoogleAppsCardV1SelectionInputOut": "_chat_101_GoogleAppsCardV1SelectionInputOut",
        "FormActionIn": "_chat_102_FormActionIn",
        "FormActionOut": "_chat_103_FormActionOut",
        "GoogleAppsCardV1DateTimePickerIn": "_chat_104_GoogleAppsCardV1DateTimePickerIn",
        "GoogleAppsCardV1DateTimePickerOut": "_chat_105_GoogleAppsCardV1DateTimePickerOut",
        "GoogleAppsCardV1CardIn": "_chat_106_GoogleAppsCardV1CardIn",
        "GoogleAppsCardV1CardOut": "_chat_107_GoogleAppsCardV1CardOut",
        "AttachmentDataRefIn": "_chat_108_AttachmentDataRefIn",
        "AttachmentDataRefOut": "_chat_109_AttachmentDataRefOut",
        "OnClickIn": "_chat_110_OnClickIn",
        "OnClickOut": "_chat_111_OnClickOut",
        "MembershipIn": "_chat_112_MembershipIn",
        "MembershipOut": "_chat_113_MembershipOut",
        "MessageIn": "_chat_114_MessageIn",
        "MessageOut": "_chat_115_MessageOut",
        "ButtonIn": "_chat_116_ButtonIn",
        "ButtonOut": "_chat_117_ButtonOut",
        "DriveDataRefIn": "_chat_118_DriveDataRefIn",
        "DriveDataRefOut": "_chat_119_DriveDataRefOut",
        "GoogleAppsCardV1DecoratedTextIn": "_chat_120_GoogleAppsCardV1DecoratedTextIn",
        "GoogleAppsCardV1DecoratedTextOut": "_chat_121_GoogleAppsCardV1DecoratedTextOut",
        "UserMentionMetadataIn": "_chat_122_UserMentionMetadataIn",
        "UserMentionMetadataOut": "_chat_123_UserMentionMetadataOut",
        "ImageIn": "_chat_124_ImageIn",
        "ImageOut": "_chat_125_ImageOut",
        "StatusIn": "_chat_126_StatusIn",
        "StatusOut": "_chat_127_StatusOut",
        "CardHeaderIn": "_chat_128_CardHeaderIn",
        "CardHeaderOut": "_chat_129_CardHeaderOut",
        "GoogleAppsCardV1WidgetIn": "_chat_130_GoogleAppsCardV1WidgetIn",
        "GoogleAppsCardV1WidgetOut": "_chat_131_GoogleAppsCardV1WidgetOut",
        "ColorIn": "_chat_132_ColorIn",
        "ColorOut": "_chat_133_ColorOut",
        "ImageButtonIn": "_chat_134_ImageButtonIn",
        "ImageButtonOut": "_chat_135_ImageButtonOut",
        "CardActionIn": "_chat_136_CardActionIn",
        "CardActionOut": "_chat_137_CardActionOut",
        "SpaceDetailsIn": "_chat_138_SpaceDetailsIn",
        "SpaceDetailsOut": "_chat_139_SpaceDetailsOut",
        "GoogleAppsCardV1ImageCropStyleIn": "_chat_140_GoogleAppsCardV1ImageCropStyleIn",
        "GoogleAppsCardV1ImageCropStyleOut": "_chat_141_GoogleAppsCardV1ImageCropStyleOut",
        "GoogleAppsCardV1ImageComponentIn": "_chat_142_GoogleAppsCardV1ImageComponentIn",
        "GoogleAppsCardV1ImageComponentOut": "_chat_143_GoogleAppsCardV1ImageComponentOut",
        "GoogleAppsCardV1CardActionIn": "_chat_144_GoogleAppsCardV1CardActionIn",
        "GoogleAppsCardV1CardActionOut": "_chat_145_GoogleAppsCardV1CardActionOut",
        "InputsIn": "_chat_146_InputsIn",
        "InputsOut": "_chat_147_InputsOut",
        "GoogleAppsCardV1CardHeaderIn": "_chat_148_GoogleAppsCardV1CardHeaderIn",
        "GoogleAppsCardV1CardHeaderOut": "_chat_149_GoogleAppsCardV1CardHeaderOut",
        "ListMembershipsResponseIn": "_chat_150_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_chat_151_ListMembershipsResponseOut",
        "CardWithIdIn": "_chat_152_CardWithIdIn",
        "CardWithIdOut": "_chat_153_CardWithIdOut",
        "ChatAppLogEntryIn": "_chat_154_ChatAppLogEntryIn",
        "ChatAppLogEntryOut": "_chat_155_ChatAppLogEntryOut",
        "SpaceIn": "_chat_156_SpaceIn",
        "SpaceOut": "_chat_157_SpaceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["CommonEventObjectIn"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "hostApp": t.string().optional(),
            "platform": t.string().optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "userLocale": t.string().optional(),
            "invokedFunction": t.string().optional(),
        }
    ).named(renames["CommonEventObjectIn"])
    types["CommonEventObjectOut"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "hostApp": t.string().optional(),
            "platform": t.string().optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "userLocale": t.string().optional(),
            "invokedFunction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonEventObjectOut"])
    types["DialogIn"] = t.struct(
        {"body": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional()}
    ).named(renames["DialogIn"])
    types["DialogOut"] = t.struct(
        {
            "body": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DialogOut"])
    types["GoogleAppsCardV1TextInputIn"] = t.struct(
        {
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsIn"]
            ).optional(),
            "hintText": t.string().optional(),
            "label": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputIn"])
    types["GoogleAppsCardV1TextInputOut"] = t.struct(
        {
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsOut"]
            ).optional(),
            "hintText": t.string().optional(),
            "label": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputOut"])
    types["GoogleAppsCardV1OnClickIn"] = t.struct(
        {
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkIn"]).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional(),
            "action": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickIn"])
    types["GoogleAppsCardV1OnClickOut"] = t.struct(
        {
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkOut"]).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "action": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickOut"])
    types["CardIn"] = t.struct(
        {
            "cardActions": t.array(t.proxy(renames["CardActionIn"])).optional(),
            "header": t.proxy(renames["CardHeaderIn"]).optional(),
            "name": t.string().optional(),
            "sections": t.array(t.proxy(renames["SectionIn"])).optional(),
        }
    ).named(renames["CardIn"])
    types["CardOut"] = t.struct(
        {
            "cardActions": t.array(t.proxy(renames["CardActionOut"])).optional(),
            "header": t.proxy(renames["CardHeaderOut"]).optional(),
            "name": t.string().optional(),
            "sections": t.array(t.proxy(renames["SectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardOut"])
    types["DateTimeInputIn"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "hasTime": t.boolean().optional(),
            "hasDate": t.boolean().optional(),
        }
    ).named(renames["DateTimeInputIn"])
    types["DateTimeInputOut"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "hasTime": t.boolean().optional(),
            "hasDate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeInputOut"])
    types["WidgetMarkupIn"] = t.struct(
        {
            "textParagraph": t.proxy(renames["TextParagraphIn"]).optional(),
            "buttons": t.array(t.proxy(renames["ButtonIn"])).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "keyValue": t.proxy(renames["KeyValueIn"]).optional(),
        }
    ).named(renames["WidgetMarkupIn"])
    types["WidgetMarkupOut"] = t.struct(
        {
            "textParagraph": t.proxy(renames["TextParagraphOut"]).optional(),
            "buttons": t.array(t.proxy(renames["ButtonOut"])).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "keyValue": t.proxy(renames["KeyValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WidgetMarkupOut"])
    types["TimeInputIn"] = t.struct(
        {"minutes": t.integer().optional(), "hours": t.integer().optional()}
    ).named(renames["TimeInputIn"])
    types["TimeInputOut"] = t.struct(
        {
            "minutes": t.integer().optional(),
            "hours": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeInputOut"])
    types["TextParagraphIn"] = t.struct({"text": t.string()}).named(
        renames["TextParagraphIn"]
    )
    types["TextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextParagraphOut"])
    types["SlashCommandMetadataIn"] = t.struct(
        {
            "commandId": t.string().optional(),
            "triggersDialog": t.boolean().optional(),
            "bot": t.proxy(renames["UserIn"]).optional(),
            "commandName": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["SlashCommandMetadataIn"])
    types["SlashCommandMetadataOut"] = t.struct(
        {
            "commandId": t.string().optional(),
            "triggersDialog": t.boolean().optional(),
            "bot": t.proxy(renames["UserOut"]).optional(),
            "commandName": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandMetadataOut"])
    types["ActionResponseIn"] = t.struct(
        {
            "type": t.string().optional(),
            "dialogAction": t.proxy(renames["DialogActionIn"]).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ActionResponseIn"])
    types["ActionResponseOut"] = t.struct(
        {
            "type": t.string().optional(),
            "dialogAction": t.proxy(renames["DialogActionOut"]).optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionResponseOut"])
    types["ActionParameterIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["ActionParameterIn"])
    types["ActionParameterOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionParameterOut"])
    types["GoogleAppsCardV1ImageIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageIn"])
    types["GoogleAppsCardV1ImageOut"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "altText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageOut"])
    types["GoogleAppsCardV1GridItemIn"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentIn"]).optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "layout": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemIn"])
    types["GoogleAppsCardV1GridItemOut"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentOut"]).optional(),
            "subtitle": t.string().optional(),
            "title": t.string().optional(),
            "layout": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemOut"])
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
    types["GoogleAppsCardV1ActionIn"] = t.struct(
        {
            "interaction": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterIn"])
            ).optional(),
            "loadIndicator": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionIn"])
    types["GoogleAppsCardV1ActionOut"] = t.struct(
        {
            "interaction": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterOut"])
            ).optional(),
            "loadIndicator": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionOut"])
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
    types["GoogleAppsCardV1SwitchControlIn"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "controlType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlIn"])
    types["GoogleAppsCardV1SwitchControlOut"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "name": t.string().optional(),
            "controlType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlOut"])
    types["MatchedUrlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatchedUrlIn"]
    )
    types["MatchedUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchedUrlOut"])
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
    types["KeyValueIn"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "topLabel": t.string().optional(),
            "icon": t.string().optional(),
            "content": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "iconUrl": t.string().optional(),
            "button": t.proxy(renames["ButtonIn"]).optional(),
        }
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "topLabel": t.string().optional(),
            "icon": t.string().optional(),
            "content": t.string().optional(),
            "bottomLabel": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "iconUrl": t.string().optional(),
            "button": t.proxy(renames["ButtonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["UserIn"] = t.struct(
        {
            "name": t.string().optional(),
            "domainId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "domainId": t.string().optional(),
            "type": t.string().optional(),
            "isAnonymous": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
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
    types["DeprecatedEventIn"] = t.struct(
        {
            "user": t.proxy(renames["UserIn"]).optional(),
            "isDialogEvent": t.boolean().optional(),
            "threadKey": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectIn"]).optional(),
            "action": t.proxy(renames["FormActionIn"]).optional(),
            "dialogEventType": t.string().optional(),
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "type": t.string().optional(),
            "eventTime": t.string().optional(),
            "token": t.string().optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
        }
    ).named(renames["DeprecatedEventIn"])
    types["DeprecatedEventOut"] = t.struct(
        {
            "user": t.proxy(renames["UserOut"]).optional(),
            "isDialogEvent": t.boolean().optional(),
            "threadKey": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectOut"]).optional(),
            "action": t.proxy(renames["FormActionOut"]).optional(),
            "dialogEventType": t.string().optional(),
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "type": t.string().optional(),
            "eventTime": t.string().optional(),
            "token": t.string().optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeprecatedEventOut"])
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
    types["AnnotationIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "slashCommand": t.proxy(renames["SlashCommandMetadataIn"]).optional(),
            "userMention": t.proxy(renames["UserMentionMetadataIn"]).optional(),
            "length": t.integer().optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "slashCommand": t.proxy(renames["SlashCommandMetadataOut"]).optional(),
            "userMention": t.proxy(renames["UserMentionMetadataOut"]).optional(),
            "length": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["GoogleAppsCardV1GridIn"] = t.struct(
        {
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "title": t.string().optional(),
            "items": t.array(t.proxy(renames["GoogleAppsCardV1GridItemIn"])).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "columnCount": t.integer().optional(),
        }
    ).named(renames["GoogleAppsCardV1GridIn"])
    types["GoogleAppsCardV1GridOut"] = t.struct(
        {
            "borderStyle": t.proxy(
                renames["GoogleAppsCardV1BorderStyleOut"]
            ).optional(),
            "title": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1GridItemOut"])
            ).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "columnCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridOut"])
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
    types["GoogleAppsCardV1ButtonIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "disabled": t.boolean().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonIn"])
    types["GoogleAppsCardV1ButtonOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "disabled": t.boolean().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonOut"])
    types["GoogleAppsCardV1SuggestionItemIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1SuggestionItemIn"])
    types["GoogleAppsCardV1SuggestionItemOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SuggestionItemOut"])
    types["OpenLinkIn"] = t.struct({"url": t.string().optional()}).named(
        renames["OpenLinkIn"]
    )
    types["OpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenLinkOut"])
    types["StringInputsIn"] = t.struct({"value": t.array(t.string()).optional()}).named(
        renames["StringInputsIn"]
    )
    types["StringInputsOut"] = t.struct(
        {
            "value": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringInputsOut"])
    types["GoogleAppsCardV1SelectionItemIn"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemIn"])
    types["GoogleAppsCardV1SelectionItemOut"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "value": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemOut"])
    types["GoogleAppsCardV1TextParagraphIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1TextParagraphIn"])
    types["GoogleAppsCardV1TextParagraphOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextParagraphOut"])
    types["ListSpacesResponseIn"] = t.struct(
        {
            "spaces": t.array(t.proxy(renames["SpaceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSpacesResponseIn"])
    types["ListSpacesResponseOut"] = t.struct(
        {
            "spaces": t.array(t.proxy(renames["SpaceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSpacesResponseOut"])
    types["SlashCommandIn"] = t.struct({"commandId": t.string().optional()}).named(
        renames["SlashCommandIn"]
    )
    types["SlashCommandOut"] = t.struct(
        {
            "commandId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandOut"])
    types["DateInputIn"] = t.struct({"msSinceEpoch": t.string().optional()}).named(
        renames["DateInputIn"]
    )
    types["DateInputOut"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateInputOut"])
    types["GoogleAppsCardV1IconIn"] = t.struct(
        {
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1IconIn"])
    types["GoogleAppsCardV1IconOut"] = t.struct(
        {
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1IconOut"])
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
    types["TextButtonIn"] = t.struct(
        {
            "text": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
        }
    ).named(renames["TextButtonIn"])
    types["TextButtonOut"] = t.struct(
        {
            "text": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextButtonOut"])
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
    types["GoogleAppsCardV1SectionIn"] = t.struct(
        {
            "header": t.string().optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "widgets": t.array(t.proxy(renames["GoogleAppsCardV1WidgetIn"])).optional(),
            "collapsible": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCardV1SectionIn"])
    types["GoogleAppsCardV1SectionOut"] = t.struct(
        {
            "header": t.string().optional(),
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "widgets": t.array(
                t.proxy(renames["GoogleAppsCardV1WidgetOut"])
            ).optional(),
            "collapsible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SectionOut"])
    types["GoogleAppsCardV1OpenLinkIn"] = t.struct(
        {
            "onClose": t.string().optional(),
            "openAs": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1OpenLinkIn"])
    types["GoogleAppsCardV1OpenLinkOut"] = t.struct(
        {
            "onClose": t.string().optional(),
            "openAs": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OpenLinkOut"])
    types["AttachmentIn"] = t.struct(
        {
            "contentName": t.string().optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefIn"]).optional(),
            "name": t.string().optional(),
            "source": t.string().optional(),
            "contentType": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefIn"]).optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "contentName": t.string().optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefOut"]).optional(),
            "name": t.string().optional(),
            "source": t.string().optional(),
            "contentType": t.string().optional(),
            "thumbnailUri": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefOut"]).optional(),
            "downloadUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["GoogleAppsCardV1ActionParameterIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["GoogleAppsCardV1ActionParameterIn"])
    types["GoogleAppsCardV1ActionParameterOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionParameterOut"])
    types["GoogleAppsCardV1DividerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsCardV1DividerIn"]
    )
    types["GoogleAppsCardV1DividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCardV1DividerOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleAppsCardV1SelectionInputIn"] = t.struct(
        {
            "type": t.string().optional(),
            "label": t.string().optional(),
            "name": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemIn"])
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputIn"])
    types["GoogleAppsCardV1SelectionInputOut"] = t.struct(
        {
            "type": t.string().optional(),
            "label": t.string().optional(),
            "name": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemOut"])
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputOut"])
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
    types["GoogleAppsCardV1DateTimePickerIn"] = t.struct(
        {
            "timezoneOffsetDate": t.integer().optional(),
            "valueMsEpoch": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerIn"])
    types["GoogleAppsCardV1DateTimePickerOut"] = t.struct(
        {
            "timezoneOffsetDate": t.integer().optional(),
            "valueMsEpoch": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerOut"])
    types["GoogleAppsCardV1CardIn"] = t.struct(
        {
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterIn"]
            ).optional(),
            "displayStyle": t.string().optional(),
            "name": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionIn"])
            ).optional(),
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderIn"]
            ).optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderIn"]).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionIn"])
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardIn"])
    types["GoogleAppsCardV1CardOut"] = t.struct(
        {
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterOut"]
            ).optional(),
            "displayStyle": t.string().optional(),
            "name": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionOut"])
            ).optional(),
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderOut"]
            ).optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderOut"]).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardOut"])
    types["AttachmentDataRefIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["AttachmentDataRefIn"])
    types["AttachmentDataRefOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentDataRefOut"])
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
    types["MembershipIn"] = t.struct(
        {"name": t.string().optional(), "member": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "role": t.string().optional(),
            "member": t.proxy(renames["UserOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["MessageIn"] = t.struct(
        {
            "clientAssignedMessageId": t.string().optional(),
            "name": t.string().optional(),
            "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "fallbackText": t.string().optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "text": t.string().optional(),
            "cards": t.array(t.proxy(renames["CardIn"])).optional(),
            "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
            "thread": t.proxy(renames["ThreadIn"]).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "clientAssignedMessageId": t.string().optional(),
            "slashCommand": t.proxy(renames["SlashCommandOut"]).optional(),
            "name": t.string().optional(),
            "attachment": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "fallbackText": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "sender": t.proxy(renames["UserOut"]).optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdOut"])).optional(),
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "text": t.string().optional(),
            "cards": t.array(t.proxy(renames["CardOut"])).optional(),
            "actionResponse": t.proxy(renames["ActionResponseOut"]).optional(),
            "matchedUrl": t.proxy(renames["MatchedUrlOut"]).optional(),
            "argumentText": t.string().optional(),
            "createTime": t.string().optional(),
            "thread": t.proxy(renames["ThreadOut"]).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "threadReply": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["ButtonIn"] = t.struct(
        {
            "textButton": t.proxy(renames["TextButtonIn"]).optional(),
            "imageButton": t.proxy(renames["ImageButtonIn"]).optional(),
        }
    ).named(renames["ButtonIn"])
    types["ButtonOut"] = t.struct(
        {
            "textButton": t.proxy(renames["TextButtonOut"]).optional(),
            "imageButton": t.proxy(renames["ImageButtonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ButtonOut"])
    types["DriveDataRefIn"] = t.struct({"driveFileId": t.string().optional()}).named(
        renames["DriveDataRefIn"]
    )
    types["DriveDataRefOut"] = t.struct(
        {
            "driveFileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveDataRefOut"])
    types["GoogleAppsCardV1DecoratedTextIn"] = t.struct(
        {
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "topLabel": t.string().optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "text": t.string(),
            "bottomLabel": t.string().optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonIn"]).optional(),
            "wrapText": t.boolean().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextIn"])
    types["GoogleAppsCardV1DecoratedTextOut"] = t.struct(
        {
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "topLabel": t.string().optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "text": t.string(),
            "bottomLabel": t.string().optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonOut"]).optional(),
            "wrapText": t.boolean().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextOut"])
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
    types["ImageIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["CardHeaderIn"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["CardHeaderIn"])
    types["CardHeaderOut"] = t.struct(
        {
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardHeaderOut"])
    types["GoogleAppsCardV1WidgetIn"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageIn"]).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphIn"]
            ).optional(),
            "grid": t.proxy(renames["GoogleAppsCardV1GridIn"]).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListIn"]).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputIn"]).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerIn"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextIn"]
            ).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerIn"]).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetIn"])
    types["GoogleAppsCardV1WidgetOut"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageOut"]).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphOut"]
            ).optional(),
            "grid": t.proxy(renames["GoogleAppsCardV1GridOut"]).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListOut"]).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputOut"]).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerOut"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextOut"]
            ).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerOut"]).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetOut"])
    types["ColorIn"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["ImageButtonIn"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "name": t.string().optional(),
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
        }
    ).named(renames["ImageButtonIn"])
    types["ImageButtonOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "name": t.string().optional(),
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageButtonOut"])
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
    types["GoogleAppsCardV1ImageComponentIn"] = t.struct(
        {
            "cropStyle": t.proxy(
                renames["GoogleAppsCardV1ImageCropStyleIn"]
            ).optional(),
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "imageUri": t.string().optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageComponentIn"])
    types["GoogleAppsCardV1ImageComponentOut"] = t.struct(
        {
            "cropStyle": t.proxy(
                renames["GoogleAppsCardV1ImageCropStyleOut"]
            ).optional(),
            "borderStyle": t.proxy(
                renames["GoogleAppsCardV1BorderStyleOut"]
            ).optional(),
            "imageUri": t.string().optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageComponentOut"])
    types["GoogleAppsCardV1CardActionIn"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardActionIn"])
    types["GoogleAppsCardV1CardActionOut"] = t.struct(
        {
            "actionLabel": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardActionOut"])
    types["InputsIn"] = t.struct(
        {
            "stringInputs": t.proxy(renames["StringInputsIn"]).optional(),
            "dateTimeInput": t.proxy(renames["DateTimeInputIn"]).optional(),
            "dateInput": t.proxy(renames["DateInputIn"]).optional(),
            "timeInput": t.proxy(renames["TimeInputIn"]).optional(),
        }
    ).named(renames["InputsIn"])
    types["InputsOut"] = t.struct(
        {
            "stringInputs": t.proxy(renames["StringInputsOut"]).optional(),
            "dateTimeInput": t.proxy(renames["DateTimeInputOut"]).optional(),
            "dateInput": t.proxy(renames["DateInputOut"]).optional(),
            "timeInput": t.proxy(renames["TimeInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputsOut"])
    types["GoogleAppsCardV1CardHeaderIn"] = t.struct(
        {
            "title": t.string(),
            "imageAltText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderIn"])
    types["GoogleAppsCardV1CardHeaderOut"] = t.struct(
        {
            "title": t.string(),
            "imageAltText": t.string().optional(),
            "imageUrl": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderOut"])
    types["ListMembershipsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
        }
    ).named(renames["ListMembershipsResponseIn"])
    types["ListMembershipsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMembershipsResponseOut"])
    types["CardWithIdIn"] = t.struct(
        {
            "card": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional(),
            "cardId": t.string(),
        }
    ).named(renames["CardWithIdIn"])
    types["CardWithIdOut"] = t.struct(
        {
            "card": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "cardId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardWithIdOut"])
    types["ChatAppLogEntryIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "deploymentFunction": t.string().optional(),
            "deployment": t.string().optional(),
        }
    ).named(renames["ChatAppLogEntryIn"])
    types["ChatAppLogEntryOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "deploymentFunction": t.string().optional(),
            "deployment": t.string().optional(),
        }
    ).named(renames["ChatAppLogEntryOut"])
    types["SpaceIn"] = t.struct(
        {
            "spaceDetails": t.proxy(renames["SpaceDetailsIn"]).optional(),
            "displayName": t.string().optional(),
            "singleUserBotDm": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SpaceIn"])
    types["SpaceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "spaceDetails": t.proxy(renames["SpaceDetailsOut"]).optional(),
            "displayName": t.string().optional(),
            "spaceThreadingState": t.string().optional(),
            "singleUserBotDm": t.boolean().optional(),
            "name": t.string().optional(),
            "adminInstalled": t.boolean().optional(),
            "threaded": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceOut"])

    functions = {}
    functions["mediaDownload"] = chat.get(
        "v1/media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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
    functions["spacesMembersGet"] = chat.get(
        "v1/{parent}/members",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListMembershipsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesGet"] = chat.post(
        "v1/{parent}/messages",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "messageReplyOption": t.string().optional(),
                "threadKey": t.string().optional(),
                "messageId": t.string().optional(),
                "clientAssignedMessageId": t.string().optional(),
                "name": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "fallbackText": t.string().optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "text": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesPatch"] = chat.post(
        "v1/{parent}/messages",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "messageReplyOption": t.string().optional(),
                "threadKey": t.string().optional(),
                "messageId": t.string().optional(),
                "clientAssignedMessageId": t.string().optional(),
                "name": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "fallbackText": t.string().optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "text": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesDelete"] = chat.post(
        "v1/{parent}/messages",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "messageReplyOption": t.string().optional(),
                "threadKey": t.string().optional(),
                "messageId": t.string().optional(),
                "clientAssignedMessageId": t.string().optional(),
                "name": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "fallbackText": t.string().optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "text": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesUpdate"] = chat.post(
        "v1/{parent}/messages",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "messageReplyOption": t.string().optional(),
                "threadKey": t.string().optional(),
                "messageId": t.string().optional(),
                "clientAssignedMessageId": t.string().optional(),
                "name": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "fallbackText": t.string().optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "text": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesCreate"] = chat.post(
        "v1/{parent}/messages",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "messageReplyOption": t.string().optional(),
                "threadKey": t.string().optional(),
                "messageId": t.string().optional(),
                "clientAssignedMessageId": t.string().optional(),
                "name": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "fallbackText": t.string().optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "text": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
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

    return Import(
        importer="chat", renames=renames, types=Box(types), functions=Box(functions)
    )
