from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_chat():
    chat = HTTPRuntime("https://chat.googleapis.com/")

    renames = {
        "ErrorResponse": "_chat_1_ErrorResponse",
        "ButtonIn": "_chat_2_ButtonIn",
        "ButtonOut": "_chat_3_ButtonOut",
        "GoogleAppsCardV1DecoratedTextIn": "_chat_4_GoogleAppsCardV1DecoratedTextIn",
        "GoogleAppsCardV1DecoratedTextOut": "_chat_5_GoogleAppsCardV1DecoratedTextOut",
        "UploadAttachmentRequestIn": "_chat_6_UploadAttachmentRequestIn",
        "UploadAttachmentRequestOut": "_chat_7_UploadAttachmentRequestOut",
        "GoogleAppsCardV1BorderStyleIn": "_chat_8_GoogleAppsCardV1BorderStyleIn",
        "GoogleAppsCardV1BorderStyleOut": "_chat_9_GoogleAppsCardV1BorderStyleOut",
        "GoogleAppsCardV1TextInputIn": "_chat_10_GoogleAppsCardV1TextInputIn",
        "GoogleAppsCardV1TextInputOut": "_chat_11_GoogleAppsCardV1TextInputOut",
        "MembershipIn": "_chat_12_MembershipIn",
        "MembershipOut": "_chat_13_MembershipOut",
        "AttachmentIn": "_chat_14_AttachmentIn",
        "AttachmentOut": "_chat_15_AttachmentOut",
        "GoogleAppsCardV1SuggestionsIn": "_chat_16_GoogleAppsCardV1SuggestionsIn",
        "GoogleAppsCardV1SuggestionsOut": "_chat_17_GoogleAppsCardV1SuggestionsOut",
        "CardHeaderIn": "_chat_18_CardHeaderIn",
        "CardHeaderOut": "_chat_19_CardHeaderOut",
        "TextParagraphIn": "_chat_20_TextParagraphIn",
        "TextParagraphOut": "_chat_21_TextParagraphOut",
        "SetUpSpaceRequestIn": "_chat_22_SetUpSpaceRequestIn",
        "SetUpSpaceRequestOut": "_chat_23_SetUpSpaceRequestOut",
        "CardWithIdIn": "_chat_24_CardWithIdIn",
        "CardWithIdOut": "_chat_25_CardWithIdOut",
        "GoogleAppsCardV1GridItemIn": "_chat_26_GoogleAppsCardV1GridItemIn",
        "GoogleAppsCardV1GridItemOut": "_chat_27_GoogleAppsCardV1GridItemOut",
        "AttachmentDataRefIn": "_chat_28_AttachmentDataRefIn",
        "AttachmentDataRefOut": "_chat_29_AttachmentDataRefOut",
        "MatchedUrlIn": "_chat_30_MatchedUrlIn",
        "MatchedUrlOut": "_chat_31_MatchedUrlOut",
        "GoogleAppsCardV1OpenLinkIn": "_chat_32_GoogleAppsCardV1OpenLinkIn",
        "GoogleAppsCardV1OpenLinkOut": "_chat_33_GoogleAppsCardV1OpenLinkOut",
        "SpaceIn": "_chat_34_SpaceIn",
        "SpaceOut": "_chat_35_SpaceOut",
        "GoogleAppsCardV1ImageComponentIn": "_chat_36_GoogleAppsCardV1ImageComponentIn",
        "GoogleAppsCardV1ImageComponentOut": "_chat_37_GoogleAppsCardV1ImageComponentOut",
        "ImageIn": "_chat_38_ImageIn",
        "ImageOut": "_chat_39_ImageOut",
        "InputsIn": "_chat_40_InputsIn",
        "InputsOut": "_chat_41_InputsOut",
        "UploadAttachmentResponseIn": "_chat_42_UploadAttachmentResponseIn",
        "UploadAttachmentResponseOut": "_chat_43_UploadAttachmentResponseOut",
        "GoogleAppsCardV1WidgetsIn": "_chat_44_GoogleAppsCardV1WidgetsIn",
        "GoogleAppsCardV1WidgetsOut": "_chat_45_GoogleAppsCardV1WidgetsOut",
        "OpenLinkIn": "_chat_46_OpenLinkIn",
        "OpenLinkOut": "_chat_47_OpenLinkOut",
        "SpaceDetailsIn": "_chat_48_SpaceDetailsIn",
        "SpaceDetailsOut": "_chat_49_SpaceDetailsOut",
        "DialogActionIn": "_chat_50_DialogActionIn",
        "DialogActionOut": "_chat_51_DialogActionOut",
        "GoogleAppsCardV1WidgetIn": "_chat_52_GoogleAppsCardV1WidgetIn",
        "GoogleAppsCardV1WidgetOut": "_chat_53_GoogleAppsCardV1WidgetOut",
        "GoogleAppsCardV1ImageCropStyleIn": "_chat_54_GoogleAppsCardV1ImageCropStyleIn",
        "GoogleAppsCardV1ImageCropStyleOut": "_chat_55_GoogleAppsCardV1ImageCropStyleOut",
        "ListMembershipsResponseIn": "_chat_56_ListMembershipsResponseIn",
        "ListMembershipsResponseOut": "_chat_57_ListMembershipsResponseOut",
        "StringInputsIn": "_chat_58_StringInputsIn",
        "StringInputsOut": "_chat_59_StringInputsOut",
        "GoogleAppsCardV1CardActionIn": "_chat_60_GoogleAppsCardV1CardActionIn",
        "GoogleAppsCardV1CardActionOut": "_chat_61_GoogleAppsCardV1CardActionOut",
        "GoogleAppsCardV1OnClickIn": "_chat_62_GoogleAppsCardV1OnClickIn",
        "GoogleAppsCardV1OnClickOut": "_chat_63_GoogleAppsCardV1OnClickOut",
        "DateInputIn": "_chat_64_DateInputIn",
        "DateInputOut": "_chat_65_DateInputOut",
        "GoogleAppsCardV1TextParagraphIn": "_chat_66_GoogleAppsCardV1TextParagraphIn",
        "GoogleAppsCardV1TextParagraphOut": "_chat_67_GoogleAppsCardV1TextParagraphOut",
        "EmptyIn": "_chat_68_EmptyIn",
        "EmptyOut": "_chat_69_EmptyOut",
        "ImageButtonIn": "_chat_70_ImageButtonIn",
        "ImageButtonOut": "_chat_71_ImageButtonOut",
        "EmojiReactionSummaryIn": "_chat_72_EmojiReactionSummaryIn",
        "EmojiReactionSummaryOut": "_chat_73_EmojiReactionSummaryOut",
        "TimeZoneIn": "_chat_74_TimeZoneIn",
        "TimeZoneOut": "_chat_75_TimeZoneOut",
        "DialogIn": "_chat_76_DialogIn",
        "DialogOut": "_chat_77_DialogOut",
        "AttachedGifIn": "_chat_78_AttachedGifIn",
        "AttachedGifOut": "_chat_79_AttachedGifOut",
        "DeletionMetadataIn": "_chat_80_DeletionMetadataIn",
        "DeletionMetadataOut": "_chat_81_DeletionMetadataOut",
        "UserIn": "_chat_82_UserIn",
        "UserOut": "_chat_83_UserOut",
        "ReactionIn": "_chat_84_ReactionIn",
        "ReactionOut": "_chat_85_ReactionOut",
        "TextButtonIn": "_chat_86_TextButtonIn",
        "TextButtonOut": "_chat_87_TextButtonOut",
        "GoogleAppsCardV1GridIn": "_chat_88_GoogleAppsCardV1GridIn",
        "GoogleAppsCardV1GridOut": "_chat_89_GoogleAppsCardV1GridOut",
        "MediaIn": "_chat_90_MediaIn",
        "MediaOut": "_chat_91_MediaOut",
        "CustomEmojiIn": "_chat_92_CustomEmojiIn",
        "CustomEmojiOut": "_chat_93_CustomEmojiOut",
        "ActionResponseIn": "_chat_94_ActionResponseIn",
        "ActionResponseOut": "_chat_95_ActionResponseOut",
        "MessageIn": "_chat_96_MessageIn",
        "MessageOut": "_chat_97_MessageOut",
        "ThreadIn": "_chat_98_ThreadIn",
        "ThreadOut": "_chat_99_ThreadOut",
        "GoogleAppsCardV1DividerIn": "_chat_100_GoogleAppsCardV1DividerIn",
        "GoogleAppsCardV1DividerOut": "_chat_101_GoogleAppsCardV1DividerOut",
        "DeprecatedEventIn": "_chat_102_DeprecatedEventIn",
        "DeprecatedEventOut": "_chat_103_DeprecatedEventOut",
        "GoogleAppsCardV1DateTimePickerIn": "_chat_104_GoogleAppsCardV1DateTimePickerIn",
        "GoogleAppsCardV1DateTimePickerOut": "_chat_105_GoogleAppsCardV1DateTimePickerOut",
        "ColorIn": "_chat_106_ColorIn",
        "ColorOut": "_chat_107_ColorOut",
        "GoogleAppsCardV1ColumnIn": "_chat_108_GoogleAppsCardV1ColumnIn",
        "GoogleAppsCardV1ColumnOut": "_chat_109_GoogleAppsCardV1ColumnOut",
        "ActionStatusIn": "_chat_110_ActionStatusIn",
        "ActionStatusOut": "_chat_111_ActionStatusOut",
        "GoogleAppsCardV1CardHeaderIn": "_chat_112_GoogleAppsCardV1CardHeaderIn",
        "GoogleAppsCardV1CardHeaderOut": "_chat_113_GoogleAppsCardV1CardHeaderOut",
        "DateTimeInputIn": "_chat_114_DateTimeInputIn",
        "DateTimeInputOut": "_chat_115_DateTimeInputOut",
        "GoogleAppsCardV1IconIn": "_chat_116_GoogleAppsCardV1IconIn",
        "GoogleAppsCardV1IconOut": "_chat_117_GoogleAppsCardV1IconOut",
        "GoogleAppsCardV1ButtonListIn": "_chat_118_GoogleAppsCardV1ButtonListIn",
        "GoogleAppsCardV1ButtonListOut": "_chat_119_GoogleAppsCardV1ButtonListOut",
        "ListSpacesResponseIn": "_chat_120_ListSpacesResponseIn",
        "ListSpacesResponseOut": "_chat_121_ListSpacesResponseOut",
        "UserMentionMetadataIn": "_chat_122_UserMentionMetadataIn",
        "UserMentionMetadataOut": "_chat_123_UserMentionMetadataOut",
        "KeyValueIn": "_chat_124_KeyValueIn",
        "KeyValueOut": "_chat_125_KeyValueOut",
        "GoogleAppsCardV1ColumnsIn": "_chat_126_GoogleAppsCardV1ColumnsIn",
        "GoogleAppsCardV1ColumnsOut": "_chat_127_GoogleAppsCardV1ColumnsOut",
        "GoogleAppsCardV1ImageIn": "_chat_128_GoogleAppsCardV1ImageIn",
        "GoogleAppsCardV1ImageOut": "_chat_129_GoogleAppsCardV1ImageOut",
        "GoogleAppsCardV1SelectionInputIn": "_chat_130_GoogleAppsCardV1SelectionInputIn",
        "GoogleAppsCardV1SelectionInputOut": "_chat_131_GoogleAppsCardV1SelectionInputOut",
        "CardIn": "_chat_132_CardIn",
        "CardOut": "_chat_133_CardOut",
        "CardActionIn": "_chat_134_CardActionIn",
        "CardActionOut": "_chat_135_CardActionOut",
        "GoogleAppsCardV1SelectionItemIn": "_chat_136_GoogleAppsCardV1SelectionItemIn",
        "GoogleAppsCardV1SelectionItemOut": "_chat_137_GoogleAppsCardV1SelectionItemOut",
        "FormActionIn": "_chat_138_FormActionIn",
        "FormActionOut": "_chat_139_FormActionOut",
        "ListMessagesResponseIn": "_chat_140_ListMessagesResponseIn",
        "ListMessagesResponseOut": "_chat_141_ListMessagesResponseOut",
        "GoogleAppsCardV1ActionIn": "_chat_142_GoogleAppsCardV1ActionIn",
        "GoogleAppsCardV1ActionOut": "_chat_143_GoogleAppsCardV1ActionOut",
        "GoogleAppsCardV1SwitchControlIn": "_chat_144_GoogleAppsCardV1SwitchControlIn",
        "GoogleAppsCardV1SwitchControlOut": "_chat_145_GoogleAppsCardV1SwitchControlOut",
        "CommonEventObjectIn": "_chat_146_CommonEventObjectIn",
        "CommonEventObjectOut": "_chat_147_CommonEventObjectOut",
        "GoogleAppsCardV1CardIn": "_chat_148_GoogleAppsCardV1CardIn",
        "GoogleAppsCardV1CardOut": "_chat_149_GoogleAppsCardV1CardOut",
        "DriveDataRefIn": "_chat_150_DriveDataRefIn",
        "DriveDataRefOut": "_chat_151_DriveDataRefOut",
        "GoogleAppsCardV1CardFixedFooterIn": "_chat_152_GoogleAppsCardV1CardFixedFooterIn",
        "GoogleAppsCardV1CardFixedFooterOut": "_chat_153_GoogleAppsCardV1CardFixedFooterOut",
        "ChatAppLogEntryIn": "_chat_154_ChatAppLogEntryIn",
        "ChatAppLogEntryOut": "_chat_155_ChatAppLogEntryOut",
        "WidgetMarkupIn": "_chat_156_WidgetMarkupIn",
        "WidgetMarkupOut": "_chat_157_WidgetMarkupOut",
        "GoogleAppsCardV1SuggestionItemIn": "_chat_158_GoogleAppsCardV1SuggestionItemIn",
        "GoogleAppsCardV1SuggestionItemOut": "_chat_159_GoogleAppsCardV1SuggestionItemOut",
        "ListReactionsResponseIn": "_chat_160_ListReactionsResponseIn",
        "ListReactionsResponseOut": "_chat_161_ListReactionsResponseOut",
        "StatusIn": "_chat_162_StatusIn",
        "StatusOut": "_chat_163_StatusOut",
        "OnClickIn": "_chat_164_OnClickIn",
        "OnClickOut": "_chat_165_OnClickOut",
        "GoogleAppsCardV1SectionIn": "_chat_166_GoogleAppsCardV1SectionIn",
        "GoogleAppsCardV1SectionOut": "_chat_167_GoogleAppsCardV1SectionOut",
        "GoogleAppsCardV1ActionParameterIn": "_chat_168_GoogleAppsCardV1ActionParameterIn",
        "GoogleAppsCardV1ActionParameterOut": "_chat_169_GoogleAppsCardV1ActionParameterOut",
        "SlashCommandMetadataIn": "_chat_170_SlashCommandMetadataIn",
        "SlashCommandMetadataOut": "_chat_171_SlashCommandMetadataOut",
        "EmojiIn": "_chat_172_EmojiIn",
        "EmojiOut": "_chat_173_EmojiOut",
        "ActionParameterIn": "_chat_174_ActionParameterIn",
        "ActionParameterOut": "_chat_175_ActionParameterOut",
        "TimeInputIn": "_chat_176_TimeInputIn",
        "TimeInputOut": "_chat_177_TimeInputOut",
        "GoogleAppsCardV1ButtonIn": "_chat_178_GoogleAppsCardV1ButtonIn",
        "GoogleAppsCardV1ButtonOut": "_chat_179_GoogleAppsCardV1ButtonOut",
        "AnnotationIn": "_chat_180_AnnotationIn",
        "AnnotationOut": "_chat_181_AnnotationOut",
        "SlashCommandIn": "_chat_182_SlashCommandIn",
        "SlashCommandOut": "_chat_183_SlashCommandOut",
        "SectionIn": "_chat_184_SectionIn",
        "SectionOut": "_chat_185_SectionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleAppsCardV1DecoratedTextIn"] = t.struct(
        {
            "text": t.string(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "bottomLabel": t.string().optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonIn"]).optional(),
            "wrapText": t.boolean().optional(),
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
            "topLabel": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlIn"]
            ).optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextIn"])
    types["GoogleAppsCardV1DecoratedTextOut"] = t.struct(
        {
            "text": t.string(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "bottomLabel": t.string().optional(),
            "button": t.proxy(renames["GoogleAppsCardV1ButtonOut"]).optional(),
            "wrapText": t.boolean().optional(),
            "endIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "topLabel": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "switchControl": t.proxy(
                renames["GoogleAppsCardV1SwitchControlOut"]
            ).optional(),
            "startIcon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DecoratedTextOut"])
    types["UploadAttachmentRequestIn"] = t.struct({"filename": t.string()}).named(
        renames["UploadAttachmentRequestIn"]
    )
    types["UploadAttachmentRequestOut"] = t.struct(
        {"filename": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UploadAttachmentRequestOut"])
    types["GoogleAppsCardV1BorderStyleIn"] = t.struct(
        {
            "type": t.string().optional(),
            "strokeColor": t.proxy(renames["ColorIn"]).optional(),
            "cornerRadius": t.integer().optional(),
        }
    ).named(renames["GoogleAppsCardV1BorderStyleIn"])
    types["GoogleAppsCardV1BorderStyleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "strokeColor": t.proxy(renames["ColorOut"]).optional(),
            "cornerRadius": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1BorderStyleOut"])
    types["GoogleAppsCardV1TextInputIn"] = t.struct(
        {
            "value": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsIn"]
            ).optional(),
            "hintText": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputIn"])
    types["GoogleAppsCardV1TextInputOut"] = t.struct(
        {
            "value": t.string().optional(),
            "initialSuggestions": t.proxy(
                renames["GoogleAppsCardV1SuggestionsOut"]
            ).optional(),
            "hintText": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "label": t.string().optional(),
            "autoCompleteAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextInputOut"])
    types["MembershipIn"] = t.struct(
        {"member": t.proxy(renames["UserIn"]).optional(), "name": t.string().optional()}
    ).named(renames["MembershipIn"])
    types["MembershipOut"] = t.struct(
        {
            "member": t.proxy(renames["UserOut"]).optional(),
            "role": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MembershipOut"])
    types["AttachmentIn"] = t.struct(
        {
            "name": t.string().optional(),
            "source": t.string().optional(),
            "contentName": t.string().optional(),
            "contentType": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefIn"]).optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefIn"]).optional(),
        }
    ).named(renames["AttachmentIn"])
    types["AttachmentOut"] = t.struct(
        {
            "thumbnailUri": t.string().optional(),
            "downloadUri": t.string().optional(),
            "name": t.string().optional(),
            "source": t.string().optional(),
            "contentName": t.string().optional(),
            "contentType": t.string().optional(),
            "driveDataRef": t.proxy(renames["DriveDataRefOut"]).optional(),
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentOut"])
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
    types["CardHeaderIn"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
            "imageStyle": t.string().optional(),
            "subtitle": t.string().optional(),
        }
    ).named(renames["CardHeaderIn"])
    types["CardHeaderOut"] = t.struct(
        {
            "imageUrl": t.string().optional(),
            "title": t.string().optional(),
            "imageStyle": t.string().optional(),
            "subtitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardHeaderOut"])
    types["TextParagraphIn"] = t.struct({"text": t.string()}).named(
        renames["TextParagraphIn"]
    )
    types["TextParagraphOut"] = t.struct(
        {"text": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextParagraphOut"])
    types["SetUpSpaceRequestIn"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["MembershipIn"])).optional(),
            "requestId": t.string().optional(),
            "space": t.proxy(renames["SpaceIn"]),
        }
    ).named(renames["SetUpSpaceRequestIn"])
    types["SetUpSpaceRequestOut"] = t.struct(
        {
            "memberships": t.array(t.proxy(renames["MembershipOut"])).optional(),
            "requestId": t.string().optional(),
            "space": t.proxy(renames["SpaceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetUpSpaceRequestOut"])
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
    types["GoogleAppsCardV1GridItemIn"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentIn"]).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "layout": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemIn"])
    types["GoogleAppsCardV1GridItemOut"] = t.struct(
        {
            "subtitle": t.string().optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageComponentOut"]).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "layout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridItemOut"])
    types["AttachmentDataRefIn"] = t.struct(
        {
            "attachmentUploadToken": t.string().optional(),
            "resourceName": t.string().optional(),
        }
    ).named(renames["AttachmentDataRefIn"])
    types["AttachmentDataRefOut"] = t.struct(
        {
            "attachmentUploadToken": t.string().optional(),
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachmentDataRefOut"])
    types["MatchedUrlIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MatchedUrlIn"]
    )
    types["MatchedUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MatchedUrlOut"])
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
    types["SpaceIn"] = t.struct(
        {
            "singleUserBotDm": t.boolean().optional(),
            "name": t.string().optional(),
            "spaceHistoryState": t.string().optional(),
            "displayName": t.string().optional(),
            "spaceDetails": t.proxy(renames["SpaceDetailsIn"]).optional(),
            "spaceType": t.string().optional(),
        }
    ).named(renames["SpaceIn"])
    types["SpaceOut"] = t.struct(
        {
            "singleUserBotDm": t.boolean().optional(),
            "name": t.string().optional(),
            "adminInstalled": t.boolean().optional(),
            "type": t.string().optional(),
            "threaded": t.boolean().optional(),
            "spaceHistoryState": t.string().optional(),
            "spaceThreadingState": t.string().optional(),
            "displayName": t.string().optional(),
            "spaceDetails": t.proxy(renames["SpaceDetailsOut"]).optional(),
            "spaceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceOut"])
    types["GoogleAppsCardV1ImageComponentIn"] = t.struct(
        {
            "cropStyle": t.proxy(
                renames["GoogleAppsCardV1ImageCropStyleIn"]
            ).optional(),
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "altText": t.string().optional(),
            "imageUri": t.string().optional(),
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
            "altText": t.string().optional(),
            "imageUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageComponentOut"])
    types["ImageIn"] = t.struct(
        {
            "aspectRatio": t.number().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "imageUrl": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "aspectRatio": t.number().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "imageUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["InputsIn"] = t.struct(
        {
            "timeInput": t.proxy(renames["TimeInputIn"]).optional(),
            "stringInputs": t.proxy(renames["StringInputsIn"]).optional(),
            "dateTimeInput": t.proxy(renames["DateTimeInputIn"]).optional(),
            "dateInput": t.proxy(renames["DateInputIn"]).optional(),
        }
    ).named(renames["InputsIn"])
    types["InputsOut"] = t.struct(
        {
            "timeInput": t.proxy(renames["TimeInputOut"]).optional(),
            "stringInputs": t.proxy(renames["StringInputsOut"]).optional(),
            "dateTimeInput": t.proxy(renames["DateTimeInputOut"]).optional(),
            "dateInput": t.proxy(renames["DateInputOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputsOut"])
    types["UploadAttachmentResponseIn"] = t.struct(
        {"attachmentDataRef": t.proxy(renames["AttachmentDataRefIn"]).optional()}
    ).named(renames["UploadAttachmentResponseIn"])
    types["UploadAttachmentResponseOut"] = t.struct(
        {
            "attachmentDataRef": t.proxy(renames["AttachmentDataRefOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UploadAttachmentResponseOut"])
    types["GoogleAppsCardV1WidgetsIn"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageIn"]).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputIn"]).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListIn"]).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerIn"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputIn"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphIn"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetsIn"])
    types["GoogleAppsCardV1WidgetsOut"] = t.struct(
        {
            "image": t.proxy(renames["GoogleAppsCardV1ImageOut"]).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputOut"]).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListOut"]).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerOut"]
            ).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputOut"]
            ).optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphOut"]
            ).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetsOut"])
    types["OpenLinkIn"] = t.struct({"url": t.string().optional()}).named(
        renames["OpenLinkIn"]
    )
    types["OpenLinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OpenLinkOut"])
    types["SpaceDetailsIn"] = t.struct(
        {"description": t.string().optional(), "guidelines": t.string().optional()}
    ).named(renames["SpaceDetailsIn"])
    types["SpaceDetailsOut"] = t.struct(
        {
            "description": t.string().optional(),
            "guidelines": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpaceDetailsOut"])
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
    types["GoogleAppsCardV1WidgetIn"] = t.struct(
        {
            "grid": t.proxy(renames["GoogleAppsCardV1GridIn"]).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputIn"]).optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageIn"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphIn"]
            ).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListIn"]).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerIn"]).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputIn"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerIn"]
            ).optional(),
            "columns": t.proxy(renames["GoogleAppsCardV1ColumnsIn"]).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextIn"]
            ).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetIn"])
    types["GoogleAppsCardV1WidgetOut"] = t.struct(
        {
            "grid": t.proxy(renames["GoogleAppsCardV1GridOut"]).optional(),
            "textInput": t.proxy(renames["GoogleAppsCardV1TextInputOut"]).optional(),
            "image": t.proxy(renames["GoogleAppsCardV1ImageOut"]).optional(),
            "horizontalAlignment": t.string().optional(),
            "textParagraph": t.proxy(
                renames["GoogleAppsCardV1TextParagraphOut"]
            ).optional(),
            "buttonList": t.proxy(renames["GoogleAppsCardV1ButtonListOut"]).optional(),
            "divider": t.proxy(renames["GoogleAppsCardV1DividerOut"]).optional(),
            "selectionInput": t.proxy(
                renames["GoogleAppsCardV1SelectionInputOut"]
            ).optional(),
            "dateTimePicker": t.proxy(
                renames["GoogleAppsCardV1DateTimePickerOut"]
            ).optional(),
            "columns": t.proxy(renames["GoogleAppsCardV1ColumnsOut"]).optional(),
            "decoratedText": t.proxy(
                renames["GoogleAppsCardV1DecoratedTextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1WidgetOut"])
    types["GoogleAppsCardV1ImageCropStyleIn"] = t.struct(
        {"type": t.string().optional(), "aspectRatio": t.number().optional()}
    ).named(renames["GoogleAppsCardV1ImageCropStyleIn"])
    types["GoogleAppsCardV1ImageCropStyleOut"] = t.struct(
        {
            "type": t.string().optional(),
            "aspectRatio": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageCropStyleOut"])
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
    types["StringInputsIn"] = t.struct({"value": t.array(t.string()).optional()}).named(
        renames["StringInputsIn"]
    )
    types["StringInputsOut"] = t.struct(
        {
            "value": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringInputsOut"])
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
    types["GoogleAppsCardV1OnClickIn"] = t.struct(
        {
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkIn"]).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionIn"]
            ).optional(),
            "action": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickIn"])
    types["GoogleAppsCardV1OnClickOut"] = t.struct(
        {
            "openLink": t.proxy(renames["GoogleAppsCardV1OpenLinkOut"]).optional(),
            "card": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "openDynamicLinkAction": t.proxy(
                renames["GoogleAppsCardV1ActionOut"]
            ).optional(),
            "action": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1OnClickOut"])
    types["DateInputIn"] = t.struct({"msSinceEpoch": t.string().optional()}).named(
        renames["DateInputIn"]
    )
    types["DateInputOut"] = t.struct(
        {
            "msSinceEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateInputOut"])
    types["GoogleAppsCardV1TextParagraphIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1TextParagraphIn"])
    types["GoogleAppsCardV1TextParagraphOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1TextParagraphOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ImageButtonIn"] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "icon": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ImageButtonIn"])
    types["ImageButtonOut"] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "icon": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageButtonOut"])
    types["EmojiReactionSummaryIn"] = t.struct(
        {
            "reactionCount": t.integer().optional(),
            "emoji": t.proxy(renames["EmojiIn"]).optional(),
        }
    ).named(renames["EmojiReactionSummaryIn"])
    types["EmojiReactionSummaryOut"] = t.struct(
        {
            "reactionCount": t.integer().optional(),
            "emoji": t.proxy(renames["EmojiOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmojiReactionSummaryOut"])
    types["TimeZoneIn"] = t.struct(
        {"offset": t.integer().optional(), "id": t.string().optional()}
    ).named(renames["TimeZoneIn"])
    types["TimeZoneOut"] = t.struct(
        {
            "offset": t.integer().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeZoneOut"])
    types["DialogIn"] = t.struct(
        {"body": t.proxy(renames["GoogleAppsCardV1CardIn"]).optional()}
    ).named(renames["DialogIn"])
    types["DialogOut"] = t.struct(
        {
            "body": t.proxy(renames["GoogleAppsCardV1CardOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DialogOut"])
    types["AttachedGifIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AttachedGifIn"]
    )
    types["AttachedGifOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachedGifOut"])
    types["DeletionMetadataIn"] = t.struct(
        {"deletionType": t.string().optional()}
    ).named(renames["DeletionMetadataIn"])
    types["DeletionMetadataOut"] = t.struct(
        {
            "deletionType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeletionMetadataOut"])
    types["UserIn"] = t.struct(
        {
            "domainId": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "domainId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "isAnonymous": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["ReactionIn"] = t.struct(
        {"emoji": t.proxy(renames["EmojiIn"]).optional(), "name": t.string().optional()}
    ).named(renames["ReactionIn"])
    types["ReactionOut"] = t.struct(
        {
            "emoji": t.proxy(renames["EmojiOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReactionOut"])
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
    types["GoogleAppsCardV1GridIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["GoogleAppsCardV1GridItemIn"])).optional(),
            "columnCount": t.integer().optional(),
            "title": t.string().optional(),
            "borderStyle": t.proxy(renames["GoogleAppsCardV1BorderStyleIn"]).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridIn"])
    types["GoogleAppsCardV1GridOut"] = t.struct(
        {
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1GridItemOut"])
            ).optional(),
            "columnCount": t.integer().optional(),
            "title": t.string().optional(),
            "borderStyle": t.proxy(
                renames["GoogleAppsCardV1BorderStyleOut"]
            ).optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1GridOut"])
    types["MediaIn"] = t.struct({"resourceName": t.string().optional()}).named(
        renames["MediaIn"]
    )
    types["MediaOut"] = t.struct(
        {
            "resourceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaOut"])
    types["CustomEmojiIn"] = t.struct({"uid": t.string().optional()}).named(
        renames["CustomEmojiIn"]
    )
    types["CustomEmojiOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomEmojiOut"])
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
    types["MessageIn"] = t.struct(
        {
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
            "createTime": t.string().optional(),
            "thread": t.proxy(renames["ThreadIn"]).optional(),
            "clientAssignedMessageId": t.string().optional(),
            "name": t.string().optional(),
            "text": t.string().optional(),
            "fallbackText": t.string().optional(),
            "cards": t.array(t.proxy(renames["CardIn"])).optional(),
            "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
        }
    ).named(renames["MessageIn"])
    types["MessageOut"] = t.struct(
        {
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "deleteTime": t.string().optional(),
            "attachment": t.array(t.proxy(renames["AttachmentOut"])).optional(),
            "threadReply": t.boolean().optional(),
            "createTime": t.string().optional(),
            "matchedUrl": t.proxy(renames["MatchedUrlOut"]).optional(),
            "thread": t.proxy(renames["ThreadOut"]).optional(),
            "slashCommand": t.proxy(renames["SlashCommandOut"]).optional(),
            "clientAssignedMessageId": t.string().optional(),
            "emojiReactionSummaries": t.array(
                t.proxy(renames["EmojiReactionSummaryOut"])
            ).optional(),
            "name": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "attachedGifs": t.array(t.proxy(renames["AttachedGifOut"])).optional(),
            "text": t.string().optional(),
            "fallbackText": t.string().optional(),
            "deletionMetadata": t.proxy(renames["DeletionMetadataOut"]).optional(),
            "cards": t.array(t.proxy(renames["CardOut"])).optional(),
            "annotations": t.array(t.proxy(renames["AnnotationOut"])).optional(),
            "argumentText": t.string().optional(),
            "actionResponse": t.proxy(renames["ActionResponseOut"]).optional(),
            "sender": t.proxy(renames["UserOut"]).optional(),
            "cardsV2": t.array(t.proxy(renames["CardWithIdOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageOut"])
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
    types["GoogleAppsCardV1DividerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleAppsCardV1DividerIn"]
    )
    types["GoogleAppsCardV1DividerOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleAppsCardV1DividerOut"])
    types["DeprecatedEventIn"] = t.struct(
        {
            "eventTime": t.string().optional(),
            "dialogEventType": t.string().optional(),
            "isDialogEvent": t.boolean().optional(),
            "type": t.string().optional(),
            "action": t.proxy(renames["FormActionIn"]).optional(),
            "space": t.proxy(renames["SpaceIn"]).optional(),
            "message": t.proxy(renames["MessageIn"]).optional(),
            "threadKey": t.string().optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "token": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectIn"]).optional(),
        }
    ).named(renames["DeprecatedEventIn"])
    types["DeprecatedEventOut"] = t.struct(
        {
            "eventTime": t.string().optional(),
            "dialogEventType": t.string().optional(),
            "isDialogEvent": t.boolean().optional(),
            "type": t.string().optional(),
            "action": t.proxy(renames["FormActionOut"]).optional(),
            "space": t.proxy(renames["SpaceOut"]).optional(),
            "message": t.proxy(renames["MessageOut"]).optional(),
            "threadKey": t.string().optional(),
            "configCompleteRedirectUrl": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "token": t.string().optional(),
            "common": t.proxy(renames["CommonEventObjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeprecatedEventOut"])
    types["GoogleAppsCardV1DateTimePickerIn"] = t.struct(
        {
            "label": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "valueMsEpoch": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerIn"])
    types["GoogleAppsCardV1DateTimePickerOut"] = t.struct(
        {
            "label": t.string().optional(),
            "timezoneOffsetDate": t.integer().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "valueMsEpoch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1DateTimePickerOut"])
    types["ColorIn"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
        }
    ).named(renames["ColorIn"])
    types["ColorOut"] = t.struct(
        {
            "alpha": t.number().optional(),
            "red": t.number().optional(),
            "blue": t.number().optional(),
            "green": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColorOut"])
    types["GoogleAppsCardV1ColumnIn"] = t.struct(
        {
            "widgets": t.array(
                t.proxy(renames["GoogleAppsCardV1WidgetsIn"])
            ).optional(),
            "horizontalAlignment": t.string().optional(),
            "horizontalSizeStyle": t.string().optional(),
            "verticalAlignment": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ColumnIn"])
    types["GoogleAppsCardV1ColumnOut"] = t.struct(
        {
            "widgets": t.array(
                t.proxy(renames["GoogleAppsCardV1WidgetsOut"])
            ).optional(),
            "horizontalAlignment": t.string().optional(),
            "horizontalSizeStyle": t.string().optional(),
            "verticalAlignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ColumnOut"])
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
            "title": t.string(),
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderIn"])
    types["GoogleAppsCardV1CardHeaderOut"] = t.struct(
        {
            "title": t.string(),
            "imageUrl": t.string().optional(),
            "imageAltText": t.string().optional(),
            "subtitle": t.string().optional(),
            "imageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardHeaderOut"])
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
    types["GoogleAppsCardV1IconIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "imageType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1IconIn"])
    types["GoogleAppsCardV1IconOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "knownIcon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "imageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1IconOut"])
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
    types["KeyValueIn"] = t.struct(
        {
            "bottomLabel": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "content": t.string().optional(),
            "topLabel": t.string().optional(),
            "onClick": t.proxy(renames["OnClickIn"]).optional(),
            "button": t.proxy(renames["ButtonIn"]).optional(),
        }
    ).named(renames["KeyValueIn"])
    types["KeyValueOut"] = t.struct(
        {
            "bottomLabel": t.string().optional(),
            "contentMultiline": t.boolean().optional(),
            "icon": t.string().optional(),
            "iconUrl": t.string().optional(),
            "content": t.string().optional(),
            "topLabel": t.string().optional(),
            "onClick": t.proxy(renames["OnClickOut"]).optional(),
            "button": t.proxy(renames["ButtonOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyValueOut"])
    types["GoogleAppsCardV1ColumnsIn"] = t.struct(
        {
            "columnItems": t.array(
                t.proxy(renames["GoogleAppsCardV1ColumnIn"])
            ).optional()
        }
    ).named(renames["GoogleAppsCardV1ColumnsIn"])
    types["GoogleAppsCardV1ColumnsOut"] = t.struct(
        {
            "columnItems": t.array(
                t.proxy(renames["GoogleAppsCardV1ColumnOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ColumnsOut"])
    types["GoogleAppsCardV1ImageIn"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]).optional(),
            "imageUrl": t.string().optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageIn"])
    types["GoogleAppsCardV1ImageOut"] = t.struct(
        {
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]).optional(),
            "imageUrl": t.string().optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ImageOut"])
    types["GoogleAppsCardV1SelectionInputIn"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "name": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemIn"])
            ).optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputIn"])
    types["GoogleAppsCardV1SelectionInputOut"] = t.struct(
        {
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "name": t.string().optional(),
            "items": t.array(
                t.proxy(renames["GoogleAppsCardV1SelectionItemOut"])
            ).optional(),
            "label": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionInputOut"])
    types["CardIn"] = t.struct(
        {
            "name": t.string().optional(),
            "header": t.proxy(renames["CardHeaderIn"]).optional(),
            "sections": t.array(t.proxy(renames["SectionIn"])).optional(),
            "cardActions": t.array(t.proxy(renames["CardActionIn"])).optional(),
        }
    ).named(renames["CardIn"])
    types["CardOut"] = t.struct(
        {
            "name": t.string().optional(),
            "header": t.proxy(renames["CardHeaderOut"]).optional(),
            "sections": t.array(t.proxy(renames["SectionOut"])).optional(),
            "cardActions": t.array(t.proxy(renames["CardActionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CardOut"])
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
    types["GoogleAppsCardV1SelectionItemIn"] = t.struct(
        {
            "value": t.string().optional(),
            "text": t.string().optional(),
            "selected": t.boolean().optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemIn"])
    types["GoogleAppsCardV1SelectionItemOut"] = t.struct(
        {
            "value": t.string().optional(),
            "text": t.string().optional(),
            "selected": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SelectionItemOut"])
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
    types["ListMessagesResponseIn"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["MessageIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListMessagesResponseIn"])
    types["ListMessagesResponseOut"] = t.struct(
        {
            "messages": t.array(t.proxy(renames["MessageOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMessagesResponseOut"])
    types["GoogleAppsCardV1ActionIn"] = t.struct(
        {
            "loadIndicator": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterIn"])
            ).optional(),
            "interaction": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionIn"])
    types["GoogleAppsCardV1ActionOut"] = t.struct(
        {
            "loadIndicator": t.string().optional(),
            "parameters": t.array(
                t.proxy(renames["GoogleAppsCardV1ActionParameterOut"])
            ).optional(),
            "interaction": t.string().optional(),
            "persistValues": t.boolean().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ActionOut"])
    types["GoogleAppsCardV1SwitchControlIn"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionIn"]).optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "controlType": t.string().optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlIn"])
    types["GoogleAppsCardV1SwitchControlOut"] = t.struct(
        {
            "selected": t.boolean().optional(),
            "onChangeAction": t.proxy(renames["GoogleAppsCardV1ActionOut"]).optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "controlType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SwitchControlOut"])
    types["CommonEventObjectIn"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneIn"]).optional(),
            "hostApp": t.string().optional(),
            "userLocale": t.string().optional(),
            "platform": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "invokedFunction": t.string().optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CommonEventObjectIn"])
    types["CommonEventObjectOut"] = t.struct(
        {
            "timeZone": t.proxy(renames["TimeZoneOut"]).optional(),
            "hostApp": t.string().optional(),
            "userLocale": t.string().optional(),
            "platform": t.string().optional(),
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "invokedFunction": t.string().optional(),
            "formInputs": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonEventObjectOut"])
    types["GoogleAppsCardV1CardIn"] = t.struct(
        {
            "displayStyle": t.string().optional(),
            "name": t.string().optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionIn"])
            ).optional(),
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderIn"]
            ).optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionIn"])
            ).optional(),
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterIn"]
            ).optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardIn"])
    types["GoogleAppsCardV1CardOut"] = t.struct(
        {
            "displayStyle": t.string().optional(),
            "name": t.string().optional(),
            "cardActions": t.array(
                t.proxy(renames["GoogleAppsCardV1CardActionOut"])
            ).optional(),
            "peekCardHeader": t.proxy(
                renames["GoogleAppsCardV1CardHeaderOut"]
            ).optional(),
            "sections": t.array(
                t.proxy(renames["GoogleAppsCardV1SectionOut"])
            ).optional(),
            "fixedFooter": t.proxy(
                renames["GoogleAppsCardV1CardFixedFooterOut"]
            ).optional(),
            "header": t.proxy(renames["GoogleAppsCardV1CardHeaderOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1CardOut"])
    types["DriveDataRefIn"] = t.struct({"driveFileId": t.string().optional()}).named(
        renames["DriveDataRefIn"]
    )
    types["DriveDataRefOut"] = t.struct(
        {
            "driveFileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DriveDataRefOut"])
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
    types["ChatAppLogEntryIn"] = t.struct(
        {
            "deployment": t.string().optional(),
            "deploymentFunction": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ChatAppLogEntryIn"])
    types["ChatAppLogEntryOut"] = t.struct(
        {
            "deployment": t.string().optional(),
            "deploymentFunction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChatAppLogEntryOut"])
    types["WidgetMarkupIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "keyValue": t.proxy(renames["KeyValueIn"]).optional(),
            "textParagraph": t.proxy(renames["TextParagraphIn"]).optional(),
            "buttons": t.array(t.proxy(renames["ButtonIn"])).optional(),
        }
    ).named(renames["WidgetMarkupIn"])
    types["WidgetMarkupOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "keyValue": t.proxy(renames["KeyValueOut"]).optional(),
            "textParagraph": t.proxy(renames["TextParagraphOut"]).optional(),
            "buttons": t.array(t.proxy(renames["ButtonOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WidgetMarkupOut"])
    types["GoogleAppsCardV1SuggestionItemIn"] = t.struct(
        {"text": t.string().optional()}
    ).named(renames["GoogleAppsCardV1SuggestionItemIn"])
    types["GoogleAppsCardV1SuggestionItemOut"] = t.struct(
        {
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1SuggestionItemOut"])
    types["ListReactionsResponseIn"] = t.struct(
        {
            "reactions": t.array(t.proxy(renames["ReactionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListReactionsResponseIn"])
    types["ListReactionsResponseOut"] = t.struct(
        {
            "reactions": t.array(t.proxy(renames["ReactionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReactionsResponseOut"])
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
    types["SlashCommandMetadataIn"] = t.struct(
        {
            "commandId": t.string().optional(),
            "triggersDialog": t.boolean().optional(),
            "type": t.string().optional(),
            "bot": t.proxy(renames["UserIn"]).optional(),
            "commandName": t.string().optional(),
        }
    ).named(renames["SlashCommandMetadataIn"])
    types["SlashCommandMetadataOut"] = t.struct(
        {
            "commandId": t.string().optional(),
            "triggersDialog": t.boolean().optional(),
            "type": t.string().optional(),
            "bot": t.proxy(renames["UserOut"]).optional(),
            "commandName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandMetadataOut"])
    types["EmojiIn"] = t.struct({"unicode": t.string().optional()}).named(
        renames["EmojiIn"]
    )
    types["EmojiOut"] = t.struct(
        {
            "unicode": t.string().optional(),
            "customEmoji": t.proxy(renames["CustomEmojiOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EmojiOut"])
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
    types["GoogleAppsCardV1ButtonIn"] = t.struct(
        {
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickIn"]),
            "text": t.string().optional(),
            "disabled": t.boolean().optional(),
            "color": t.proxy(renames["ColorIn"]).optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconIn"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonIn"])
    types["GoogleAppsCardV1ButtonOut"] = t.struct(
        {
            "altText": t.string().optional(),
            "onClick": t.proxy(renames["GoogleAppsCardV1OnClickOut"]),
            "text": t.string().optional(),
            "disabled": t.boolean().optional(),
            "color": t.proxy(renames["ColorOut"]).optional(),
            "icon": t.proxy(renames["GoogleAppsCardV1IconOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppsCardV1ButtonOut"])
    types["AnnotationIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "length": t.integer().optional(),
            "type": t.string().optional(),
            "userMention": t.proxy(renames["UserMentionMetadataIn"]).optional(),
            "slashCommand": t.proxy(renames["SlashCommandMetadataIn"]).optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "length": t.integer().optional(),
            "type": t.string().optional(),
            "userMention": t.proxy(renames["UserMentionMetadataOut"]).optional(),
            "slashCommand": t.proxy(renames["SlashCommandMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["SlashCommandIn"] = t.struct({"commandId": t.string().optional()}).named(
        renames["SlashCommandIn"]
    )
    types["SlashCommandOut"] = t.struct(
        {
            "commandId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SlashCommandOut"])
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

    functions = {}
    functions["spacesGet"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesFindDirectMessage"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesSetup"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesCreate"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesPatch"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesList"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesDelete"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMembersDelete"] = chat.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMembersList"] = chat.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMembersCreate"] = chat.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMembersGet"] = chat.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["MembershipOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesCreate"] = chat.put(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "createTime": t.string().optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "text": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
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
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "createTime": t.string().optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "text": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
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
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "createTime": t.string().optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "text": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["MessageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesList"] = chat.put(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "createTime": t.string().optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "text": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
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
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "createTime": t.string().optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "text": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
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
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string(),
                "name": t.string().optional(),
                "space": t.proxy(renames["SpaceIn"]).optional(),
                "attachment": t.array(t.proxy(renames["AttachmentIn"])).optional(),
                "createTime": t.string().optional(),
                "thread": t.proxy(renames["ThreadIn"]).optional(),
                "clientAssignedMessageId": t.string().optional(),
                "text": t.string().optional(),
                "fallbackText": t.string().optional(),
                "cards": t.array(t.proxy(renames["CardIn"])).optional(),
                "actionResponse": t.proxy(renames["ActionResponseIn"]).optional(),
                "cardsV2": t.array(t.proxy(renames["CardWithIdIn"])).optional(),
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
    functions["spacesMessagesReactionsList"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesReactionsCreate"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["spacesMessagesReactionsDelete"] = chat.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaDownload"] = chat.post(
        "v1/{parent}/attachments:upload",
        t.struct(
            {
                "parent": t.string(),
                "filename": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadAttachmentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["mediaUpload"] = chat.post(
        "v1/{parent}/attachments:upload",
        t.struct(
            {
                "parent": t.string(),
                "filename": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UploadAttachmentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="chat", renames=renames, types=Box(types), functions=Box(functions)
    )
