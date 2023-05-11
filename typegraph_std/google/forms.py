from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_forms() -> Import:
    forms = HTTPRuntime("https://forms.googleapis.com/")

    renames = {
        "ErrorResponse": "_forms_1_ErrorResponse",
        "ImageIn": "_forms_2_ImageIn",
        "ImageOut": "_forms_3_ImageOut",
        "OptionIn": "_forms_4_OptionIn",
        "OptionOut": "_forms_5_OptionOut",
        "FileUploadQuestionIn": "_forms_6_FileUploadQuestionIn",
        "FileUploadQuestionOut": "_forms_7_FileUploadQuestionOut",
        "CorrectAnswersIn": "_forms_8_CorrectAnswersIn",
        "CorrectAnswersOut": "_forms_9_CorrectAnswersOut",
        "UpdateSettingsRequestIn": "_forms_10_UpdateSettingsRequestIn",
        "UpdateSettingsRequestOut": "_forms_11_UpdateSettingsRequestOut",
        "TextQuestionIn": "_forms_12_TextQuestionIn",
        "TextQuestionOut": "_forms_13_TextQuestionOut",
        "QuestionItemIn": "_forms_14_QuestionItemIn",
        "QuestionItemOut": "_forms_15_QuestionItemOut",
        "WatchTargetIn": "_forms_16_WatchTargetIn",
        "WatchTargetOut": "_forms_17_WatchTargetOut",
        "ListWatchesResponseIn": "_forms_18_ListWatchesResponseIn",
        "ListWatchesResponseOut": "_forms_19_ListWatchesResponseOut",
        "TextAnswersIn": "_forms_20_TextAnswersIn",
        "TextAnswersOut": "_forms_21_TextAnswersOut",
        "DateQuestionIn": "_forms_22_DateQuestionIn",
        "DateQuestionOut": "_forms_23_DateQuestionOut",
        "MoveItemRequestIn": "_forms_24_MoveItemRequestIn",
        "MoveItemRequestOut": "_forms_25_MoveItemRequestOut",
        "ImageItemIn": "_forms_26_ImageItemIn",
        "ImageItemOut": "_forms_27_ImageItemOut",
        "QuestionIn": "_forms_28_QuestionIn",
        "QuestionOut": "_forms_29_QuestionOut",
        "BatchUpdateFormRequestIn": "_forms_30_BatchUpdateFormRequestIn",
        "BatchUpdateFormRequestOut": "_forms_31_BatchUpdateFormRequestOut",
        "DeleteItemRequestIn": "_forms_32_DeleteItemRequestIn",
        "DeleteItemRequestOut": "_forms_33_DeleteItemRequestOut",
        "UpdateItemRequestIn": "_forms_34_UpdateItemRequestIn",
        "UpdateItemRequestOut": "_forms_35_UpdateItemRequestOut",
        "UpdateFormInfoRequestIn": "_forms_36_UpdateFormInfoRequestIn",
        "UpdateFormInfoRequestOut": "_forms_37_UpdateFormInfoRequestOut",
        "CreateWatchRequestIn": "_forms_38_CreateWatchRequestIn",
        "CreateWatchRequestOut": "_forms_39_CreateWatchRequestOut",
        "ScaleQuestionIn": "_forms_40_ScaleQuestionIn",
        "ScaleQuestionOut": "_forms_41_ScaleQuestionOut",
        "QuizSettingsIn": "_forms_42_QuizSettingsIn",
        "QuizSettingsOut": "_forms_43_QuizSettingsOut",
        "BatchUpdateFormResponseIn": "_forms_44_BatchUpdateFormResponseIn",
        "BatchUpdateFormResponseOut": "_forms_45_BatchUpdateFormResponseOut",
        "AnswerIn": "_forms_46_AnswerIn",
        "AnswerOut": "_forms_47_AnswerOut",
        "WriteControlIn": "_forms_48_WriteControlIn",
        "WriteControlOut": "_forms_49_WriteControlOut",
        "CreateItemRequestIn": "_forms_50_CreateItemRequestIn",
        "CreateItemRequestOut": "_forms_51_CreateItemRequestOut",
        "CloudPubsubTopicIn": "_forms_52_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_forms_53_CloudPubsubTopicOut",
        "VideoLinkIn": "_forms_54_VideoLinkIn",
        "VideoLinkOut": "_forms_55_VideoLinkOut",
        "EmptyIn": "_forms_56_EmptyIn",
        "EmptyOut": "_forms_57_EmptyOut",
        "GradeIn": "_forms_58_GradeIn",
        "GradeOut": "_forms_59_GradeOut",
        "FormResponseIn": "_forms_60_FormResponseIn",
        "FormResponseOut": "_forms_61_FormResponseOut",
        "ItemIn": "_forms_62_ItemIn",
        "ItemOut": "_forms_63_ItemOut",
        "RequestIn": "_forms_64_RequestIn",
        "RequestOut": "_forms_65_RequestOut",
        "FileUploadAnswerIn": "_forms_66_FileUploadAnswerIn",
        "FileUploadAnswerOut": "_forms_67_FileUploadAnswerOut",
        "GradingIn": "_forms_68_GradingIn",
        "GradingOut": "_forms_69_GradingOut",
        "TextLinkIn": "_forms_70_TextLinkIn",
        "TextLinkOut": "_forms_71_TextLinkOut",
        "VideoIn": "_forms_72_VideoIn",
        "VideoOut": "_forms_73_VideoOut",
        "VideoItemIn": "_forms_74_VideoItemIn",
        "VideoItemOut": "_forms_75_VideoItemOut",
        "ChoiceQuestionIn": "_forms_76_ChoiceQuestionIn",
        "ChoiceQuestionOut": "_forms_77_ChoiceQuestionOut",
        "RowQuestionIn": "_forms_78_RowQuestionIn",
        "RowQuestionOut": "_forms_79_RowQuestionOut",
        "GridIn": "_forms_80_GridIn",
        "GridOut": "_forms_81_GridOut",
        "QuestionGroupItemIn": "_forms_82_QuestionGroupItemIn",
        "QuestionGroupItemOut": "_forms_83_QuestionGroupItemOut",
        "LocationIn": "_forms_84_LocationIn",
        "LocationOut": "_forms_85_LocationOut",
        "CorrectAnswerIn": "_forms_86_CorrectAnswerIn",
        "CorrectAnswerOut": "_forms_87_CorrectAnswerOut",
        "CreateItemResponseIn": "_forms_88_CreateItemResponseIn",
        "CreateItemResponseOut": "_forms_89_CreateItemResponseOut",
        "MediaPropertiesIn": "_forms_90_MediaPropertiesIn",
        "MediaPropertiesOut": "_forms_91_MediaPropertiesOut",
        "ExtraMaterialIn": "_forms_92_ExtraMaterialIn",
        "ExtraMaterialOut": "_forms_93_ExtraMaterialOut",
        "TimeQuestionIn": "_forms_94_TimeQuestionIn",
        "TimeQuestionOut": "_forms_95_TimeQuestionOut",
        "RenewWatchRequestIn": "_forms_96_RenewWatchRequestIn",
        "RenewWatchRequestOut": "_forms_97_RenewWatchRequestOut",
        "FileUploadAnswersIn": "_forms_98_FileUploadAnswersIn",
        "FileUploadAnswersOut": "_forms_99_FileUploadAnswersOut",
        "FormIn": "_forms_100_FormIn",
        "FormOut": "_forms_101_FormOut",
        "ListFormResponsesResponseIn": "_forms_102_ListFormResponsesResponseIn",
        "ListFormResponsesResponseOut": "_forms_103_ListFormResponsesResponseOut",
        "PageBreakItemIn": "_forms_104_PageBreakItemIn",
        "PageBreakItemOut": "_forms_105_PageBreakItemOut",
        "TextItemIn": "_forms_106_TextItemIn",
        "TextItemOut": "_forms_107_TextItemOut",
        "ResponseIn": "_forms_108_ResponseIn",
        "ResponseOut": "_forms_109_ResponseOut",
        "TextAnswerIn": "_forms_110_TextAnswerIn",
        "TextAnswerOut": "_forms_111_TextAnswerOut",
        "FeedbackIn": "_forms_112_FeedbackIn",
        "FeedbackOut": "_forms_113_FeedbackOut",
        "FormSettingsIn": "_forms_114_FormSettingsIn",
        "FormSettingsOut": "_forms_115_FormSettingsOut",
        "WatchIn": "_forms_116_WatchIn",
        "WatchOut": "_forms_117_WatchOut",
        "InfoIn": "_forms_118_InfoIn",
        "InfoOut": "_forms_119_InfoOut",
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
    types["OptionIn"] = t.struct(
        {
            "goToSectionId": t.string().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "isOther": t.boolean().optional(),
            "value": t.string(),
            "goToAction": t.string().optional(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "goToSectionId": t.string().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "isOther": t.boolean().optional(),
            "value": t.string(),
            "goToAction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
    types["FileUploadQuestionIn"] = t.struct(
        {
            "folderId": t.string(),
            "maxFiles": t.integer().optional(),
            "maxFileSize": t.string().optional(),
            "types": t.array(t.string()).optional(),
        }
    ).named(renames["FileUploadQuestionIn"])
    types["FileUploadQuestionOut"] = t.struct(
        {
            "folderId": t.string(),
            "maxFiles": t.integer().optional(),
            "maxFileSize": t.string().optional(),
            "types": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadQuestionOut"])
    types["CorrectAnswersIn"] = t.struct(
        {"answers": t.array(t.proxy(renames["CorrectAnswerIn"])).optional()}
    ).named(renames["CorrectAnswersIn"])
    types["CorrectAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["CorrectAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorrectAnswersOut"])
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
    types["TextQuestionIn"] = t.struct({"paragraph": t.boolean().optional()}).named(
        renames["TextQuestionIn"]
    )
    types["TextQuestionOut"] = t.struct(
        {
            "paragraph": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextQuestionOut"])
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
    types["WatchTargetIn"] = t.struct(
        {"topic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["WatchTargetIn"])
    types["WatchTargetOut"] = t.struct(
        {
            "topic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchTargetOut"])
    types["ListWatchesResponseIn"] = t.struct(
        {"watches": t.array(t.proxy(renames["WatchIn"])).optional()}
    ).named(renames["ListWatchesResponseIn"])
    types["ListWatchesResponseOut"] = t.struct(
        {
            "watches": t.array(t.proxy(renames["WatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWatchesResponseOut"])
    types["TextAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswersIn"]
    )
    types["TextAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["TextAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswersOut"])
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
    types["ImageItemIn"] = t.struct({"image": t.proxy(renames["ImageIn"])}).named(
        renames["ImageItemIn"]
    )
    types["ImageItemOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageItemOut"])
    types["QuestionIn"] = t.struct(
        {
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionIn"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionIn"]).optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionIn"]).optional(),
            "questionId": t.string().optional(),
            "textQuestion": t.proxy(renames["TextQuestionIn"]).optional(),
            "dateQuestion": t.proxy(renames["DateQuestionIn"]).optional(),
            "required": t.boolean().optional(),
            "grading": t.proxy(renames["GradingIn"]).optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionIn"]).optional(),
            "rowQuestion": t.proxy(renames["RowQuestionIn"]).optional(),
        }
    ).named(renames["QuestionIn"])
    types["QuestionOut"] = t.struct(
        {
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionOut"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionOut"]).optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionOut"]).optional(),
            "questionId": t.string().optional(),
            "textQuestion": t.proxy(renames["TextQuestionOut"]).optional(),
            "dateQuestion": t.proxy(renames["DateQuestionOut"]).optional(),
            "required": t.boolean().optional(),
            "grading": t.proxy(renames["GradingOut"]).optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionOut"]).optional(),
            "rowQuestion": t.proxy(renames["RowQuestionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionOut"])
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
    types["DeleteItemRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"])}
    ).named(renames["DeleteItemRequestIn"])
    types["DeleteItemRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteItemRequestOut"])
    types["UpdateItemRequestIn"] = t.struct(
        {
            "item": t.proxy(renames["ItemIn"]),
            "location": t.proxy(renames["LocationIn"]),
            "updateMask": t.string(),
        }
    ).named(renames["UpdateItemRequestIn"])
    types["UpdateItemRequestOut"] = t.struct(
        {
            "item": t.proxy(renames["ItemOut"]),
            "location": t.proxy(renames["LocationOut"]),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateItemRequestOut"])
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
    types["QuizSettingsIn"] = t.struct({"isQuiz": t.boolean().optional()}).named(
        renames["QuizSettingsIn"]
    )
    types["QuizSettingsOut"] = t.struct(
        {
            "isQuiz": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuizSettingsOut"])
    types["BatchUpdateFormResponseIn"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
        }
    ).named(renames["BatchUpdateFormResponseIn"])
    types["BatchUpdateFormResponseOut"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateFormResponseOut"])
    types["AnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AnswerIn"]
    )
    types["AnswerOut"] = t.struct(
        {
            "grade": t.proxy(renames["GradeOut"]).optional(),
            "questionId": t.string().optional(),
            "fileUploadAnswers": t.proxy(renames["FileUploadAnswersOut"]).optional(),
            "textAnswers": t.proxy(renames["TextAnswersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnswerOut"])
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
    types["CreateItemRequestIn"] = t.struct(
        {"item": t.proxy(renames["ItemIn"]), "location": t.proxy(renames["LocationIn"])}
    ).named(renames["CreateItemRequestIn"])
    types["CreateItemRequestOut"] = t.struct(
        {
            "item": t.proxy(renames["ItemOut"]),
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateItemRequestOut"])
    types["CloudPubsubTopicIn"] = t.struct({"topicName": t.string()}).named(
        renames["CloudPubsubTopicIn"]
    )
    types["CloudPubsubTopicOut"] = t.struct(
        {"topicName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudPubsubTopicOut"])
    types["VideoLinkIn"] = t.struct(
        {"youtubeUri": t.string().optional(), "displayText": t.string()}
    ).named(renames["VideoLinkIn"])
    types["VideoLinkOut"] = t.struct(
        {
            "youtubeUri": t.string().optional(),
            "displayText": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VideoLinkOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GradeIn"] = t.struct({"_": t.string().optional()}).named(renames["GradeIn"])
    types["GradeOut"] = t.struct(
        {
            "feedback": t.proxy(renames["FeedbackOut"]).optional(),
            "correct": t.boolean().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeOut"])
    types["FormResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FormResponseIn"]
    )
    types["FormResponseOut"] = t.struct(
        {
            "formId": t.string().optional(),
            "answers": t.struct({"_": t.string().optional()}).optional(),
            "respondentEmail": t.string().optional(),
            "totalScore": t.number().optional(),
            "responseId": t.string().optional(),
            "createTime": t.string().optional(),
            "lastSubmittedTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormResponseOut"])
    types["ItemIn"] = t.struct(
        {
            "questionGroupItem": t.proxy(renames["QuestionGroupItemIn"]).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "videoItem": t.proxy(renames["VideoItemIn"]).optional(),
            "questionItem": t.proxy(renames["QuestionItemIn"]).optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemIn"]).optional(),
            "itemId": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemIn"]).optional(),
            "textItem": t.proxy(renames["TextItemIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "questionGroupItem": t.proxy(renames["QuestionGroupItemOut"]).optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "videoItem": t.proxy(renames["VideoItemOut"]).optional(),
            "questionItem": t.proxy(renames["QuestionItemOut"]).optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemOut"]).optional(),
            "itemId": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemOut"]).optional(),
            "textItem": t.proxy(renames["TextItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
    types["RequestIn"] = t.struct(
        {
            "deleteItem": t.proxy(renames["DeleteItemRequestIn"]).optional(),
            "moveItem": t.proxy(renames["MoveItemRequestIn"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestIn"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestIn"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestIn"]).optional(),
            "updateItem": t.proxy(renames["UpdateItemRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "deleteItem": t.proxy(renames["DeleteItemRequestOut"]).optional(),
            "moveItem": t.proxy(renames["MoveItemRequestOut"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestOut"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestOut"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestOut"]).optional(),
            "updateItem": t.proxy(renames["UpdateItemRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
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
    types["GradingIn"] = t.struct(
        {
            "pointValue": t.integer(),
            "correctAnswers": t.proxy(renames["CorrectAnswersIn"]),
            "generalFeedback": t.proxy(renames["FeedbackIn"]).optional(),
            "whenRight": t.proxy(renames["FeedbackIn"]).optional(),
            "whenWrong": t.proxy(renames["FeedbackIn"]).optional(),
        }
    ).named(renames["GradingIn"])
    types["GradingOut"] = t.struct(
        {
            "pointValue": t.integer(),
            "correctAnswers": t.proxy(renames["CorrectAnswersOut"]),
            "generalFeedback": t.proxy(renames["FeedbackOut"]).optional(),
            "whenRight": t.proxy(renames["FeedbackOut"]).optional(),
            "whenWrong": t.proxy(renames["FeedbackOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradingOut"])
    types["TextLinkIn"] = t.struct(
        {"displayText": t.string(), "uri": t.string()}
    ).named(renames["TextLinkIn"])
    types["TextLinkOut"] = t.struct(
        {
            "displayText": t.string(),
            "uri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextLinkOut"])
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
    types["ChoiceQuestionIn"] = t.struct(
        {
            "shuffle": t.boolean().optional(),
            "type": t.string(),
            "options": t.array(t.proxy(renames["OptionIn"])),
        }
    ).named(renames["ChoiceQuestionIn"])
    types["ChoiceQuestionOut"] = t.struct(
        {
            "shuffle": t.boolean().optional(),
            "type": t.string(),
            "options": t.array(t.proxy(renames["OptionOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChoiceQuestionOut"])
    types["RowQuestionIn"] = t.struct({"title": t.string()}).named(
        renames["RowQuestionIn"]
    )
    types["RowQuestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RowQuestionOut"])
    types["GridIn"] = t.struct(
        {
            "shuffleQuestions": t.boolean().optional(),
            "columns": t.proxy(renames["ChoiceQuestionIn"]),
        }
    ).named(renames["GridIn"])
    types["GridOut"] = t.struct(
        {
            "shuffleQuestions": t.boolean().optional(),
            "columns": t.proxy(renames["ChoiceQuestionOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GridOut"])
    types["QuestionGroupItemIn"] = t.struct(
        {
            "grid": t.proxy(renames["GridIn"]).optional(),
            "questions": t.array(t.proxy(renames["QuestionIn"])),
            "image": t.proxy(renames["ImageIn"]).optional(),
        }
    ).named(renames["QuestionGroupItemIn"])
    types["QuestionGroupItemOut"] = t.struct(
        {
            "grid": t.proxy(renames["GridOut"]).optional(),
            "questions": t.array(t.proxy(renames["QuestionOut"])),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionGroupItemOut"])
    types["LocationIn"] = t.struct({"index": t.integer().optional()}).named(
        renames["LocationIn"]
    )
    types["LocationOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CorrectAnswerIn"] = t.struct({"value": t.string()}).named(
        renames["CorrectAnswerIn"]
    )
    types["CorrectAnswerOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CorrectAnswerOut"])
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
    types["TimeQuestionIn"] = t.struct({"duration": t.boolean().optional()}).named(
        renames["TimeQuestionIn"]
    )
    types["TimeQuestionOut"] = t.struct(
        {
            "duration": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeQuestionOut"])
    types["RenewWatchRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenewWatchRequestIn"]
    )
    types["RenewWatchRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RenewWatchRequestOut"])
    types["FileUploadAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FileUploadAnswersIn"]
    )
    types["FileUploadAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["FileUploadAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadAnswersOut"])
    types["FormIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemIn"])),
            "info": t.proxy(renames["InfoIn"]),
            "settings": t.proxy(renames["FormSettingsIn"]).optional(),
        }
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ItemOut"])),
            "revisionId": t.string().optional(),
            "info": t.proxy(renames["InfoOut"]),
            "linkedSheetId": t.string().optional(),
            "formId": t.string().optional(),
            "responderUri": t.string().optional(),
            "settings": t.proxy(renames["FormSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
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
    types["PageBreakItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PageBreakItemIn"]
    )
    types["PageBreakItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PageBreakItemOut"])
    types["TextItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextItemIn"]
    )
    types["TextItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextItemOut"])
    types["ResponseIn"] = t.struct(
        {"createItem": t.proxy(renames["CreateItemResponseIn"]).optional()}
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createItem": t.proxy(renames["CreateItemResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["TextAnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswerIn"]
    )
    types["TextAnswerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswerOut"])
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
    types["FormSettingsIn"] = t.struct(
        {"quizSettings": t.proxy(renames["QuizSettingsIn"]).optional()}
    ).named(renames["FormSettingsIn"])
    types["FormSettingsOut"] = t.struct(
        {
            "quizSettings": t.proxy(renames["QuizSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormSettingsOut"])
    types["WatchIn"] = t.struct(
        {"eventType": t.string(), "target": t.proxy(renames["WatchTargetIn"])}
    ).named(renames["WatchIn"])
    types["WatchOut"] = t.struct(
        {
            "eventType": t.string(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "errorType": t.string().optional(),
            "id": t.string().optional(),
            "expireTime": t.string().optional(),
            "target": t.proxy(renames["WatchTargetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchOut"])
    types["InfoIn"] = t.struct(
        {"title": t.string(), "description": t.string().optional()}
    ).named(renames["InfoIn"])
    types["InfoOut"] = t.struct(
        {
            "documentTitle": t.string().optional(),
            "title": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoOut"])

    functions = {}
    functions["formsBatchUpdate"] = forms.get(
        "v1/forms/{formId}",
        t.struct({"formId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsCreate"] = forms.get(
        "v1/forms/{formId}",
        t.struct({"formId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsGet"] = forms.get(
        "v1/forms/{formId}",
        t.struct({"formId": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsResponsesGet"] = forms.get(
        "v1/forms/{formId}/responses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "formId": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFormResponsesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsResponsesList"] = forms.get(
        "v1/forms/{formId}/responses",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "formId": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFormResponsesResponseOut"]),
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

    return Import(importer="forms", renames=renames, types=types, functions=functions)
