from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_forms() -> Import:
    forms = HTTPRuntime("https://forms.googleapis.com/")

    renames = {
        "ErrorResponse": "_forms_1_ErrorResponse",
        "ImageIn": "_forms_2_ImageIn",
        "ImageOut": "_forms_3_ImageOut",
        "AnswerIn": "_forms_4_AnswerIn",
        "AnswerOut": "_forms_5_AnswerOut",
        "TextItemIn": "_forms_6_TextItemIn",
        "TextItemOut": "_forms_7_TextItemOut",
        "TimeQuestionIn": "_forms_8_TimeQuestionIn",
        "TimeQuestionOut": "_forms_9_TimeQuestionOut",
        "OptionIn": "_forms_10_OptionIn",
        "OptionOut": "_forms_11_OptionOut",
        "BatchUpdateFormRequestIn": "_forms_12_BatchUpdateFormRequestIn",
        "BatchUpdateFormRequestOut": "_forms_13_BatchUpdateFormRequestOut",
        "MoveItemRequestIn": "_forms_14_MoveItemRequestIn",
        "MoveItemRequestOut": "_forms_15_MoveItemRequestOut",
        "RequestIn": "_forms_16_RequestIn",
        "RequestOut": "_forms_17_RequestOut",
        "GradingIn": "_forms_18_GradingIn",
        "GradingOut": "_forms_19_GradingOut",
        "ScaleQuestionIn": "_forms_20_ScaleQuestionIn",
        "ScaleQuestionOut": "_forms_21_ScaleQuestionOut",
        "TextAnswersIn": "_forms_22_TextAnswersIn",
        "TextAnswersOut": "_forms_23_TextAnswersOut",
        "CorrectAnswerIn": "_forms_24_CorrectAnswerIn",
        "CorrectAnswerOut": "_forms_25_CorrectAnswerOut",
        "ChoiceQuestionIn": "_forms_26_ChoiceQuestionIn",
        "ChoiceQuestionOut": "_forms_27_ChoiceQuestionOut",
        "FormResponseIn": "_forms_28_FormResponseIn",
        "FormResponseOut": "_forms_29_FormResponseOut",
        "EmptyIn": "_forms_30_EmptyIn",
        "EmptyOut": "_forms_31_EmptyOut",
        "TextQuestionIn": "_forms_32_TextQuestionIn",
        "TextQuestionOut": "_forms_33_TextQuestionOut",
        "QuestionIn": "_forms_34_QuestionIn",
        "QuestionOut": "_forms_35_QuestionOut",
        "FileUploadAnswerIn": "_forms_36_FileUploadAnswerIn",
        "FileUploadAnswerOut": "_forms_37_FileUploadAnswerOut",
        "DateQuestionIn": "_forms_38_DateQuestionIn",
        "DateQuestionOut": "_forms_39_DateQuestionOut",
        "VideoLinkIn": "_forms_40_VideoLinkIn",
        "VideoLinkOut": "_forms_41_VideoLinkOut",
        "ExtraMaterialIn": "_forms_42_ExtraMaterialIn",
        "ExtraMaterialOut": "_forms_43_ExtraMaterialOut",
        "FormSettingsIn": "_forms_44_FormSettingsIn",
        "FormSettingsOut": "_forms_45_FormSettingsOut",
        "TextAnswerIn": "_forms_46_TextAnswerIn",
        "TextAnswerOut": "_forms_47_TextAnswerOut",
        "MediaPropertiesIn": "_forms_48_MediaPropertiesIn",
        "MediaPropertiesOut": "_forms_49_MediaPropertiesOut",
        "VideoIn": "_forms_50_VideoIn",
        "VideoOut": "_forms_51_VideoOut",
        "CreateWatchRequestIn": "_forms_52_CreateWatchRequestIn",
        "CreateWatchRequestOut": "_forms_53_CreateWatchRequestOut",
        "QuestionGroupItemIn": "_forms_54_QuestionGroupItemIn",
        "QuestionGroupItemOut": "_forms_55_QuestionGroupItemOut",
        "ResponseIn": "_forms_56_ResponseIn",
        "ResponseOut": "_forms_57_ResponseOut",
        "ImageItemIn": "_forms_58_ImageItemIn",
        "ImageItemOut": "_forms_59_ImageItemOut",
        "CreateItemResponseIn": "_forms_60_CreateItemResponseIn",
        "CreateItemResponseOut": "_forms_61_CreateItemResponseOut",
        "InfoIn": "_forms_62_InfoIn",
        "InfoOut": "_forms_63_InfoOut",
        "DeleteItemRequestIn": "_forms_64_DeleteItemRequestIn",
        "DeleteItemRequestOut": "_forms_65_DeleteItemRequestOut",
        "FormIn": "_forms_66_FormIn",
        "FormOut": "_forms_67_FormOut",
        "UpdateItemRequestIn": "_forms_68_UpdateItemRequestIn",
        "UpdateItemRequestOut": "_forms_69_UpdateItemRequestOut",
        "GradeIn": "_forms_70_GradeIn",
        "GradeOut": "_forms_71_GradeOut",
        "WatchIn": "_forms_72_WatchIn",
        "WatchOut": "_forms_73_WatchOut",
        "WatchTargetIn": "_forms_74_WatchTargetIn",
        "WatchTargetOut": "_forms_75_WatchTargetOut",
        "QuestionItemIn": "_forms_76_QuestionItemIn",
        "QuestionItemOut": "_forms_77_QuestionItemOut",
        "ListWatchesResponseIn": "_forms_78_ListWatchesResponseIn",
        "ListWatchesResponseOut": "_forms_79_ListWatchesResponseOut",
        "CloudPubsubTopicIn": "_forms_80_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_forms_81_CloudPubsubTopicOut",
        "CorrectAnswersIn": "_forms_82_CorrectAnswersIn",
        "CorrectAnswersOut": "_forms_83_CorrectAnswersOut",
        "ListFormResponsesResponseIn": "_forms_84_ListFormResponsesResponseIn",
        "ListFormResponsesResponseOut": "_forms_85_ListFormResponsesResponseOut",
        "RenewWatchRequestIn": "_forms_86_RenewWatchRequestIn",
        "RenewWatchRequestOut": "_forms_87_RenewWatchRequestOut",
        "LocationIn": "_forms_88_LocationIn",
        "LocationOut": "_forms_89_LocationOut",
        "RowQuestionIn": "_forms_90_RowQuestionIn",
        "RowQuestionOut": "_forms_91_RowQuestionOut",
        "BatchUpdateFormResponseIn": "_forms_92_BatchUpdateFormResponseIn",
        "BatchUpdateFormResponseOut": "_forms_93_BatchUpdateFormResponseOut",
        "PageBreakItemIn": "_forms_94_PageBreakItemIn",
        "PageBreakItemOut": "_forms_95_PageBreakItemOut",
        "TextLinkIn": "_forms_96_TextLinkIn",
        "TextLinkOut": "_forms_97_TextLinkOut",
        "FileUploadQuestionIn": "_forms_98_FileUploadQuestionIn",
        "FileUploadQuestionOut": "_forms_99_FileUploadQuestionOut",
        "ItemIn": "_forms_100_ItemIn",
        "ItemOut": "_forms_101_ItemOut",
        "WriteControlIn": "_forms_102_WriteControlIn",
        "WriteControlOut": "_forms_103_WriteControlOut",
        "VideoItemIn": "_forms_104_VideoItemIn",
        "VideoItemOut": "_forms_105_VideoItemOut",
        "FeedbackIn": "_forms_106_FeedbackIn",
        "FeedbackOut": "_forms_107_FeedbackOut",
        "QuizSettingsIn": "_forms_108_QuizSettingsIn",
        "QuizSettingsOut": "_forms_109_QuizSettingsOut",
        "GridIn": "_forms_110_GridIn",
        "GridOut": "_forms_111_GridOut",
        "FileUploadAnswersIn": "_forms_112_FileUploadAnswersIn",
        "FileUploadAnswersOut": "_forms_113_FileUploadAnswersOut",
        "UpdateSettingsRequestIn": "_forms_114_UpdateSettingsRequestIn",
        "UpdateSettingsRequestOut": "_forms_115_UpdateSettingsRequestOut",
        "UpdateFormInfoRequestIn": "_forms_116_UpdateFormInfoRequestIn",
        "UpdateFormInfoRequestOut": "_forms_117_UpdateFormInfoRequestOut",
        "CreateItemRequestIn": "_forms_118_CreateItemRequestIn",
        "CreateItemRequestOut": "_forms_119_CreateItemRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ImageIn"] = t.struct(
        {
            "sourceUri": t.string().optional(),
            "altText": t.string().optional(),
            "properties": t.proxy(renames["MediaPropertiesIn"]).optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "sourceUri": t.string().optional(),
            "contentUri": t.string().optional(),
            "altText": t.string().optional(),
            "properties": t.proxy(renames["MediaPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["AnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnswerIn"]
    )
    types["AnswerOut"] = t.struct(
        {
            "textAnswers": t.proxy(renames["TextAnswersOut"]).optional(),
            "questionId": t.string().optional(),
            "fileUploadAnswers": t.proxy(renames["FileUploadAnswersOut"]).optional(),
            "grade": t.proxy(renames["GradeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnswerOut"])
    types["TextItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextItemIn"]
    )
    types["TextItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextItemOut"])
    types["TimeQuestionIn"] = t.struct({"duration": t.boolean().optional()}).named(
        renames["TimeQuestionIn"]
    )
    types["TimeQuestionOut"] = t.struct(
        {
            "duration": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeQuestionOut"])
    types["OptionIn"] = t.struct(
        {
            "goToAction": t.string().optional(),
            "goToSectionId": t.string().optional(),
            "value": t.string(),
            "isOther": t.boolean().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "goToAction": t.string().optional(),
            "goToSectionId": t.string().optional(),
            "value": t.string(),
            "isOther": t.boolean().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
    types["BatchUpdateFormRequestIn"] = t.struct(
        {
            "includeFormInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
        }
    ).named(renames["BatchUpdateFormRequestIn"])
    types["BatchUpdateFormRequestOut"] = t.struct(
        {
            "includeFormInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateFormRequestOut"])
    types["MoveItemRequestIn"] = t.struct(
        {
            "originalLocation": t.proxy(renames["LocationIn"]),
            "newLocation": t.proxy(renames["LocationIn"]),
        }
    ).named(renames["MoveItemRequestIn"])
    types["MoveItemRequestOut"] = t.struct(
        {
            "originalLocation": t.proxy(renames["LocationOut"]),
            "newLocation": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveItemRequestOut"])
    types["RequestIn"] = t.struct(
        {
            "updateItem": t.proxy(renames["UpdateItemRequestIn"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestIn"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestIn"]).optional(),
            "deleteItem": t.proxy(renames["DeleteItemRequestIn"]).optional(),
            "moveItem": t.proxy(renames["MoveItemRequestIn"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "updateItem": t.proxy(renames["UpdateItemRequestOut"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestOut"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestOut"]).optional(),
            "deleteItem": t.proxy(renames["DeleteItemRequestOut"]).optional(),
            "moveItem": t.proxy(renames["MoveItemRequestOut"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["GradingIn"] = t.struct(
        {
            "generalFeedback": t.proxy(renames["FeedbackIn"]).optional(),
            "whenRight": t.proxy(renames["FeedbackIn"]).optional(),
            "whenWrong": t.proxy(renames["FeedbackIn"]).optional(),
            "correctAnswers": t.proxy(renames["CorrectAnswersIn"]),
            "pointValue": t.integer(),
        }
    ).named(renames["GradingIn"])
    types["GradingOut"] = t.struct(
        {
            "generalFeedback": t.proxy(renames["FeedbackOut"]).optional(),
            "whenRight": t.proxy(renames["FeedbackOut"]).optional(),
            "whenWrong": t.proxy(renames["FeedbackOut"]).optional(),
            "correctAnswers": t.proxy(renames["CorrectAnswersOut"]),
            "pointValue": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradingOut"])
    types["ScaleQuestionIn"] = t.struct(
        {
            "high": t.integer(),
            "low": t.integer(),
            "lowLabel": t.string().optional(),
            "highLabel": t.string().optional(),
        }
    ).named(renames["ScaleQuestionIn"])
    types["ScaleQuestionOut"] = t.struct(
        {
            "high": t.integer(),
            "low": t.integer(),
            "lowLabel": t.string().optional(),
            "highLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScaleQuestionOut"])
    types["TextAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswersIn"]
    )
    types["TextAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["TextAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswersOut"])
    types["CorrectAnswerIn"] = t.struct({"value": t.string()}).named(
        renames["CorrectAnswerIn"]
    )
    types["CorrectAnswerOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CorrectAnswerOut"])
    types["ChoiceQuestionIn"] = t.struct(
        {
            "type": t.string(),
            "options": t.array(t.proxy(renames["OptionIn"])),
            "shuffle": t.boolean().optional(),
        }
    ).named(renames["ChoiceQuestionIn"])
    types["ChoiceQuestionOut"] = t.struct(
        {
            "type": t.string(),
            "options": t.array(t.proxy(renames["OptionOut"])),
            "shuffle": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChoiceQuestionOut"])
    types["FormResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FormResponseIn"]
    )
    types["FormResponseOut"] = t.struct(
        {
            "respondentEmail": t.string().optional(),
            "answers": t.struct({"_": t.string().optional()}).optional(),
            "responseId": t.string().optional(),
            "formId": t.string().optional(),
            "totalScore": t.number().optional(),
            "createTime": t.string().optional(),
            "lastSubmittedTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TextQuestionIn"] = t.struct({"paragraph": t.boolean().optional()}).named(
        renames["TextQuestionIn"]
    )
    types["TextQuestionOut"] = t.struct(
        {
            "paragraph": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextQuestionOut"])
    types["QuestionIn"] = t.struct(
        {
            "grading": t.proxy(renames["GradingIn"]).optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionIn"]).optional(),
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionIn"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionIn"]).optional(),
            "required": t.boolean().optional(),
            "rowQuestion": t.proxy(renames["RowQuestionIn"]).optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionIn"]).optional(),
            "dateQuestion": t.proxy(renames["DateQuestionIn"]).optional(),
            "textQuestion": t.proxy(renames["TextQuestionIn"]).optional(),
            "questionId": t.string().optional(),
        }
    ).named(renames["QuestionIn"])
    types["QuestionOut"] = t.struct(
        {
            "grading": t.proxy(renames["GradingOut"]).optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionOut"]).optional(),
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionOut"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionOut"]).optional(),
            "required": t.boolean().optional(),
            "rowQuestion": t.proxy(renames["RowQuestionOut"]).optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionOut"]).optional(),
            "dateQuestion": t.proxy(renames["DateQuestionOut"]).optional(),
            "textQuestion": t.proxy(renames["TextQuestionOut"]).optional(),
            "questionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionOut"])
    types["FileUploadAnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FileUploadAnswerIn"]
    )
    types["FileUploadAnswerOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "fileId": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadAnswerOut"])
    types["DateQuestionIn"] = t.struct(
        {"includeYear": t.boolean().optional(), "includeTime": t.boolean().optional()}
    ).named(renames["DateQuestionIn"])
    types["DateQuestionOut"] = t.struct(
        {
            "includeYear": t.boolean().optional(),
            "includeTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateQuestionOut"])
    types["VideoLinkIn"] = t.struct(
        {"displayText": t.string(), "youtubeUri": t.string().optional()}
    ).named(renames["VideoLinkIn"])
    types["VideoLinkOut"] = t.struct(
        {
            "displayText": t.string(),
            "youtubeUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoLinkOut"])
    types["ExtraMaterialIn"] = t.struct(
        {
            "video": t.proxy(renames["VideoLinkIn"]).optional(),
            "link": t.proxy(renames["TextLinkIn"]).optional(),
        }
    ).named(renames["ExtraMaterialIn"])
    types["ExtraMaterialOut"] = t.struct(
        {
            "video": t.proxy(renames["VideoLinkOut"]).optional(),
            "link": t.proxy(renames["TextLinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtraMaterialOut"])
    types["FormSettingsIn"] = t.struct(
        {"quizSettings": t.proxy(renames["QuizSettingsIn"]).optional()}
    ).named(renames["FormSettingsIn"])
    types["FormSettingsOut"] = t.struct(
        {
            "quizSettings": t.proxy(renames["QuizSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormSettingsOut"])
    types["TextAnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswerIn"]
    )
    types["TextAnswerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswerOut"])
    types["MediaPropertiesIn"] = t.struct(
        {"alignment": t.string().optional(), "width": t.integer().optional()}
    ).named(renames["MediaPropertiesIn"])
    types["MediaPropertiesOut"] = t.struct(
        {
            "alignment": t.string().optional(),
            "width": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaPropertiesOut"])
    types["VideoIn"] = t.struct(
        {
            "youtubeUri": t.string(),
            "properties": t.proxy(renames["MediaPropertiesIn"]).optional(),
        }
    ).named(renames["VideoIn"])
    types["VideoOut"] = t.struct(
        {
            "youtubeUri": t.string(),
            "properties": t.proxy(renames["MediaPropertiesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOut"])
    types["CreateWatchRequestIn"] = t.struct(
        {"watchId": t.string().optional(), "watch": t.proxy(renames["WatchIn"])}
    ).named(renames["CreateWatchRequestIn"])
    types["CreateWatchRequestOut"] = t.struct(
        {
            "watchId": t.string().optional(),
            "watch": t.proxy(renames["WatchOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateWatchRequestOut"])
    types["QuestionGroupItemIn"] = t.struct(
        {
            "questions": t.array(t.proxy(renames["QuestionIn"])),
            "grid": t.proxy(renames["GridIn"]).optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["QuestionGroupItemIn"])
    types["QuestionGroupItemOut"] = t.struct(
        {
            "questions": t.array(t.proxy(renames["QuestionOut"])),
            "grid": t.proxy(renames["GridOut"]).optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionGroupItemOut"])
    types["ResponseIn"] = t.struct(
        {"createItem": t.proxy(renames["CreateItemResponseIn"]).optional()}
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createItem": t.proxy(renames["CreateItemResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["ImageItemIn"] = t.struct({"image": t.proxy(renames["ImageIn"])}).named(
        renames["ImageItemIn"]
    )
    types["ImageItemOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageItemOut"])
    types["CreateItemResponseIn"] = t.struct(
        {"itemId": t.string().optional(), "questionId": t.array(t.string()).optional()}
    ).named(renames["CreateItemResponseIn"])
    types["CreateItemResponseOut"] = t.struct(
        {
            "itemId": t.string().optional(),
            "questionId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateItemResponseOut"])
    types["InfoIn"] = t.struct(
        {"description": t.string().optional(), "title": t.string()}
    ).named(renames["InfoIn"])
    types["InfoOut"] = t.struct(
        {
            "documentTitle": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoOut"])
    types["DeleteItemRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"])}
    ).named(renames["DeleteItemRequestIn"])
    types["DeleteItemRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteItemRequestOut"])
    types["FormIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemIn"])),
            "settings": t.proxy(renames["FormSettingsIn"]).optional(),
            "info": t.proxy(renames["InfoIn"]),
        }
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])),
            "responderUri": t.string().optional(),
            "formId": t.string().optional(),
            "linkedSheetId": t.string().optional(),
            "revisionId": t.string().optional(),
            "settings": t.proxy(renames["FormSettingsOut"]).optional(),
            "info": t.proxy(renames["InfoOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
    types["UpdateItemRequestIn"] = t.struct(
        {
            "item": t.proxy(renames["ItemIn"]),
            "updateMask": t.string(),
            "location": t.proxy(renames["LocationIn"]),
        }
    ).named(renames["UpdateItemRequestIn"])
    types["UpdateItemRequestOut"] = t.struct(
        {
            "item": t.proxy(renames["ItemOut"]),
            "updateMask": t.string(),
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateItemRequestOut"])
    types["GradeIn"] = t.struct({"_": t.string().optional()}).named(renames["GradeIn"])
    types["GradeOut"] = t.struct(
        {
            "correct": t.boolean().optional(),
            "score": t.number().optional(),
            "feedback": t.proxy(renames["FeedbackOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeOut"])
    types["WatchIn"] = t.struct(
        {"eventType": t.string(), "target": t.proxy(renames["WatchTargetIn"])}
    ).named(renames["WatchIn"])
    types["WatchOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "errorType": t.string().optional(),
            "eventType": t.string(),
            "id": t.string().optional(),
            "target": t.proxy(renames["WatchTargetOut"]),
            "state": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchOut"])
    types["WatchTargetIn"] = t.struct(
        {"topic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["WatchTargetIn"])
    types["WatchTargetOut"] = t.struct(
        {
            "topic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchTargetOut"])
    types["QuestionItemIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "question": t.proxy(renames["QuestionIn"]),
        }
    ).named(renames["QuestionItemIn"])
    types["QuestionItemOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "question": t.proxy(renames["QuestionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionItemOut"])
    types["ListWatchesResponseIn"] = t.struct(
        {"watches": t.array(t.proxy(renames["WatchIn"])).optional()}
    ).named(renames["ListWatchesResponseIn"])
    types["ListWatchesResponseOut"] = t.struct(
        {
            "watches": t.array(t.proxy(renames["WatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWatchesResponseOut"])
    types["CloudPubsubTopicIn"] = t.struct({"topicName": t.string()}).named(
        renames["CloudPubsubTopicIn"]
    )
    types["CloudPubsubTopicOut"] = t.struct(
        {"topicName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudPubsubTopicOut"])
    types["CorrectAnswersIn"] = t.struct(
        {"answers": t.array(t.proxy(renames["CorrectAnswerIn"])).optional()}
    ).named(renames["CorrectAnswersIn"])
    types["CorrectAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["CorrectAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorrectAnswersOut"])
    types["ListFormResponsesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "responses": t.array(t.proxy(renames["FormResponseIn"])).optional(),
        }
    ).named(renames["ListFormResponsesResponseIn"])
    types["ListFormResponsesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "responses": t.array(t.proxy(renames["FormResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFormResponsesResponseOut"])
    types["RenewWatchRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenewWatchRequestIn"]
    )
    types["RenewWatchRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RenewWatchRequestOut"])
    types["LocationIn"] = t.struct({"index": t.integer().optional()}).named(
        renames["LocationIn"]
    )
    types["LocationOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RowQuestionIn"] = t.struct({"title": t.string()}).named(
        renames["RowQuestionIn"]
    )
    types["RowQuestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RowQuestionOut"])
    types["BatchUpdateFormResponseIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
        }
    ).named(renames["BatchUpdateFormResponseIn"])
    types["BatchUpdateFormResponseOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateFormResponseOut"])
    types["PageBreakItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PageBreakItemIn"]
    )
    types["PageBreakItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PageBreakItemOut"])
    types["TextLinkIn"] = t.struct(
        {"uri": t.string(), "displayText": t.string()}
    ).named(renames["TextLinkIn"])
    types["TextLinkOut"] = t.struct(
        {
            "uri": t.string(),
            "displayText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextLinkOut"])
    types["FileUploadQuestionIn"] = t.struct(
        {
            "folderId": t.string(),
            "types": t.array(t.string()).optional(),
            "maxFileSize": t.string().optional(),
            "maxFiles": t.integer().optional(),
        }
    ).named(renames["FileUploadQuestionIn"])
    types["FileUploadQuestionOut"] = t.struct(
        {
            "folderId": t.string(),
            "types": t.array(t.string()).optional(),
            "maxFileSize": t.string().optional(),
            "maxFiles": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadQuestionOut"])
    types["ItemIn"] = t.struct(
        {
            "questionGroupItem": t.proxy(renames["QuestionGroupItemIn"]).optional(),
            "itemId": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemIn"]).optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemIn"]).optional(),
            "questionItem": t.proxy(renames["QuestionItemIn"]).optional(),
            "videoItem": t.proxy(renames["VideoItemIn"]).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "textItem": t.proxy(renames["TextItemIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "questionGroupItem": t.proxy(renames["QuestionGroupItemOut"]).optional(),
            "itemId": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemOut"]).optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemOut"]).optional(),
            "questionItem": t.proxy(renames["QuestionItemOut"]).optional(),
            "videoItem": t.proxy(renames["VideoItemOut"]).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "textItem": t.proxy(renames["TextItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["WriteControlIn"] = t.struct(
        {
            "targetRevisionId": t.string().optional(),
            "requiredRevisionId": t.string().optional(),
        }
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "targetRevisionId": t.string().optional(),
            "requiredRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
    types["VideoItemIn"] = t.struct(
        {"video": t.proxy(renames["VideoIn"]), "caption": t.string().optional()}
    ).named(renames["VideoItemIn"])
    types["VideoItemOut"] = t.struct(
        {
            "video": t.proxy(renames["VideoOut"]),
            "caption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoItemOut"])
    types["FeedbackIn"] = t.struct(
        {
            "text": t.string(),
            "material": t.array(t.proxy(renames["ExtraMaterialIn"])).optional(),
        }
    ).named(renames["FeedbackIn"])
    types["FeedbackOut"] = t.struct(
        {
            "text": t.string(),
            "material": t.array(t.proxy(renames["ExtraMaterialOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedbackOut"])
    types["QuizSettingsIn"] = t.struct({"isQuiz": t.boolean().optional()}).named(
        renames["QuizSettingsIn"]
    )
    types["QuizSettingsOut"] = t.struct(
        {
            "isQuiz": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuizSettingsOut"])
    types["GridIn"] = t.struct(
        {
            "columns": t.proxy(renames["ChoiceQuestionIn"]),
            "shuffleQuestions": t.boolean().optional(),
        }
    ).named(renames["GridIn"])
    types["GridOut"] = t.struct(
        {
            "columns": t.proxy(renames["ChoiceQuestionOut"]),
            "shuffleQuestions": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridOut"])
    types["FileUploadAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FileUploadAnswersIn"]
    )
    types["FileUploadAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["FileUploadAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadAnswersOut"])
    types["UpdateSettingsRequestIn"] = t.struct(
        {"updateMask": t.string(), "settings": t.proxy(renames["FormSettingsIn"])}
    ).named(renames["UpdateSettingsRequestIn"])
    types["UpdateSettingsRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "settings": t.proxy(renames["FormSettingsOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSettingsRequestOut"])
    types["UpdateFormInfoRequestIn"] = t.struct(
        {"updateMask": t.string(), "info": t.proxy(renames["InfoIn"]).optional()}
    ).named(renames["UpdateFormInfoRequestIn"])
    types["UpdateFormInfoRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "info": t.proxy(renames["InfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFormInfoRequestOut"])
    types["CreateItemRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"]), "item": t.proxy(renames["ItemIn"])}
    ).named(renames["CreateItemRequestIn"])
    types["CreateItemRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "item": t.proxy(renames["ItemOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateItemRequestOut"])

    functions = {}
    functions["formsGet"] = forms.post(
        "v1/forms",
        t.struct(
            {
                "items": t.array(t.proxy(renames["ItemIn"])),
                "settings": t.proxy(renames["FormSettingsIn"]).optional(),
                "info": t.proxy(renames["InfoIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsBatchUpdate"] = forms.post(
        "v1/forms",
        t.struct(
            {
                "items": t.array(t.proxy(renames["ItemIn"])),
                "settings": t.proxy(renames["FormSettingsIn"]).optional(),
                "info": t.proxy(renames["InfoIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsCreate"] = forms.post(
        "v1/forms",
        t.struct(
            {
                "items": t.array(t.proxy(renames["ItemIn"])),
                "settings": t.proxy(renames["FormSettingsIn"]).optional(),
                "info": t.proxy(renames["InfoIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsResponsesList"] = forms.get(
        "v1/forms/{formId}/responses/{responseId}",
        t.struct(
            {
                "formId": t.string(),
                "responseId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsResponsesGet"] = forms.get(
        "v1/forms/{formId}/responses/{responseId}",
        t.struct(
            {
                "formId": t.string(),
                "responseId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesList"] = forms.post(
        "v1/forms/{formId}/watches/{watchId}:renew",
        t.struct(
            {
                "formId": t.string(),
                "watchId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesCreate"] = forms.post(
        "v1/forms/{formId}/watches/{watchId}:renew",
        t.struct(
            {
                "formId": t.string(),
                "watchId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesDelete"] = forms.post(
        "v1/forms/{formId}/watches/{watchId}:renew",
        t.struct(
            {
                "formId": t.string(),
                "watchId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesRenew"] = forms.post(
        "v1/forms/{formId}/watches/{watchId}:renew",
        t.struct(
            {
                "formId": t.string(),
                "watchId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="forms", renames=renames, types=Box(types), functions=Box(functions)
    )
