from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_forms() -> Import:
    forms = HTTPRuntime("https://forms.googleapis.com/")

    renames = {
        "ErrorResponse": "_forms_1_ErrorResponse",
        "FeedbackIn": "_forms_2_FeedbackIn",
        "FeedbackOut": "_forms_3_FeedbackOut",
        "QuestionItemIn": "_forms_4_QuestionItemIn",
        "QuestionItemOut": "_forms_5_QuestionItemOut",
        "LocationIn": "_forms_6_LocationIn",
        "LocationOut": "_forms_7_LocationOut",
        "InfoIn": "_forms_8_InfoIn",
        "InfoOut": "_forms_9_InfoOut",
        "ExtraMaterialIn": "_forms_10_ExtraMaterialIn",
        "ExtraMaterialOut": "_forms_11_ExtraMaterialOut",
        "RequestIn": "_forms_12_RequestIn",
        "RequestOut": "_forms_13_RequestOut",
        "ScaleQuestionIn": "_forms_14_ScaleQuestionIn",
        "ScaleQuestionOut": "_forms_15_ScaleQuestionOut",
        "DateQuestionIn": "_forms_16_DateQuestionIn",
        "DateQuestionOut": "_forms_17_DateQuestionOut",
        "TextItemIn": "_forms_18_TextItemIn",
        "TextItemOut": "_forms_19_TextItemOut",
        "VideoItemIn": "_forms_20_VideoItemIn",
        "VideoItemOut": "_forms_21_VideoItemOut",
        "ResponseIn": "_forms_22_ResponseIn",
        "ResponseOut": "_forms_23_ResponseOut",
        "GradingIn": "_forms_24_GradingIn",
        "GradingOut": "_forms_25_GradingOut",
        "ImageIn": "_forms_26_ImageIn",
        "ImageOut": "_forms_27_ImageOut",
        "FormResponseIn": "_forms_28_FormResponseIn",
        "FormResponseOut": "_forms_29_FormResponseOut",
        "ChoiceQuestionIn": "_forms_30_ChoiceQuestionIn",
        "ChoiceQuestionOut": "_forms_31_ChoiceQuestionOut",
        "RenewWatchRequestIn": "_forms_32_RenewWatchRequestIn",
        "RenewWatchRequestOut": "_forms_33_RenewWatchRequestOut",
        "CreateWatchRequestIn": "_forms_34_CreateWatchRequestIn",
        "CreateWatchRequestOut": "_forms_35_CreateWatchRequestOut",
        "QuizSettingsIn": "_forms_36_QuizSettingsIn",
        "QuizSettingsOut": "_forms_37_QuizSettingsOut",
        "CreateItemRequestIn": "_forms_38_CreateItemRequestIn",
        "CreateItemRequestOut": "_forms_39_CreateItemRequestOut",
        "TimeQuestionIn": "_forms_40_TimeQuestionIn",
        "TimeQuestionOut": "_forms_41_TimeQuestionOut",
        "UpdateSettingsRequestIn": "_forms_42_UpdateSettingsRequestIn",
        "UpdateSettingsRequestOut": "_forms_43_UpdateSettingsRequestOut",
        "VideoLinkIn": "_forms_44_VideoLinkIn",
        "VideoLinkOut": "_forms_45_VideoLinkOut",
        "UpdateItemRequestIn": "_forms_46_UpdateItemRequestIn",
        "UpdateItemRequestOut": "_forms_47_UpdateItemRequestOut",
        "FileUploadAnswersIn": "_forms_48_FileUploadAnswersIn",
        "FileUploadAnswersOut": "_forms_49_FileUploadAnswersOut",
        "CorrectAnswersIn": "_forms_50_CorrectAnswersIn",
        "CorrectAnswersOut": "_forms_51_CorrectAnswersOut",
        "CorrectAnswerIn": "_forms_52_CorrectAnswerIn",
        "CorrectAnswerOut": "_forms_53_CorrectAnswerOut",
        "TextAnswersIn": "_forms_54_TextAnswersIn",
        "TextAnswersOut": "_forms_55_TextAnswersOut",
        "QuestionIn": "_forms_56_QuestionIn",
        "QuestionOut": "_forms_57_QuestionOut",
        "TextQuestionIn": "_forms_58_TextQuestionIn",
        "TextQuestionOut": "_forms_59_TextQuestionOut",
        "FormIn": "_forms_60_FormIn",
        "FormOut": "_forms_61_FormOut",
        "TextAnswerIn": "_forms_62_TextAnswerIn",
        "TextAnswerOut": "_forms_63_TextAnswerOut",
        "VideoIn": "_forms_64_VideoIn",
        "VideoOut": "_forms_65_VideoOut",
        "WatchIn": "_forms_66_WatchIn",
        "WatchOut": "_forms_67_WatchOut",
        "MediaPropertiesIn": "_forms_68_MediaPropertiesIn",
        "MediaPropertiesOut": "_forms_69_MediaPropertiesOut",
        "ListWatchesResponseIn": "_forms_70_ListWatchesResponseIn",
        "ListWatchesResponseOut": "_forms_71_ListWatchesResponseOut",
        "GradeIn": "_forms_72_GradeIn",
        "GradeOut": "_forms_73_GradeOut",
        "OptionIn": "_forms_74_OptionIn",
        "OptionOut": "_forms_75_OptionOut",
        "AnswerIn": "_forms_76_AnswerIn",
        "AnswerOut": "_forms_77_AnswerOut",
        "BatchUpdateFormRequestIn": "_forms_78_BatchUpdateFormRequestIn",
        "BatchUpdateFormRequestOut": "_forms_79_BatchUpdateFormRequestOut",
        "EmptyIn": "_forms_80_EmptyIn",
        "EmptyOut": "_forms_81_EmptyOut",
        "DeleteItemRequestIn": "_forms_82_DeleteItemRequestIn",
        "DeleteItemRequestOut": "_forms_83_DeleteItemRequestOut",
        "WriteControlIn": "_forms_84_WriteControlIn",
        "WriteControlOut": "_forms_85_WriteControlOut",
        "CloudPubsubTopicIn": "_forms_86_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_forms_87_CloudPubsubTopicOut",
        "FormSettingsIn": "_forms_88_FormSettingsIn",
        "FormSettingsOut": "_forms_89_FormSettingsOut",
        "QuestionGroupItemIn": "_forms_90_QuestionGroupItemIn",
        "QuestionGroupItemOut": "_forms_91_QuestionGroupItemOut",
        "FileUploadAnswerIn": "_forms_92_FileUploadAnswerIn",
        "FileUploadAnswerOut": "_forms_93_FileUploadAnswerOut",
        "CreateItemResponseIn": "_forms_94_CreateItemResponseIn",
        "CreateItemResponseOut": "_forms_95_CreateItemResponseOut",
        "RowQuestionIn": "_forms_96_RowQuestionIn",
        "RowQuestionOut": "_forms_97_RowQuestionOut",
        "MoveItemRequestIn": "_forms_98_MoveItemRequestIn",
        "MoveItemRequestOut": "_forms_99_MoveItemRequestOut",
        "ImageItemIn": "_forms_100_ImageItemIn",
        "ImageItemOut": "_forms_101_ImageItemOut",
        "TextLinkIn": "_forms_102_TextLinkIn",
        "TextLinkOut": "_forms_103_TextLinkOut",
        "BatchUpdateFormResponseIn": "_forms_104_BatchUpdateFormResponseIn",
        "BatchUpdateFormResponseOut": "_forms_105_BatchUpdateFormResponseOut",
        "UpdateFormInfoRequestIn": "_forms_106_UpdateFormInfoRequestIn",
        "UpdateFormInfoRequestOut": "_forms_107_UpdateFormInfoRequestOut",
        "WatchTargetIn": "_forms_108_WatchTargetIn",
        "WatchTargetOut": "_forms_109_WatchTargetOut",
        "FileUploadQuestionIn": "_forms_110_FileUploadQuestionIn",
        "FileUploadQuestionOut": "_forms_111_FileUploadQuestionOut",
        "ItemIn": "_forms_112_ItemIn",
        "ItemOut": "_forms_113_ItemOut",
        "GridIn": "_forms_114_GridIn",
        "GridOut": "_forms_115_GridOut",
        "ListFormResponsesResponseIn": "_forms_116_ListFormResponsesResponseIn",
        "ListFormResponsesResponseOut": "_forms_117_ListFormResponsesResponseOut",
        "PageBreakItemIn": "_forms_118_PageBreakItemIn",
        "PageBreakItemOut": "_forms_119_PageBreakItemOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FeedbackIn"] = t.struct(
        {
            "material": t.array(t.proxy(renames["ExtraMaterialIn"])).optional(),
            "text": t.string(),
        }
    ).named(renames["FeedbackIn"])
    types["FeedbackOut"] = t.struct(
        {
            "material": t.array(t.proxy(renames["ExtraMaterialOut"])).optional(),
            "text": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeedbackOut"])
    types["QuestionItemIn"] = t.struct(
        {
            "question": t.proxy(renames["QuestionIn"]),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["QuestionItemIn"])
    types["QuestionItemOut"] = t.struct(
        {
            "question": t.proxy(renames["QuestionOut"]),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionItemOut"])
    types["LocationIn"] = t.struct({"index": t.integer().optional()}).named(
        renames["LocationIn"]
    )
    types["LocationOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["InfoIn"] = t.struct(
        {"title": t.string(), "description": t.string().optional()}
    ).named(renames["InfoIn"])
    types["InfoOut"] = t.struct(
        {
            "title": t.string(),
            "description": t.string().optional(),
            "documentTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoOut"])
    types["ExtraMaterialIn"] = t.struct(
        {
            "link": t.proxy(renames["TextLinkIn"]).optional(),
            "video": t.proxy(renames["VideoLinkIn"]).optional(),
        }
    ).named(renames["ExtraMaterialIn"])
    types["ExtraMaterialOut"] = t.struct(
        {
            "link": t.proxy(renames["TextLinkOut"]).optional(),
            "video": t.proxy(renames["VideoLinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtraMaterialOut"])
    types["RequestIn"] = t.struct(
        {
            "moveItem": t.proxy(renames["MoveItemRequestIn"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestIn"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestIn"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestIn"]).optional(),
            "deleteItem": t.proxy(renames["DeleteItemRequestIn"]).optional(),
            "updateItem": t.proxy(renames["UpdateItemRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "moveItem": t.proxy(renames["MoveItemRequestOut"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestOut"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestOut"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestOut"]).optional(),
            "deleteItem": t.proxy(renames["DeleteItemRequestOut"]).optional(),
            "updateItem": t.proxy(renames["UpdateItemRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["ScaleQuestionIn"] = t.struct(
        {
            "high": t.integer(),
            "highLabel": t.string().optional(),
            "lowLabel": t.string().optional(),
            "low": t.integer(),
        }
    ).named(renames["ScaleQuestionIn"])
    types["ScaleQuestionOut"] = t.struct(
        {
            "high": t.integer(),
            "highLabel": t.string().optional(),
            "lowLabel": t.string().optional(),
            "low": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScaleQuestionOut"])
    types["DateQuestionIn"] = t.struct(
        {"includeTime": t.boolean().optional(), "includeYear": t.boolean().optional()}
    ).named(renames["DateQuestionIn"])
    types["DateQuestionOut"] = t.struct(
        {
            "includeTime": t.boolean().optional(),
            "includeYear": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateQuestionOut"])
    types["TextItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextItemIn"]
    )
    types["TextItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextItemOut"])
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
    types["ResponseIn"] = t.struct(
        {"createItem": t.proxy(renames["CreateItemResponseIn"]).optional()}
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createItem": t.proxy(renames["CreateItemResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["GradingIn"] = t.struct(
        {
            "whenWrong": t.proxy(renames["FeedbackIn"]).optional(),
            "pointValue": t.integer(),
            "whenRight": t.proxy(renames["FeedbackIn"]).optional(),
            "correctAnswers": t.proxy(renames["CorrectAnswersIn"]),
            "generalFeedback": t.proxy(renames["FeedbackIn"]).optional(),
        }
    ).named(renames["GradingIn"])
    types["GradingOut"] = t.struct(
        {
            "whenWrong": t.proxy(renames["FeedbackOut"]).optional(),
            "pointValue": t.integer(),
            "whenRight": t.proxy(renames["FeedbackOut"]).optional(),
            "correctAnswers": t.proxy(renames["CorrectAnswersOut"]),
            "generalFeedback": t.proxy(renames["FeedbackOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradingOut"])
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
            "altText": t.string().optional(),
            "properties": t.proxy(renames["MediaPropertiesOut"]).optional(),
            "contentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
    types["FormResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FormResponseIn"]
    )
    types["FormResponseOut"] = t.struct(
        {
            "totalScore": t.number().optional(),
            "answers": t.struct({"_": t.string().optional()}).optional(),
            "responseId": t.string().optional(),
            "respondentEmail": t.string().optional(),
            "formId": t.string().optional(),
            "lastSubmittedTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormResponseOut"])
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
    types["RenewWatchRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenewWatchRequestIn"]
    )
    types["RenewWatchRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RenewWatchRequestOut"])
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
    types["QuizSettingsIn"] = t.struct({"isQuiz": t.boolean().optional()}).named(
        renames["QuizSettingsIn"]
    )
    types["QuizSettingsOut"] = t.struct(
        {
            "isQuiz": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuizSettingsOut"])
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
    types["TimeQuestionIn"] = t.struct({"duration": t.boolean().optional()}).named(
        renames["TimeQuestionIn"]
    )
    types["TimeQuestionOut"] = t.struct(
        {
            "duration": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeQuestionOut"])
    types["UpdateSettingsRequestIn"] = t.struct(
        {"settings": t.proxy(renames["FormSettingsIn"]), "updateMask": t.string()}
    ).named(renames["UpdateSettingsRequestIn"])
    types["UpdateSettingsRequestOut"] = t.struct(
        {
            "settings": t.proxy(renames["FormSettingsOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateSettingsRequestOut"])
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
    types["UpdateItemRequestIn"] = t.struct(
        {
            "location": t.proxy(renames["LocationIn"]),
            "item": t.proxy(renames["ItemIn"]),
            "updateMask": t.string(),
        }
    ).named(renames["UpdateItemRequestIn"])
    types["UpdateItemRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "item": t.proxy(renames["ItemOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateItemRequestOut"])
    types["FileUploadAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FileUploadAnswersIn"]
    )
    types["FileUploadAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["FileUploadAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadAnswersOut"])
    types["CorrectAnswersIn"] = t.struct(
        {"answers": t.array(t.proxy(renames["CorrectAnswerIn"])).optional()}
    ).named(renames["CorrectAnswersIn"])
    types["CorrectAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["CorrectAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorrectAnswersOut"])
    types["CorrectAnswerIn"] = t.struct({"value": t.string()}).named(
        renames["CorrectAnswerIn"]
    )
    types["CorrectAnswerOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CorrectAnswerOut"])
    types["TextAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswersIn"]
    )
    types["TextAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["TextAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswersOut"])
    types["QuestionIn"] = t.struct(
        {
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionIn"]).optional(),
            "rowQuestion": t.proxy(renames["RowQuestionIn"]).optional(),
            "grading": t.proxy(renames["GradingIn"]).optional(),
            "textQuestion": t.proxy(renames["TextQuestionIn"]).optional(),
            "required": t.boolean().optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionIn"]).optional(),
            "dateQuestion": t.proxy(renames["DateQuestionIn"]).optional(),
            "questionId": t.string().optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionIn"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionIn"]).optional(),
        }
    ).named(renames["QuestionIn"])
    types["QuestionOut"] = t.struct(
        {
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionOut"]).optional(),
            "rowQuestion": t.proxy(renames["RowQuestionOut"]).optional(),
            "grading": t.proxy(renames["GradingOut"]).optional(),
            "textQuestion": t.proxy(renames["TextQuestionOut"]).optional(),
            "required": t.boolean().optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionOut"]).optional(),
            "dateQuestion": t.proxy(renames["DateQuestionOut"]).optional(),
            "questionId": t.string().optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionOut"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionOut"])
    types["TextQuestionIn"] = t.struct({"paragraph": t.boolean().optional()}).named(
        renames["TextQuestionIn"]
    )
    types["TextQuestionOut"] = t.struct(
        {
            "paragraph": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextQuestionOut"])
    types["FormIn"] = t.struct(
        {
            "settings": t.proxy(renames["FormSettingsIn"]).optional(),
            "info": t.proxy(renames["InfoIn"]),
            "items": t.array(t.proxy(renames["ItemIn"])),
        }
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "settings": t.proxy(renames["FormSettingsOut"]).optional(),
            "formId": t.string().optional(),
            "info": t.proxy(renames["InfoOut"]),
            "items": t.array(t.proxy(renames["ItemOut"])),
            "responderUri": t.string().optional(),
            "linkedSheetId": t.string().optional(),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
    types["TextAnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswerIn"]
    )
    types["TextAnswerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswerOut"])
    types["VideoIn"] = t.struct(
        {
            "properties": t.proxy(renames["MediaPropertiesIn"]).optional(),
            "youtubeUri": t.string(),
        }
    ).named(renames["VideoIn"])
    types["VideoOut"] = t.struct(
        {
            "properties": t.proxy(renames["MediaPropertiesOut"]).optional(),
            "youtubeUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoOut"])
    types["WatchIn"] = t.struct(
        {"target": t.proxy(renames["WatchTargetIn"]), "eventType": t.string()}
    ).named(renames["WatchIn"])
    types["WatchOut"] = t.struct(
        {
            "target": t.proxy(renames["WatchTargetOut"]),
            "expireTime": t.string().optional(),
            "id": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "errorType": t.string().optional(),
            "eventType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchOut"])
    types["MediaPropertiesIn"] = t.struct(
        {"width": t.integer().optional(), "alignment": t.string().optional()}
    ).named(renames["MediaPropertiesIn"])
    types["MediaPropertiesOut"] = t.struct(
        {
            "width": t.integer().optional(),
            "alignment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaPropertiesOut"])
    types["ListWatchesResponseIn"] = t.struct(
        {"watches": t.array(t.proxy(renames["WatchIn"])).optional()}
    ).named(renames["ListWatchesResponseIn"])
    types["ListWatchesResponseOut"] = t.struct(
        {
            "watches": t.array(t.proxy(renames["WatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWatchesResponseOut"])
    types["GradeIn"] = t.struct({"_": t.string().optional()}).named(renames["GradeIn"])
    types["GradeOut"] = t.struct(
        {
            "score": t.number().optional(),
            "feedback": t.proxy(renames["FeedbackOut"]).optional(),
            "correct": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeOut"])
    types["OptionIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "goToSectionId": t.string().optional(),
            "goToAction": t.string().optional(),
            "isOther": t.boolean().optional(),
            "value": t.string(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "goToSectionId": t.string().optional(),
            "goToAction": t.string().optional(),
            "isOther": t.boolean().optional(),
            "value": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
    types["AnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnswerIn"]
    )
    types["AnswerOut"] = t.struct(
        {
            "textAnswers": t.proxy(renames["TextAnswersOut"]).optional(),
            "grade": t.proxy(renames["GradeOut"]).optional(),
            "questionId": t.string().optional(),
            "fileUploadAnswers": t.proxy(renames["FileUploadAnswersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnswerOut"])
    types["BatchUpdateFormRequestIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "includeFormInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])),
        }
    ).named(renames["BatchUpdateFormRequestIn"])
    types["BatchUpdateFormRequestOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "includeFormInResponse": t.boolean().optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateFormRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DeleteItemRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"])}
    ).named(renames["DeleteItemRequestIn"])
    types["DeleteItemRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteItemRequestOut"])
    types["WriteControlIn"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "targetRevisionId": t.string().optional(),
        }
    ).named(renames["WriteControlIn"])
    types["WriteControlOut"] = t.struct(
        {
            "requiredRevisionId": t.string().optional(),
            "targetRevisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WriteControlOut"])
    types["CloudPubsubTopicIn"] = t.struct({"topicName": t.string()}).named(
        renames["CloudPubsubTopicIn"]
    )
    types["CloudPubsubTopicOut"] = t.struct(
        {"topicName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudPubsubTopicOut"])
    types["FormSettingsIn"] = t.struct(
        {"quizSettings": t.proxy(renames["QuizSettingsIn"]).optional()}
    ).named(renames["FormSettingsIn"])
    types["FormSettingsOut"] = t.struct(
        {
            "quizSettings": t.proxy(renames["QuizSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormSettingsOut"])
    types["QuestionGroupItemIn"] = t.struct(
        {
            "questions": t.array(t.proxy(renames["QuestionIn"])),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "grid": t.proxy(renames["GridIn"]).optional(),
        }
    ).named(renames["QuestionGroupItemIn"])
    types["QuestionGroupItemOut"] = t.struct(
        {
            "questions": t.array(t.proxy(renames["QuestionOut"])),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "grid": t.proxy(renames["GridOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionGroupItemOut"])
    types["FileUploadAnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FileUploadAnswerIn"]
    )
    types["FileUploadAnswerOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "fileName": t.string().optional(),
            "fileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadAnswerOut"])
    types["CreateItemResponseIn"] = t.struct(
        {"questionId": t.array(t.string()).optional(), "itemId": t.string().optional()}
    ).named(renames["CreateItemResponseIn"])
    types["CreateItemResponseOut"] = t.struct(
        {
            "questionId": t.array(t.string()).optional(),
            "itemId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateItemResponseOut"])
    types["RowQuestionIn"] = t.struct({"title": t.string()}).named(
        renames["RowQuestionIn"]
    )
    types["RowQuestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RowQuestionOut"])
    types["MoveItemRequestIn"] = t.struct(
        {
            "newLocation": t.proxy(renames["LocationIn"]),
            "originalLocation": t.proxy(renames["LocationIn"]),
        }
    ).named(renames["MoveItemRequestIn"])
    types["MoveItemRequestOut"] = t.struct(
        {
            "newLocation": t.proxy(renames["LocationOut"]),
            "originalLocation": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveItemRequestOut"])
    types["ImageItemIn"] = t.struct({"image": t.proxy(renames["ImageIn"])}).named(
        renames["ImageItemIn"]
    )
    types["ImageItemOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageItemOut"])
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
    types["BatchUpdateFormResponseIn"] = t.struct(
        {
            "form": t.proxy(renames["FormIn"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
        }
    ).named(renames["BatchUpdateFormResponseIn"])
    types["BatchUpdateFormResponseOut"] = t.struct(
        {
            "form": t.proxy(renames["FormOut"]).optional(),
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateFormResponseOut"])
    types["UpdateFormInfoRequestIn"] = t.struct(
        {"info": t.proxy(renames["InfoIn"]).optional(), "updateMask": t.string()}
    ).named(renames["UpdateFormInfoRequestIn"])
    types["UpdateFormInfoRequestOut"] = t.struct(
        {
            "info": t.proxy(renames["InfoOut"]).optional(),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFormInfoRequestOut"])
    types["WatchTargetIn"] = t.struct(
        {"topic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["WatchTargetIn"])
    types["WatchTargetOut"] = t.struct(
        {
            "topic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchTargetOut"])
    types["FileUploadQuestionIn"] = t.struct(
        {
            "folderId": t.string(),
            "maxFiles": t.integer().optional(),
            "types": t.array(t.string()).optional(),
            "maxFileSize": t.string().optional(),
        }
    ).named(renames["FileUploadQuestionIn"])
    types["FileUploadQuestionOut"] = t.struct(
        {
            "folderId": t.string(),
            "maxFiles": t.integer().optional(),
            "types": t.array(t.string()).optional(),
            "maxFileSize": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadQuestionOut"])
    types["ItemIn"] = t.struct(
        {
            "questionItem": t.proxy(renames["QuestionItemIn"]).optional(),
            "itemId": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemIn"]).optional(),
            "description": t.string().optional(),
            "videoItem": t.proxy(renames["VideoItemIn"]).optional(),
            "title": t.string().optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemIn"]).optional(),
            "questionGroupItem": t.proxy(renames["QuestionGroupItemIn"]).optional(),
            "textItem": t.proxy(renames["TextItemIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "questionItem": t.proxy(renames["QuestionItemOut"]).optional(),
            "itemId": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemOut"]).optional(),
            "description": t.string().optional(),
            "videoItem": t.proxy(renames["VideoItemOut"]).optional(),
            "title": t.string().optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemOut"]).optional(),
            "questionGroupItem": t.proxy(renames["QuestionGroupItemOut"]).optional(),
            "textItem": t.proxy(renames["TextItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
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
    types["ListFormResponsesResponseIn"] = t.struct(
        {
            "responses": t.array(t.proxy(renames["FormResponseIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFormResponsesResponseIn"])
    types["ListFormResponsesResponseOut"] = t.struct(
        {
            "responses": t.array(t.proxy(renames["FormResponseOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFormResponsesResponseOut"])
    types["PageBreakItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PageBreakItemIn"]
    )
    types["PageBreakItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PageBreakItemOut"])

    functions = {}
    functions["formsGet"] = forms.post(
        "v1/forms/{formId}:batchUpdate",
        t.struct(
            {
                "formId": t.string(),
                "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
                "includeFormInResponse": t.boolean().optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateFormResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsCreate"] = forms.post(
        "v1/forms/{formId}:batchUpdate",
        t.struct(
            {
                "formId": t.string(),
                "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
                "includeFormInResponse": t.boolean().optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateFormResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsBatchUpdate"] = forms.post(
        "v1/forms/{formId}:batchUpdate",
        t.struct(
            {
                "formId": t.string(),
                "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
                "includeFormInResponse": t.boolean().optional(),
                "requests": t.array(t.proxy(renames["RequestIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BatchUpdateFormResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesDelete"] = forms.get(
        "v1/forms/{formId}/watches",
        t.struct({"formId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListWatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesRenew"] = forms.get(
        "v1/forms/{formId}/watches",
        t.struct({"formId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListWatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesCreate"] = forms.get(
        "v1/forms/{formId}/watches",
        t.struct({"formId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListWatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesList"] = forms.get(
        "v1/forms/{formId}/watches",
        t.struct({"formId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListWatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsResponsesList"] = forms.get(
        "v1/forms/{formId}/responses/{responseId}",
        t.struct(
            {
                "responseId": t.string(),
                "formId": t.string(),
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
                "responseId": t.string(),
                "formId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="forms", renames=renames, types=Box(types), functions=Box(functions)
    )
