from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_mybusinessqanda() -> Import:
    mybusinessqanda = HTTPRuntime("https://mybusinessqanda.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusinessqanda_1_ErrorResponse",
        "QuestionIn": "_mybusinessqanda_2_QuestionIn",
        "QuestionOut": "_mybusinessqanda_3_QuestionOut",
        "AuthorIn": "_mybusinessqanda_4_AuthorIn",
        "AuthorOut": "_mybusinessqanda_5_AuthorOut",
        "ListQuestionsResponseIn": "_mybusinessqanda_6_ListQuestionsResponseIn",
        "ListQuestionsResponseOut": "_mybusinessqanda_7_ListQuestionsResponseOut",
        "AnswerIn": "_mybusinessqanda_8_AnswerIn",
        "AnswerOut": "_mybusinessqanda_9_AnswerOut",
        "ListAnswersResponseIn": "_mybusinessqanda_10_ListAnswersResponseIn",
        "ListAnswersResponseOut": "_mybusinessqanda_11_ListAnswersResponseOut",
        "UpsertAnswerRequestIn": "_mybusinessqanda_12_UpsertAnswerRequestIn",
        "UpsertAnswerRequestOut": "_mybusinessqanda_13_UpsertAnswerRequestOut",
        "EmptyIn": "_mybusinessqanda_14_EmptyIn",
        "EmptyOut": "_mybusinessqanda_15_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["QuestionIn"] = t.struct(
        {"name": t.string().optional(), "text": t.string()}
    ).named(renames["QuestionIn"])
    types["QuestionOut"] = t.struct(
        {
            "author": t.proxy(renames["AuthorOut"]).optional(),
            "topAnswers": t.array(t.proxy(renames["AnswerOut"])).optional(),
            "name": t.string().optional(),
            "text": t.string(),
            "totalAnswerCount": t.integer().optional(),
            "createTime": t.string().optional(),
            "upvoteCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionOut"])
    types["AuthorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "profilePhotoUri": t.string().optional(),
        }
    ).named(renames["AuthorIn"])
    types["AuthorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "profilePhotoUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorOut"])
    types["ListQuestionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "questions": t.array(t.proxy(renames["QuestionIn"])).optional(),
        }
    ).named(renames["ListQuestionsResponseIn"])
    types["ListQuestionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "questions": t.array(t.proxy(renames["QuestionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQuestionsResponseOut"])
    types["AnswerIn"] = t.struct({"text": t.string()}).named(renames["AnswerIn"])
    types["AnswerOut"] = t.struct(
        {
            "text": t.string(),
            "updateTime": t.string().optional(),
            "author": t.proxy(renames["AuthorOut"]).optional(),
            "upvoteCount": t.integer().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnswerOut"])
    types["ListAnswersResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "answers": t.array(t.proxy(renames["AnswerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAnswersResponseIn"])
    types["ListAnswersResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "answers": t.array(t.proxy(renames["AnswerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAnswersResponseOut"])
    types["UpsertAnswerRequestIn"] = t.struct(
        {"answer": t.proxy(renames["AnswerIn"])}
    ).named(renames["UpsertAnswerRequestIn"])
    types["UpsertAnswerRequestOut"] = t.struct(
        {
            "answer": t.proxy(renames["AnswerOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpsertAnswerRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["locationsQuestionsDelete"] = mybusinessqanda.post(
        "v1/{parent}",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsList"] = mybusinessqanda.post(
        "v1/{parent}",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsPatch"] = mybusinessqanda.post(
        "v1/{parent}",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsCreate"] = mybusinessqanda.post(
        "v1/{parent}",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersUpsert"] = mybusinessqanda.get(
        "v1/{parent}/answers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnswersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersDelete"] = mybusinessqanda.get(
        "v1/{parent}/answers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnswersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersList"] = mybusinessqanda.get(
        "v1/{parent}/answers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAnswersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessqanda",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
