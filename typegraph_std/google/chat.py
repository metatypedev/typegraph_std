from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_chat() -> Import:
    chat = HTTPRuntime("https://chat.googleapis.com/")

    renames = {
        "ErrorResponse": "_chat_1_ErrorResponse",
        "MatchedUrlIn": "_chat_2_MatchedUrlIn",
        "MatchedUrlOut": "_chat_3_MatchedUrlOut",
        "GoogleAppsCardV1SuggestionsIn": "_chat_4_GoogleAppsCardV1SuggestionsIn",
        "GoogleAppsCardV1SuggestionsOut": "_chat_5_GoogleAppsCardV1SuggestionsOut",
        "OnClickIn": "_chat_6_OnClickIn",
        "OnClickOut": "_chat_7_OnClickOut",
        "GoogleAppsCardV1SuggestionItemIn": "_chat_8_GoogleAppsCardV1SuggestionItemIn",
        "GoogleAppsCardV1SuggestionItemOut": "_chat_9_GoogleAppsCardV1SuggestionItemOut",
        "GoogleAppsCardV1SwitchControlIn": "_chat_10_GoogleAppsCardV1SwitchControlIn",
        "GoogleAppsCardV1SwitchControlOut": "_chat_11_GoogleAppsCardV1SwitchControlOut",
        "GoogleAppsCardV1DividerIn": "_chat_12_GoogleAppsCardV1DividerIn",
        "GoogleAppsCardV1DividerOut": "_chat_13_GoogleAppsCardV1DividerOut",
        "ThreadIn": "_chat_14_ThreadIn",
        "ThreadOut": "_chat_15_ThreadOut",
        "AnnotationIn": "_chat_16_AnnotationIn",
        "AnnotationOut": "_chat_17_AnnotationOut",
        "GoogleAppsCardV1OpenLinkIn": "_chat_18_GoogleAppsCardV1OpenLinkIn",
        "GoogleAppsCardV1OpenLinkOut": "_chat_19_GoogleAppsCardV1OpenLinkOut",
        "DateInputIn": "_chat_20_DateInputIn",
        "DateInputOut": "_chat_21_DateInputOut",
        "GoogleAppsCardV1ImageCropStyleIn": "_chat_22_GoogleAppsCardV1ImageCropStyleIn",
        "GoogleAppsCardV1ImageCropStyleOut": "_chat_23_GoogleAppsCardV1ImageCropStyleOut",
        "GoogleAppsCardV1ActionIn": "_chat_24_GoogleAppsCardV1ActionIn",
        "GoogleAppsCardV1ActionOut": "_chat_25_GoogleAppsCardV1ActionOut",
        "TextParagraphIn": "_chat_26_TextParagraphIn",
        "TextParagraphOut": "_chat_27_TextParagraphOut",
        "EmptyIn": "_chat_28_EmptyIn",
        "EmptyOut": "_chat_29_EmptyOut",
        "TimeInputIn": "_chat_30_TimeInputIn",
        "TimeInputOut": "_chat_31_TimeInputOut",
        "DialogIn": "_chat_32_DialogIn",
        "DialogOut": "_chat_33_DialogOut",
        "ColorIn": "_chat_34_ColorIn",
        "ColorOut": "_chat_35_ColorOut",
        "GoogleAppsCardV1SelectionItemIn": "_chat_36_GoogleAppsCardV1SelectionItemIn",
        "GoogleAppsCardV1SelectionItemOut": "_chat_37_GoogleAppsCardV1SelectionItemOut",
        "DeprecatedEventIn": "_chat_38_DeprecatedEventIn",
        "DeprecatedEventOut": "_chat_39_DeprecatedEventOut",
        "StringInputsIn": "_chat_40_StringInputsIn",
        "StringInputsOut": "_chat_41_StringInputsOut",
        "GoogleAppsCardV1GridItemIn": "_chat_42_GoogleAppsCardV1GridItemIn",
        "GoogleAppsCardV1GridItemOut": "_chat_43_GoogleAppsCardV1GridItemOut",
        "UserIn": "_chat_44_UserIn",
        "UserOut": "_chat_45_UserOut",
        "GoogleAppsCardV1SectionIn": "_chat_46_GoogleAppsCardV1SectionIn",
        "GoogleAppsCardV1SectionOut": "_chat_47_GoogleAppsCardV1SectionOut",
        "TextButtonIn": "_chat_48_TextButtonIn",
        "TextButtonOut": "_chat_49_TextButtonOut",
        "ButtonIn": "_chat_50_ButtonIn",
        "ButtonOut": "_chat_51_ButtonOut",
        "GoogleAppsCardV1CardHeaderIn": "_chat_52_GoogleAppsCardV1CardHeaderIn",
        "GoogleAppsCardV1CardHeaderOut": "_chat_53_GoogleAppsCardV1CardHeaderOut",
        "ListSpacesResponseIn": "_chat_54_ListSpacesResponseIn",
        "ListSpacesResponseOut": "_chat_55_ListSpacesResponseOut",
        "ImageIn": "_chat_56_ImageIn",
        "ImageOut": "_chat_57_ImageOut",
        "ListMembershipsResponseIn": "_chat_58_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_chat_59_ListMembershipsResponseOut",
        "MembershipIn": "_chat_60_MembershipIn",
        "MembershipOut": "_chat_61_MembershipOut",
        "CardHeaderIn": "_chat_62_CardHeaderIn",
        "CardHeaderOut": "_chat_63_CardHeaderOut",
        "GoogleAppsCardV1DecoratedTextIn": "_chat_64_GoogleAppsCardV1DecoratedTextIn",
        "GoogleAppsCardV1DecoratedTextOut": "_chat_65_GoogleAppsCardV1DecoratedTextOut",
        "AttachmentDataRefIn": "_chat_66_AttachmentDataRefIn",
        "AttachmentDataRefOut": "_chat_67_AttachmentDataRefOut",
        "GoogleAppsCardV1ButtonListIn": "_chat_68_GoogleAppsCardV1ButtonListIn",
        "GoogleAppsCardV1ButtonListOut": "_chat_69_GoogleAppsCardV1ButtonListOut",
        "WidgetMarkupIn": "_chat_70_WidgetMarkupIn",
        "WidgetMarkupOut": "_chat_71_WidgetMarkupOut",
        "GoogleAppsCardV1ButtonIn": "_chat_72_GoogleAppsCardV1ButtonIn",
        "GoogleAppsCardV1ButtonOut": "_chat_73_GoogleAppsCardV1ButtonOut",
        "GoogleAppsCardV1ImageIn": "_chat_74_GoogleAppsCardV1ImageIn",
        "GoogleAppsCardV1ImageOut": "_chat_75_GoogleAppsCardV1ImageOut",
        "CommonEventObjectIn": "_chat_76_CommonEventObjectIn",
        "CommonEventObjectOut": "_chat_77_CommonEventObjectOut",
        "MediaIn": "_chat_78_MediaIn",
        "MediaOut": "_chat_79_MediaOut",
        "GoogleAppsCardV1OnClickIn": "_chat_80_GoogleAppsCardV1OnClickIn",
        "GoogleAppsCardV1OnClickOut": "_chat_81_GoogleAppsCardV1OnClickOut",
        "SlashCommandMetadataIn": "_chat_82_SlashCommandMetadataIn",
        "SlashCommandMetadataOut": "_chat_83_SlashCommandMetadataOut",
        "CardActionIn": "_chat_84_CardActionIn",
        "CardActionOut": "_chat_85_CardActionOut",
        "CardIn": "_chat_86_CardIn",
        "CardOut": "_chat_87_CardOut",
        "TimeZoneIn": "_chat_88_TimeZoneIn",
        "TimeZoneOut": "_chat_89_TimeZoneOut",
        "GoogleAppsCardV1GridIn": "_chat_90_GoogleAppsCardV1GridIn",
        "GoogleAppsCardV1GridOut": "_chat_91_GoogleAppsCardV1GridOut",
        "SpaceIn": "_chat_92_SpaceIn",
        "SpaceOut": "_chat_93_SpaceOut",
        "ActionParameterIn": "_chat_94_ActionParameterIn",
        "ActionParameterOut": "_chat_95_ActionParameterOut",
        "SlashCommandIn": "_chat_96_SlashCommandIn",
        "SlashCommandOut": "_chat_97_SlashCommandOut",
        "GoogleAppsCardV1BorderStyleIn": "_chat_98_GoogleAppsCardV1BorderStyleIn",
        "GoogleAppsCardV1BorderStyleOut": "_chat_99_GoogleAppsCardV1BorderStyleOut",
        "ChatAppLogEntryIn": "_chat_100_ChatAppLogEntryIn",
        "ChatAppLogEntryOut": "_chat_101_ChatAppLogEntryOut",
        "DriveDataRefIn": "_chat_102_DriveDataRefIn",
        "DriveDataRefOut": "_chat_103_DriveDataRefOut",
        "ImageButtonIn": "_chat_104_ImageButtonIn",
        "ImageButtonOut": "_chat_105_ImageButtonOut",
        "GoogleAppsCardV1CardIn": "_chat_106_GoogleAppsCardV1CardIn",
        "GoogleAppsCardV1CardOut": "_chat_107_GoogleAppsCardV1CardOut",
        "GoogleAppsCardV1CardActionIn": "_chat_108_GoogleAppsCardV1CardActionIn",
        "GoogleAppsCardV1CardActionOut": "_chat_109_GoogleAppsCardV1CardActionOut",
        "DialogActionIn": "_chat_110_DialogActionIn",
        "DialogActionOut": "_chat_111_DialogActionOut",
        "GoogleAppsCardV1TextParagraphIn": "_chat_112_GoogleAppsCardV1TextParagraphIn",
        "GoogleAppsCardV1TextParagraphOut": "_chat_113_GoogleAppsCardV1TextParagraphOut",
        "GoogleAppsCardV1TextInputIn": "_chat_114_GoogleAppsCardV1TextInputIn",
        "GoogleAppsCardV1TextInputOut": "_chat_115_GoogleAppsCardV1TextInputOut",
        "CardWithIdIn": "_chat_116_CardWithIdIn",
        "CardWithIdOut": "_chat_117_CardWithIdOut",
        "AttachmentIn": "_chat_118_AttachmentIn",
        "AttachmentOut": "_chat_119_AttachmentOut",
        "ActionStatusIn": "_chat_120_ActionStatusIn",
        "ActionStatusOut": "_chat_121_ActionStatusOut",
        "KeyValueIn": "_chat_122_KeyValueIn",
        "KeyValueOut": "_chat_123_KeyValueOut",
        "GoogleAppsCardV1ImageComponentIn": "_chat_124_GoogleAppsCardV1ImageComponentIn",
        "GoogleAppsCardV1ImageComponentOut": "_chat_125_GoogleAppsCardV1ImageComponentOut",
        "StatusIn": "_chat_126_StatusIn",
        "StatusOut": "_chat_127_StatusOut",
        "GoogleAppsCardV1SelectionInputIn": "_chat_128_GoogleAppsCardV1SelectionInputIn",
        "GoogleAppsCardV1SelectionInputOut": "_chat_129_GoogleAppsCardV1SelectionInputOut",
        "SpaceDetailsIn": "_chat_130_SpaceDetailsIn",
        "SpaceDetailsOut": "_chat_131_SpaceDetailsOut",
        "ActionResponseIn": "_chat_132_ActionResponseIn",
        "ActionResponseOut": "_chat_133_ActionResponseOut",
        "UserMentionMetadataIn": "_chat_134_UserMentionMetadataIn",
        "UserMentionMetadataOut": "_chat_135_UserMentionMetadataOut",
        "GoogleAppsCardV1CardFixedFooterIn": "_chat_136_GoogleAppsCardV1CardFixedFooterIn",
        "GoogleAppsCardV1CardFixedFooterOut": "_chat_137_GoogleAppsCardV1CardFixedFooterOut",
        "OpenLinkIn": "_chat_138_OpenLinkIn",
        "OpenLinkOut": "_chat_139_OpenLinkOut",
        "SectionIn": "_chat_140_SectionIn",
        "SectionOut": "_chat_141_SectionOut",
        "GoogleAppsCardV1WidgetIn": "_chat_142_GoogleAppsCardV1WidgetIn",
        "GoogleAppsCardV1WidgetOut": "_chat_143_GoogleAppsCardV1WidgetOut",
        "FormActionIn": "_chat_144_FormActionIn",
        "FormActionOut": "_chat_145_FormActionOut",
        "DateTimeInputIn": "_chat_146_DateTimeInputIn",
        "DateTimeInputOut": "_chat_147_DateTimeInputOut",
        "GoogleAppsCardV1IconIn": "_chat_148_GoogleAppsCardV1IconIn",
        "GoogleAppsCardV1IconOut": "_chat_149_GoogleAppsCardV1IconOut",
        "MessageIn": "_chat_150_MessageIn",
        "MessageOut": "_chat_151_MessageOut",
        "GoogleAppsCardV1DateTimePickerIn": "_chat_152_GoogleAppsCardV1DateTimePickerIn",
        "GoogleAppsCardV1DateTimePickerOut": "_chat_153_GoogleAppsCardV1DateTimePickerOut",
        "InputsIn": "_chat_154_InputsIn",
        "InputsOut": "_chat_155_InputsOut",
        "GoogleAppsCardV1ActionParameterIn": "_chat_156_GoogleAppsCardV1ActionParameterIn",
        "GoogleAppsCardV1ActionParameterOut": "_chat_157_GoogleAppsCardV1ActionParameterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MatchedUrlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatchedUrlIn"]
    )
    types["MatchedUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchedUrlOut"])
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
    types["OnClickIn"] = t.struct(
        {
            "action": t.proxy(renames["FormActionIn"]).optional(),
            "openLink": t.proxy(renames["OpenLinkIn"]).optional(),
        }
    ).named(renames["OnClickIn"])
    types["OnClickOut"] = t.struct(
        {
            "action": t.proxy(renames["FormActionOut"]).optional(),
            "openLink": t.proxy(renames["OpenLinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OnClickOut"])
    types["GoogleAppsCardV1SuggestionItemIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1SuggestionItemIn"])
    types["GoogleAppsCardV1SuggestionItemOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SuggestionItemOut"])
    types["GoogleAppsCardV1SwitchControlIn"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "value": t.string().optional(),
            "controlType": t.string().optional(),
            "selected": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlIn"])
    types["GoogleAppsCardV1SwitchControlOut"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "value": t.string().optional(),
            "controlType": t.string().optional(),
            "selected": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlOut"])
    types["GoogleAppsCardV1DividerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsCardV1DividerIn"]
    )
    types["GoogleAppsCardV1DividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCardV1DividerOut"])
    types["ThreadIn"] = t.struct(
        {"threadKey": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ThreadIn"])
    types["ThreadOut"] = t.struct(
        {
            "threadKey": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThreadOut"])
    types["AnnotationIn"] = t.struct(
        {
            "slashCommand": t.proxy(renames["SlashCommandMetadataIn"]).optional(),
            "userMention": t.proxy(renames["UserMentionMetadataIn"]).optional(),
            "length": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "slashCommand": t.proxy(renames["SlashCommandMetadataOut"]).optional(),
            "userMention": t.proxy(renames["UserMentionMetadataOut"]).optional(),
            "length": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["GoogleAppsCardV1OpenLinkIn"] = t.struct(
        {
            "url": t.string().optional(),
            "openAs": t.string().optional(),
            "onClose": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1OpenLinkIn"])
    types["GoogleAppsCardV1OpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "openAs": t.string().optional(),
            "onClose": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OpenLinkOut"])
    types["DateInputIn"] = t.struct({"msSinceEpoch": t.string().optional()}).named(
        renames["DateInputIn"]
    )
    types["DateInputOut"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateInputOut"])
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
    types["GoogleAppsCardV1ActionIn"] = t.struct(
        {
            "persistValues": t.boolean().optional(),
            "loadIndicator": t.string().optional(),
            "interaction": t.string().optional(),
            "function": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterIn"])
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionIn"])
    types["GoogleAppsCardV1ActionOut"] = t.struct(
        {
            "persistValues": t.boolean().optional(),
            "loadIndicator": t.string().optional(),
            "interaction": t.string().optional(),
            "function": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionOut"])
    types["TextParagraphIn"] = t.struct({"text": t.string()}).named(
        renames["TextParagraphIn"]
    )
    types["TextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextParagraphOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["DialogIn"] = t.struct(
        {"body": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional()}
    ).named(renames["DialogIn"])
    types["DialogOut"] = t.struct(
        {
            "body": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DialogOut"])
    types["ColorIn"] = t.struct(
        {
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "green": t.number().optional(),
            "alpha": t.number().optional(),
            "blue": t.number().optional(),
            "red": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["GoogleAppsCardV1SelectionItemIn"] = t.struct(
        {
            "value": t.string().optional(),
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemIn"])
    types["GoogleAppsCardV1SelectionItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "selected": t.boolean().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemOut"])
    types["DeprecatedEventIn"] = t.struct(
        {
            "isDialogEvent": t.boolean().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "token": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectIn"]).optional(),
            "threadKey": t.string().optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "dialogEventType": t.string().optional(),
            "eventTime": t.string().optional(),
            "action": t.proxy(renames["FormActionIn"]).optional(),
            "type": t.string().optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
        }
    ).named(renames["DeprecatedEventIn"])
    types["DeprecatedEventOut"] = t.struct(
        {
            "isDialogEvent": t.boolean().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "token": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectOut"]).optional(),
            "threadKey": t.string().optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "dialogEventType": t.string().optional(),
            "eventTime": t.string().optional(),
            "action": t.proxy(renames["FormActionOut"]).optional(),
            "type": t.string().optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeprecatedEventOut"])
    types["StringInputsIn"] = t.struct({"value": t.array(t.string()).optional()}).named(
        renames["StringInputsIn"]
    )
    types["StringInputsOut"] = t.struct(
        {
            "value": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringInputsOut"])
    types["GoogleAppsCardV1GridItemIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "layout": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemIn"])
    types["GoogleAppsCardV1GridItemOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "layout": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemOut"])
    types["UserIn"] = t.struct(
        {
            "type": t.string().optional(),
            "domainId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "type": t.string().optional(),
            "domainId": t.string().optional(),
            "name": t.string().optional(),
            "isAnonymous": t.boolean().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["GoogleAppsCardV1SectionIn"] = t.struct(
        {
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "header": t.string().optional(),
            "widgets": t.array(t.proxy(renames["GoogleAppsCardV1WidgetIn"])).optional(),
            "collapsible": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCardV1SectionIn"])
    types["GoogleAppsCardV1SectionOut"] = t.struct(
        {
            "uncollapsibleWidgetsCount": t.integer().optional(),
            "header": t.string().optional(),
            "widgets": t.array(
                t.proxy(renames["GoogleAppsCardV1WidgetOut"])
            ).optional(),
            "collapsible": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SectionOut"])
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
    types["GoogleAppsCardV1CardHeaderIn"] = t.struct(
        {
            "imageAltText": t.string().optional(),
            "title": t.string(),
            "subtitle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "imageType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderIn"])
    types["GoogleAppsCardV1CardHeaderOut"] = t.struct(
        {
            "imageAltText": t.string().optional(),
            "title": t.string(),
            "subtitle": t.string().optional(),
            "imageUrl": t.string().optional(),
            "imageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderOut"])
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
    types["MembershipIn"] = t.struct(
        {"name": t.string().optional(), "member": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "member": t.proxy(renames["UserOut"]).optional(),
            "createTime": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["CardHeaderIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
        }
    ).named(renames["CardHeaderIn"])
    types["CardHeaderOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageStyle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardHeaderOut"])
    types["GoogleAppsCardV1DecoratedTextIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "topLabel": t.string().optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonIn"]).optional(),
            "wrapText": t.boolean().optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlIn"]
            ).optional(),
            "text": t.string(),
            "bottomLabel": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextIn"])
    types["GoogleAppsCardV1DecoratedTextOut"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "topLabel": t.string().optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonOut"]).optional(),
            "wrapText": t.boolean().optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlOut"]
            ).optional(),
            "text": t.string(),
            "bottomLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextOut"])
    types["AttachmentDataRefIn"] = t.struct(
        {"resourceName": t.string().optional()}
    ).named(renames["AttachmentDataRefIn"])
    types["AttachmentDataRefOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentDataRefOut"])
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
    types["GoogleAppsCardV1ButtonIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]),
            "text": t.string().optional(),
            "altText": t.string().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonIn"])
    types["GoogleAppsCardV1ButtonOut"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]),
            "text": t.string().optional(),
            "altText": t.string().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonOut"])
    types["GoogleAppsCardV1ImageIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageIn"])
    types["GoogleAppsCardV1ImageOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageOut"])
    types["CommonEventObjectIn"] = t.struct(
        {
            "invokedFunction": t.string().optional(),
            "hostApp": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "platform": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
            "userLocale": t.string().optional(),
        }
    ).named(renames["CommonEventObjectIn"])
    types["CommonEventObjectOut"] = t.struct(
        {
            "invokedFunction": t.string().optional(),
            "hostApp": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "platform": t.string().optional(),
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
            "userLocale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonEventObjectOut"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["GoogleAppsCardV1OnClickIn"] = t.struct(
        {
            "action": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkIn"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickIn"])
    types["GoogleAppsCardV1OnClickOut"] = t.struct(
        {
            "action": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkOut"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickOut"])
    types["SlashCommandMetadataIn"] = t.struct(
        {
            "triggersDialog": t.boolean().optional(),
            "commandId": t.string().optional(),
            "type": t.string().optional(),
            "commandName": t.string().optional(),
            "bot": t.proxy(renames["UserIn"]).optional(),
        }
    ).named(renames["SlashCommandMetadataIn"])
    types["SlashCommandMetadataOut"] = t.struct(
        {
            "triggersDialog": t.boolean().optional(),
            "commandId": t.string().optional(),
            "type": t.string().optional(),
            "commandName": t.string().optional(),
            "bot": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandMetadataOut"])
    types["CardActionIn"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "actionLabel": t.string().optional(),
        }
    ).named(renames["CardActionIn"])
    types["CardActionOut"] = t.struct(
        {
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "actionLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardActionOut"])
    types["CardIn"] = t.struct(
        {
            "header": t.proxy(renames["CardHeaderIn"]).optional(),
            "sections": t.array(t.proxy(renames["SectionIn"])).optional(),
            "name": t.string().optional(),
            "cardActions": t.array(t.proxy(renames["CardActionIn"])).optional(),
        }
    ).named(renames["CardIn"])
    types["CardOut"] = t.struct(
        {
            "header": t.proxy(renames["CardHeaderOut"]).optional(),
            "sections": t.array(t.proxy(renames["SectionOut"])).optional(),
            "name": t.string().optional(),
            "cardActions": t.array(t.proxy(renames["CardActionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardOut"])
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
    types["GoogleAppsCardV1GridIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GoogleAppsCardV1GridItemIn"])).optional(),
            "columnCount": t.integer().optional(),
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1GridIn"])
    types["GoogleAppsCardV1GridOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1GridItemOut"])
            ).optional(),
            "columnCount": t.integer().optional(),
            "borderStyle": t.proxy(
                renames["GoogleAppsCardV1BorderStyleOut"]
            ).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridOut"])
    types["SpaceIn"] = t.struct(
        {
            "singleUserBotDm": t.boolean().optional(),
            "spaceDetails": t.proxy(renames["SpaceDetailsIn"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SpaceIn"])
    types["SpaceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "singleUserBotDm": t.boolean().optional(),
            "threaded": t.boolean().optional(),
            "spaceDetails": t.proxy(renames["SpaceDetailsOut"]).optional(),
            "spaceThreadingState": t.string().optional(),
            "displayName": t.string().optional(),
            "adminInstalled": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceOut"])
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
    types["SlashCommandIn"] = t.struct({"commandId": t.string().optional()}).named(
        renames["SlashCommandIn"]
    )
    types["SlashCommandOut"] = t.struct(
        {
            "commandId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandOut"])
    types["GoogleAppsCardV1BorderStyleIn"] = t.struct(
        {
            "type": t.string().optional(),
            "cornerRadius": t.integer().optional(),
            "strokeColor": t.proxy(renames["ColorIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1BorderStyleIn"])
    types["GoogleAppsCardV1BorderStyleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "cornerRadius": t.integer().optional(),
            "strokeColor": t.proxy(renames["ColorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1BorderStyleOut"])
    types["ChatAppLogEntryIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "deployment": t.string().optional(),
            "deploymentFunction": t.string().optional(),
        }
    ).named(renames["ChatAppLogEntryIn"])
    types["ChatAppLogEntryOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "deployment": t.string().optional(),
            "deploymentFunction": t.string().optional(),
        }
    ).named(renames["ChatAppLogEntryOut"])
    types["DriveDataRefIn"] = t.struct({"driveFileId": t.string().optional()}).named(
        renames["DriveDataRefIn"]
    )
    types["DriveDataRefOut"] = t.struct(
        {
            "driveFileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveDataRefOut"])
    types["ImageButtonIn"] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "name": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "icon": t.string().optional(),
        }
    ).named(renames["ImageButtonIn"])
    types["ImageButtonOut"] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "name": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "icon": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageButtonOut"])
    types["GoogleAppsCardV1CardIn"] = t.struct(
        {
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderIn"]
            ).optional(),
            "displayStyle": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionIn"])
            ).optional(),
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterIn"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionIn"])
            ).optional(),
            "name": t.string().optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardIn"])
    types["GoogleAppsCardV1CardOut"] = t.struct(
        {
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderOut"]
            ).optional(),
            "displayStyle": t.string().optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionOut"])
            ).optional(),
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterOut"]
            ).optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionOut"])
            ).optional(),
            "name": t.string().optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardOut"])
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
    types["DialogActionIn"] = t.struct(
        {
            "actionStatus": t.proxy(renames["ActionStatusIn"]).optional(),
            "dialog": t.proxy(renames["DialogIn"]).optional(),
        }
    ).named(renames["DialogActionIn"])
    types["DialogActionOut"] = t.struct(
        {
            "actionStatus": t.proxy(renames["ActionStatusOut"]).optional(),
            "dialog": t.proxy(renames["DialogOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DialogActionOut"])
    types["GoogleAppsCardV1TextParagraphIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1TextParagraphIn"])
    types["GoogleAppsCardV1TextParagraphOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextParagraphOut"])
    types["GoogleAppsCardV1TextInputIn"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "value": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsIn"]
            ).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
            "hintText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputIn"])
    types["GoogleAppsCardV1TextInputOut"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "value": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsOut"]
            ).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "hintText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputOut"])
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
    types["AttachmentIn"] = t.struct(
        {
            "contentName": t.string().optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefIn"]).optional(),
            "name": t.string().optional(),
            "source": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefIn"]).optional(),
            "contentType": t.string().optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "contentName": t.string().optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefOut"]).optional(),
            "downloadUri": t.string().optional(),
            "thumbnailUri": t.string().optional(),
            "name": t.string().optional(),
            "source": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefOut"]).optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
    types["ActionStatusIn"] = t.struct(
        {
            "userFacingMessage": t.string().optional(),
            "statusCode": t.string().optional(),
        }
    ).named(renames["ActionStatusIn"])
    types["ActionStatusOut"] = t.struct(
        {
            "userFacingMessage": t.string().optional(),
            "statusCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionStatusOut"])
    types["KeyValueIn"] = t.struct(
        {
            "topLabel": t.string().optional(),
            "content": t.string().optional(),
            "icon": t.string().optional(),
            "button": t.proxy(renames["ButtonIn"]).optional(),
            "contentMultiline": t.boolean().optional(),
            "bottomLabel": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
        }
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "topLabel": t.string().optional(),
            "content": t.string().optional(),
            "icon": t.string().optional(),
            "button": t.proxy(renames["ButtonOut"]).optional(),
            "contentMultiline": t.boolean().optional(),
            "bottomLabel": t.string().optional(),
            "iconUrl": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["GoogleAppsCardV1ImageComponentIn"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "cropStyle": t.proxy(
                renames["GoogleAppsCardV1ImageCropStyleIn"]
            ).optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageComponentIn"])
    types["GoogleAppsCardV1ImageComponentOut"] = t.struct(
        {
            "imageUri": t.string().optional(),
            "borderStyle": t.proxy(
                renames["GoogleAppsCardV1BorderStyleOut"]
            ).optional(),
            "cropStyle": t.proxy(
                renames["GoogleAppsCardV1ImageCropStyleOut"]
            ).optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageComponentOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleAppsCardV1SelectionInputIn"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemIn"])
            ).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputIn"])
    types["GoogleAppsCardV1SelectionInputOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemOut"])
            ).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputOut"])
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
    types["ActionResponseIn"] = t.struct(
        {
            "url": t.string().optional(),
            "type": t.string().optional(),
            "dialogAction": t.proxy(renames["DialogActionIn"]).optional(),
        }
    ).named(renames["ActionResponseIn"])
    types["ActionResponseOut"] = t.struct(
        {
            "url": t.string().optional(),
            "type": t.string().optional(),
            "dialogAction": t.proxy(renames["DialogActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionResponseOut"])
    types["UserMentionMetadataIn"] = t.struct(
        {"type": t.string().optional(), "user": t.proxy(renames["UserIn"]).optional()}
    ).named(renames["UserMentionMetadataIn"])
    types["UserMentionMetadataOut"] = t.struct(
        {
            "type": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserMentionMetadataOut"])
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
    types["OpenLinkIn"] = t.struct({"url": t.string().optional()}).named(
        renames["OpenLinkIn"]
    )
    types["OpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenLinkOut"])
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
    types["GoogleAppsCardV1WidgetIn"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageIn"]).optional(),
            "grid": t.proxy(renames["GoogleAppsCardV1GridIn"]).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerIn"]).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextIn"]
            ).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListIn"]).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputIn"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerIn"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphIn"]
            ).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetIn"])
    types["GoogleAppsCardV1WidgetOut"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageOut"]).optional(),
            "grid": t.proxy(renames["GoogleAppsCardV1GridOut"]).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerOut"]).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextOut"]
            ).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListOut"]).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputOut"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerOut"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphOut"]
            ).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetOut"])
    types["FormActionIn"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ActionParameterIn"])).optional(),
            "actionMethodName": t.string().optional(),
        }
    ).named(renames["FormActionIn"])
    types["FormActionOut"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["ActionParameterOut"])).optional(),
            "actionMethodName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormActionOut"])
    types["DateTimeInputIn"] = t.struct(
        {
            "hasDate": t.boolean().optional(),
            "hasTime": t.boolean().optional(),
            "msSinceEpoch": t.string().optional(),
        }
    ).named(renames["DateTimeInputIn"])
    types["DateTimeInputOut"] = t.struct(
        {
            "hasDate": t.boolean().optional(),
            "hasTime": t.boolean().optional(),
            "msSinceEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateTimeInputOut"])
    types["GoogleAppsCardV1IconIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1IconIn"])
    types["GoogleAppsCardV1IconOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
            "imageType": t.string().optional(),
            "iconUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1IconOut"])
    types["MessageIn"] = t.struct(
        {
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "thread": t.proxy(renames["ThreadIn"]).optional(),
            "name": t.string().optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
            "text": t.string().optional(),
            "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "clientAssignedMessageId": t.string().optional(),
            "fallbackText": t.string().optional(),
            "cards": t.array(t.proxy(renames["CardIn"])).optional(),
            "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "sender": t.proxy(renames["UserOut"]).optional(),
            "threadReply": t.boolean().optional(),
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "matchedUrl": t.proxy(renames["MatchedUrlOut"]).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "slashCommand": t.proxy(renames["SlashCommandOut"]).optional(),
            "thread": t.proxy(renames["ThreadOut"]).optional(),
            "createTime": t.string().optional(),
            "argumentText": t.string().optional(),
            "name": t.string().optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdOut"])).optional(),
            "text": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "attachment": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "clientAssignedMessageId": t.string().optional(),
            "fallbackText": t.string().optional(),
            "cards": t.array(t.proxy(renames["CardOut"])).optional(),
            "actionResponse": t.proxy(renames["ActionResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
    types["GoogleAppsCardV1DateTimePickerIn"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerIn"])
    types["GoogleAppsCardV1DateTimePickerOut"] = t.struct(
        {
            "valueMsEpoch": t.string().optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerOut"])
    types["InputsIn"] = t.struct(
        {
            "stringInputs": t.proxy(renames["StringInputsIn"]).optional(),
            "timeInput": t.proxy(renames["TimeInputIn"]).optional(),
            "dateInput": t.proxy(renames["DateInputIn"]).optional(),
            "dateTimeInput": t.proxy(renames["DateTimeInputIn"]).optional(),
        }
    ).named(renames["InputsIn"])
    types["InputsOut"] = t.struct(
        {
            "stringInputs": t.proxy(renames["StringInputsOut"]).optional(),
            "timeInput": t.proxy(renames["TimeInputOut"]).optional(),
            "dateInput": t.proxy(renames["DateInputOut"]).optional(),
            "dateTimeInput": t.proxy(renames["DateTimeInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputsOut"])
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

    functions = {}
    functions["spacesGet"] = chat.get(
        "v1/spaces",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
    functions["spacesMessagesCreate"] = chat.put(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "text": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesDelete"] = chat.put(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "text": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesGet"] = chat.put(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "text": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesPatch"] = chat.put(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "text": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesUpdate"] = chat.put(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "text": t.string().optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
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
    functions["mediaDownload"] = chat.get(
        "v1/media/{resourceName}",
        t.struct(
            {"resourceName": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["MediaOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="chat", renames=renames, types=Box(types), functions=Box(functions)
    )
