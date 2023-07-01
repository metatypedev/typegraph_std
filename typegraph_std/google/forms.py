from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_forms():
    forms = HTTPRuntime("https://forms.googleapis.com/")

    renames = {
        "ErrorResponse": "_forms_1_ErrorResponse",
        "GradeIn": "_forms_2_GradeIn",
        "GradeOut": "_forms_3_GradeOut",
        "MoveItemRequestIn": "_forms_4_MoveItemRequestIn",
        "MoveItemRequestOut": "_forms_5_MoveItemRequestOut",
        "BatchUpdateFormResponseIn": "_forms_6_BatchUpdateFormResponseIn",
        "BatchUpdateFormResponseOut": "_forms_7_BatchUpdateFormResponseOut",
        "OptionIn": "_forms_8_OptionIn",
        "OptionOut": "_forms_9_OptionOut",
        "TimeQuestionIn": "_forms_10_TimeQuestionIn",
        "TimeQuestionOut": "_forms_11_TimeQuestionOut",
        "UpdateFormInfoRequestIn": "_forms_12_UpdateFormInfoRequestIn",
        "UpdateFormInfoRequestOut": "_forms_13_UpdateFormInfoRequestOut",
        "FileUploadAnswersIn": "_forms_14_FileUploadAnswersIn",
        "FileUploadAnswersOut": "_forms_15_FileUploadAnswersOut",
        "RequestIn": "_forms_16_RequestIn",
        "RequestOut": "_forms_17_RequestOut",
        "VideoLinkIn": "_forms_18_VideoLinkIn",
        "VideoLinkOut": "_forms_19_VideoLinkOut",
        "InfoIn": "_forms_20_InfoIn",
        "InfoOut": "_forms_21_InfoOut",
        "VideoItemIn": "_forms_22_VideoItemIn",
        "VideoItemOut": "_forms_23_VideoItemOut",
        "DeleteItemRequestIn": "_forms_24_DeleteItemRequestIn",
        "DeleteItemRequestOut": "_forms_25_DeleteItemRequestOut",
        "LocationIn": "_forms_26_LocationIn",
        "LocationOut": "_forms_27_LocationOut",
        "TextAnswersIn": "_forms_28_TextAnswersIn",
        "TextAnswersOut": "_forms_29_TextAnswersOut",
        "CorrectAnswersIn": "_forms_30_CorrectAnswersIn",
        "CorrectAnswersOut": "_forms_31_CorrectAnswersOut",
        "CloudPubsubTopicIn": "_forms_32_CloudPubsubTopicIn",
        "CloudPubsubTopicOut": "_forms_33_CloudPubsubTopicOut",
        "FormIn": "_forms_34_FormIn",
        "FormOut": "_forms_35_FormOut",
        "WatchTargetIn": "_forms_36_WatchTargetIn",
        "WatchTargetOut": "_forms_37_WatchTargetOut",
        "TextItemIn": "_forms_38_TextItemIn",
        "TextItemOut": "_forms_39_TextItemOut",
        "AnswerIn": "_forms_40_AnswerIn",
        "AnswerOut": "_forms_41_AnswerOut",
        "CreateWatchRequestIn": "_forms_42_CreateWatchRequestIn",
        "CreateWatchRequestOut": "_forms_43_CreateWatchRequestOut",
        "QuestionIn": "_forms_44_QuestionIn",
        "QuestionOut": "_forms_45_QuestionOut",
        "ResponseIn": "_forms_46_ResponseIn",
        "ResponseOut": "_forms_47_ResponseOut",
        "UpdateItemRequestIn": "_forms_48_UpdateItemRequestIn",
        "UpdateItemRequestOut": "_forms_49_UpdateItemRequestOut",
        "GridIn": "_forms_50_GridIn",
        "GridOut": "_forms_51_GridOut",
        "ListFormResponsesResponseIn": "_forms_52_ListFormResponsesResponseIn",
        "ListFormResponsesResponseOut": "_forms_53_ListFormResponsesResponseOut",
        "RowQuestionIn": "_forms_54_RowQuestionIn",
        "RowQuestionOut": "_forms_55_RowQuestionOut",
        "FormSettingsIn": "_forms_56_FormSettingsIn",
        "FormSettingsOut": "_forms_57_FormSettingsOut",
        "BatchUpdateFormRequestIn": "_forms_58_BatchUpdateFormRequestIn",
        "BatchUpdateFormRequestOut": "_forms_59_BatchUpdateFormRequestOut",
        "GradingIn": "_forms_60_GradingIn",
        "GradingOut": "_forms_61_GradingOut",
        "TextAnswerIn": "_forms_62_TextAnswerIn",
        "TextAnswerOut": "_forms_63_TextAnswerOut",
        "CreateItemResponseIn": "_forms_64_CreateItemResponseIn",
        "CreateItemResponseOut": "_forms_65_CreateItemResponseOut",
        "FeedbackIn": "_forms_66_FeedbackIn",
        "FeedbackOut": "_forms_67_FeedbackOut",
        "FileUploadAnswerIn": "_forms_68_FileUploadAnswerIn",
        "FileUploadAnswerOut": "_forms_69_FileUploadAnswerOut",
        "TextLinkIn": "_forms_70_TextLinkIn",
        "TextLinkOut": "_forms_71_TextLinkOut",
        "ScaleQuestionIn": "_forms_72_ScaleQuestionIn",
        "ScaleQuestionOut": "_forms_73_ScaleQuestionOut",
        "WatchIn": "_forms_74_WatchIn",
        "WatchOut": "_forms_75_WatchOut",
        "UpdateSettingsRequestIn": "_forms_76_UpdateSettingsRequestIn",
        "UpdateSettingsRequestOut": "_forms_77_UpdateSettingsRequestOut",
        "QuestionItemIn": "_forms_78_QuestionItemIn",
        "QuestionItemOut": "_forms_79_QuestionItemOut",
        "TextQuestionIn": "_forms_80_TextQuestionIn",
        "TextQuestionOut": "_forms_81_TextQuestionOut",
        "ItemIn": "_forms_82_ItemIn",
        "ItemOut": "_forms_83_ItemOut",
        "ChoiceQuestionIn": "_forms_84_ChoiceQuestionIn",
        "ChoiceQuestionOut": "_forms_85_ChoiceQuestionOut",
        "QuizSettingsIn": "_forms_86_QuizSettingsIn",
        "QuizSettingsOut": "_forms_87_QuizSettingsOut",
        "PageBreakItemIn": "_forms_88_PageBreakItemIn",
        "PageBreakItemOut": "_forms_89_PageBreakItemOut",
        "ImageIn": "_forms_90_ImageIn",
        "ImageOut": "_forms_91_ImageOut",
        "DateQuestionIn": "_forms_92_DateQuestionIn",
        "DateQuestionOut": "_forms_93_DateQuestionOut",
        "ListWatchesResponseIn": "_forms_94_ListWatchesResponseIn",
        "ListWatchesResponseOut": "_forms_95_ListWatchesResponseOut",
        "CorrectAnswerIn": "_forms_96_CorrectAnswerIn",
        "CorrectAnswerOut": "_forms_97_CorrectAnswerOut",
        "FormResponseIn": "_forms_98_FormResponseIn",
        "FormResponseOut": "_forms_99_FormResponseOut",
        "EmptyIn": "_forms_100_EmptyIn",
        "EmptyOut": "_forms_101_EmptyOut",
        "ImageItemIn": "_forms_102_ImageItemIn",
        "ImageItemOut": "_forms_103_ImageItemOut",
        "FileUploadQuestionIn": "_forms_104_FileUploadQuestionIn",
        "FileUploadQuestionOut": "_forms_105_FileUploadQuestionOut",
        "QuestionGroupItemIn": "_forms_106_QuestionGroupItemIn",
        "QuestionGroupItemOut": "_forms_107_QuestionGroupItemOut",
        "RenewWatchRequestIn": "_forms_108_RenewWatchRequestIn",
        "RenewWatchRequestOut": "_forms_109_RenewWatchRequestOut",
        "WriteControlIn": "_forms_110_WriteControlIn",
        "WriteControlOut": "_forms_111_WriteControlOut",
        "ExtraMaterialIn": "_forms_112_ExtraMaterialIn",
        "ExtraMaterialOut": "_forms_113_ExtraMaterialOut",
        "MediaPropertiesIn": "_forms_114_MediaPropertiesIn",
        "MediaPropertiesOut": "_forms_115_MediaPropertiesOut",
        "CreateItemRequestIn": "_forms_116_CreateItemRequestIn",
        "CreateItemRequestOut": "_forms_117_CreateItemRequestOut",
        "VideoIn": "_forms_118_VideoIn",
        "VideoOut": "_forms_119_VideoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GradeIn"] = t.struct({"_": t.string().optional()}).named(renames["GradeIn"])
    types["GradeOut"] = t.struct(
        {
            "score": t.number().optional(),
            "feedback": t.proxy(renames["FeedbackOut"]).optional(),
            "correct": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradeOut"])
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
    types["BatchUpdateFormResponseIn"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseIn"])).optional(),
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
        }
    ).named(renames["BatchUpdateFormResponseIn"])
    types["BatchUpdateFormResponseOut"] = t.struct(
        {
            "replies": t.array(t.proxy(renames["ResponseOut"])).optional(),
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateFormResponseOut"])
    types["OptionIn"] = t.struct(
        {
            "goToAction": t.string().optional(),
            "isOther": t.boolean().optional(),
            "image": t.proxy(renames["ImageIn"]).optional(),
            "value": t.string(),
            "goToSectionId": t.string().optional(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "goToAction": t.string().optional(),
            "isOther": t.boolean().optional(),
            "image": t.proxy(renames["ImageOut"]).optional(),
            "value": t.string(),
            "goToSectionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
    types["TimeQuestionIn"] = t.struct({"duration": t.boolean().optional()}).named(
        renames["TimeQuestionIn"]
    )
    types["TimeQuestionOut"] = t.struct(
        {
            "duration": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeQuestionOut"])
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
    types["FileUploadAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FileUploadAnswersIn"]
    )
    types["FileUploadAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["FileUploadAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadAnswersOut"])
    types["RequestIn"] = t.struct(
        {
            "moveItem": t.proxy(renames["MoveItemRequestIn"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestIn"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestIn"]).optional(),
            "updateItem": t.proxy(renames["UpdateItemRequestIn"]).optional(),
            "deleteItem": t.proxy(renames["DeleteItemRequestIn"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "moveItem": t.proxy(renames["MoveItemRequestOut"]).optional(),
            "updateFormInfo": t.proxy(renames["UpdateFormInfoRequestOut"]).optional(),
            "updateSettings": t.proxy(renames["UpdateSettingsRequestOut"]).optional(),
            "updateItem": t.proxy(renames["UpdateItemRequestOut"]).optional(),
            "deleteItem": t.proxy(renames["DeleteItemRequestOut"]).optional(),
            "createItem": t.proxy(renames["CreateItemRequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
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
    types["InfoIn"] = t.struct(
        {"description": t.string().optional(), "title": t.string()}
    ).named(renames["InfoIn"])
    types["InfoOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string(),
            "documentTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InfoOut"])
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
    types["DeleteItemRequestIn"] = t.struct(
        {"location": t.proxy(renames["LocationIn"])}
    ).named(renames["DeleteItemRequestIn"])
    types["DeleteItemRequestOut"] = t.struct(
        {
            "location": t.proxy(renames["LocationOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteItemRequestOut"])
    types["LocationIn"] = t.struct({"index": t.integer().optional()}).named(
        renames["LocationIn"]
    )
    types["LocationOut"] = t.struct(
        {
            "index": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["TextAnswersIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswersIn"]
    )
    types["TextAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["TextAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswersOut"])
    types["CorrectAnswersIn"] = t.struct(
        {"answers": t.array(t.proxy(renames["CorrectAnswerIn"])).optional()}
    ).named(renames["CorrectAnswersIn"])
    types["CorrectAnswersOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["CorrectAnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CorrectAnswersOut"])
    types["CloudPubsubTopicIn"] = t.struct({"topicName": t.string()}).named(
        renames["CloudPubsubTopicIn"]
    )
    types["CloudPubsubTopicOut"] = t.struct(
        {"topicName": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudPubsubTopicOut"])
    types["FormIn"] = t.struct(
        {
            "info": t.proxy(renames["InfoIn"]),
            "settings": t.proxy(renames["FormSettingsIn"]).optional(),
            "items": t.array(t.proxy(renames["ItemIn"])),
        }
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "formId": t.string().optional(),
            "info": t.proxy(renames["InfoOut"]),
            "linkedSheetId": t.string().optional(),
            "responderUri": t.string().optional(),
            "settings": t.proxy(renames["FormSettingsOut"]).optional(),
            "items": t.array(t.proxy(renames["ItemOut"])),
            "revisionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
    types["WatchTargetIn"] = t.struct(
        {"topic": t.proxy(renames["CloudPubsubTopicIn"]).optional()}
    ).named(renames["WatchTargetIn"])
    types["WatchTargetOut"] = t.struct(
        {
            "topic": t.proxy(renames["CloudPubsubTopicOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchTargetOut"])
    types["TextItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextItemIn"]
    )
    types["TextItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TextItemOut"])
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
    types["CreateWatchRequestIn"] = t.struct(
        {"watch": t.proxy(renames["WatchIn"]), "watchId": t.string().optional()}
    ).named(renames["CreateWatchRequestIn"])
    types["CreateWatchRequestOut"] = t.struct(
        {
            "watch": t.proxy(renames["WatchOut"]),
            "watchId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateWatchRequestOut"])
    types["QuestionIn"] = t.struct(
        {
            "questionId": t.string().optional(),
            "dateQuestion": t.proxy(renames["DateQuestionIn"]).optional(),
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionIn"]).optional(),
            "textQuestion": t.proxy(renames["TextQuestionIn"]).optional(),
            "required": t.boolean().optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionIn"]).optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionIn"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionIn"]).optional(),
            "grading": t.proxy(renames["GradingIn"]).optional(),
            "rowQuestion": t.proxy(renames["RowQuestionIn"]).optional(),
        }
    ).named(renames["QuestionIn"])
    types["QuestionOut"] = t.struct(
        {
            "questionId": t.string().optional(),
            "dateQuestion": t.proxy(renames["DateQuestionOut"]).optional(),
            "fileUploadQuestion": t.proxy(renames["FileUploadQuestionOut"]).optional(),
            "textQuestion": t.proxy(renames["TextQuestionOut"]).optional(),
            "required": t.boolean().optional(),
            "choiceQuestion": t.proxy(renames["ChoiceQuestionOut"]).optional(),
            "scaleQuestion": t.proxy(renames["ScaleQuestionOut"]).optional(),
            "timeQuestion": t.proxy(renames["TimeQuestionOut"]).optional(),
            "grading": t.proxy(renames["GradingOut"]).optional(),
            "rowQuestion": t.proxy(renames["RowQuestionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionOut"])
    types["ResponseIn"] = t.struct(
        {"createItem": t.proxy(renames["CreateItemResponseIn"]).optional()}
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "createItem": t.proxy(renames["CreateItemResponseOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
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
    types["RowQuestionIn"] = t.struct({"title": t.string()}).named(
        renames["RowQuestionIn"]
    )
    types["RowQuestionOut"] = t.struct(
        {"title": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RowQuestionOut"])
    types["FormSettingsIn"] = t.struct(
        {"quizSettings": t.proxy(renames["QuizSettingsIn"]).optional()}
    ).named(renames["FormSettingsIn"])
    types["FormSettingsOut"] = t.struct(
        {
            "quizSettings": t.proxy(renames["QuizSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormSettingsOut"])
    types["BatchUpdateFormRequestIn"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlIn"]).optional(),
            "requests": t.array(t.proxy(renames["RequestIn"])),
            "includeFormInResponse": t.boolean().optional(),
        }
    ).named(renames["BatchUpdateFormRequestIn"])
    types["BatchUpdateFormRequestOut"] = t.struct(
        {
            "writeControl": t.proxy(renames["WriteControlOut"]).optional(),
            "requests": t.array(t.proxy(renames["RequestOut"])),
            "includeFormInResponse": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateFormRequestOut"])
    types["GradingIn"] = t.struct(
        {
            "correctAnswers": t.proxy(renames["CorrectAnswersIn"]),
            "whenRight": t.proxy(renames["FeedbackIn"]).optional(),
            "pointValue": t.integer(),
            "generalFeedback": t.proxy(renames["FeedbackIn"]).optional(),
            "whenWrong": t.proxy(renames["FeedbackIn"]).optional(),
        }
    ).named(renames["GradingIn"])
    types["GradingOut"] = t.struct(
        {
            "correctAnswers": t.proxy(renames["CorrectAnswersOut"]),
            "whenRight": t.proxy(renames["FeedbackOut"]).optional(),
            "pointValue": t.integer(),
            "generalFeedback": t.proxy(renames["FeedbackOut"]).optional(),
            "whenWrong": t.proxy(renames["FeedbackOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GradingOut"])
    types["TextAnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["TextAnswerIn"]
    )
    types["TextAnswerOut"] = t.struct(
        {
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextAnswerOut"])
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
    types["FileUploadAnswerIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FileUploadAnswerIn"]
    )
    types["FileUploadAnswerOut"] = t.struct(
        {
            "fileId": t.string().optional(),
            "mimeType": t.string().optional(),
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadAnswerOut"])
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
    types["ScaleQuestionIn"] = t.struct(
        {
            "high": t.integer(),
            "lowLabel": t.string().optional(),
            "highLabel": t.string().optional(),
            "low": t.integer(),
        }
    ).named(renames["ScaleQuestionIn"])
    types["ScaleQuestionOut"] = t.struct(
        {
            "high": t.integer(),
            "lowLabel": t.string().optional(),
            "highLabel": t.string().optional(),
            "low": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScaleQuestionOut"])
    types["WatchIn"] = t.struct(
        {"target": t.proxy(renames["WatchTargetIn"]), "eventType": t.string()}
    ).named(renames["WatchIn"])
    types["WatchOut"] = t.struct(
        {
            "errorType": t.string().optional(),
            "expireTime": t.string().optional(),
            "target": t.proxy(renames["WatchTargetOut"]),
            "createTime": t.string().optional(),
            "id": t.string().optional(),
            "eventType": t.string(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WatchOut"])
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
    types["TextQuestionIn"] = t.struct({"paragraph": t.boolean().optional()}).named(
        renames["TextQuestionIn"]
    )
    types["TextQuestionOut"] = t.struct(
        {
            "paragraph": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextQuestionOut"])
    types["ItemIn"] = t.struct(
        {
            "questionGroupItem": t.proxy(renames["QuestionGroupItemIn"]).optional(),
            "textItem": t.proxy(renames["TextItemIn"]).optional(),
            "videoItem": t.proxy(renames["VideoItemIn"]).optional(),
            "questionItem": t.proxy(renames["QuestionItemIn"]).optional(),
            "title": t.string().optional(),
            "itemId": t.string().optional(),
            "description": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemIn"]).optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemIn"]).optional(),
        }
    ).named(renames["ItemIn"])
    types["ItemOut"] = t.struct(
        {
            "questionGroupItem": t.proxy(renames["QuestionGroupItemOut"]).optional(),
            "textItem": t.proxy(renames["TextItemOut"]).optional(),
            "videoItem": t.proxy(renames["VideoItemOut"]).optional(),
            "questionItem": t.proxy(renames["QuestionItemOut"]).optional(),
            "title": t.string().optional(),
            "itemId": t.string().optional(),
            "description": t.string().optional(),
            "imageItem": t.proxy(renames["ImageItemOut"]).optional(),
            "pageBreakItem": t.proxy(renames["PageBreakItemOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ItemOut"])
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
    types["QuizSettingsIn"] = t.struct({"isQuiz": t.boolean().optional()}).named(
        renames["QuizSettingsIn"]
    )
    types["QuizSettingsOut"] = t.struct(
        {
            "isQuiz": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuizSettingsOut"])
    types["PageBreakItemIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PageBreakItemIn"]
    )
    types["PageBreakItemOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PageBreakItemOut"])
    types["ImageIn"] = t.struct(
        {
            "properties": t.proxy(renames["MediaPropertiesIn"]).optional(),
            "sourceUri": t.string().optional(),
            "altText": t.string().optional(),
        }
    ).named(renames["ImageIn"])
    types["ImageOut"] = t.struct(
        {
            "properties": t.proxy(renames["MediaPropertiesOut"]).optional(),
            "contentUri": t.string().optional(),
            "sourceUri": t.string().optional(),
            "altText": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageOut"])
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
    types["ListWatchesResponseIn"] = t.struct(
        {"watches": t.array(t.proxy(renames["WatchIn"])).optional()}
    ).named(renames["ListWatchesResponseIn"])
    types["ListWatchesResponseOut"] = t.struct(
        {
            "watches": t.array(t.proxy(renames["WatchOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWatchesResponseOut"])
    types["CorrectAnswerIn"] = t.struct({"value": t.string()}).named(
        renames["CorrectAnswerIn"]
    )
    types["CorrectAnswerOut"] = t.struct(
        {"value": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CorrectAnswerOut"])
    types["FormResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FormResponseIn"]
    )
    types["FormResponseOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "lastSubmittedTime": t.string().optional(),
            "totalScore": t.number().optional(),
            "respondentEmail": t.string().optional(),
            "responseId": t.string().optional(),
            "answers": t.struct({"_": t.string().optional()}).optional(),
            "formId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ImageItemIn"] = t.struct({"image": t.proxy(renames["ImageIn"])}).named(
        renames["ImageItemIn"]
    )
    types["ImageItemOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImageItemOut"])
    types["FileUploadQuestionIn"] = t.struct(
        {
            "maxFileSize": t.string().optional(),
            "maxFiles": t.integer().optional(),
            "types": t.array(t.string()).optional(),
            "folderId": t.string(),
        }
    ).named(renames["FileUploadQuestionIn"])
    types["FileUploadQuestionOut"] = t.struct(
        {
            "maxFileSize": t.string().optional(),
            "maxFiles": t.integer().optional(),
            "types": t.array(t.string()).optional(),
            "folderId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileUploadQuestionOut"])
    types["QuestionGroupItemIn"] = t.struct(
        {
            "image": t.proxy(renames["ImageIn"]).optional(),
            "grid": t.proxy(renames["GridIn"]).optional(),
            "questions": t.array(t.proxy(renames["QuestionIn"])),
        }
    ).named(renames["QuestionGroupItemIn"])
    types["QuestionGroupItemOut"] = t.struct(
        {
            "image": t.proxy(renames["ImageOut"]).optional(),
            "grid": t.proxy(renames["GridOut"]).optional(),
            "questions": t.array(t.proxy(renames["QuestionOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionGroupItemOut"])
    types["RenewWatchRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RenewWatchRequestIn"]
    )
    types["RenewWatchRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RenewWatchRequestOut"])
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

    functions = {}
    functions["formsBatchUpdate"] = forms.post(
        "v1/forms",
        t.struct(
            {
                "info": t.proxy(renames["InfoIn"]),
                "settings": t.proxy(renames["FormSettingsIn"]).optional(),
                "items": t.array(t.proxy(renames["ItemIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsGet"] = forms.post(
        "v1/forms",
        t.struct(
            {
                "info": t.proxy(renames["InfoIn"]),
                "settings": t.proxy(renames["FormSettingsIn"]).optional(),
                "items": t.array(t.proxy(renames["ItemIn"])),
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
                "info": t.proxy(renames["InfoIn"]),
                "settings": t.proxy(renames["FormSettingsIn"]).optional(),
                "items": t.array(t.proxy(renames["ItemIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["FormOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesDelete"] = forms.post(
        "v1/forms/{formId}/watches",
        t.struct(
            {
                "formId": t.string(),
                "watch": t.proxy(renames["WatchIn"]),
                "watchId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesRenew"] = forms.post(
        "v1/forms/{formId}/watches",
        t.struct(
            {
                "formId": t.string(),
                "watch": t.proxy(renames["WatchIn"]),
                "watchId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesList"] = forms.post(
        "v1/forms/{formId}/watches",
        t.struct(
            {
                "formId": t.string(),
                "watch": t.proxy(renames["WatchIn"]),
                "watchId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["formsWatchesCreate"] = forms.post(
        "v1/forms/{formId}/watches",
        t.struct(
            {
                "formId": t.string(),
                "watch": t.proxy(renames["WatchIn"]),
                "watchId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WatchOut"]),
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
