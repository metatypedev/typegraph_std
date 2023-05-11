from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_mybusinessqanda() -> Import:
    mybusinessqanda = HTTPRuntime("https://mybusinessqanda.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusinessqanda_1_ErrorResponse",
        "UpsertAnswerRequestIn": "_mybusinessqanda_2_UpsertAnswerRequestIn",
        "UpsertAnswerRequestOut": "_mybusinessqanda_3_UpsertAnswerRequestOut",
        "AnswerIn": "_mybusinessqanda_4_AnswerIn",
        "AnswerOut": "_mybusinessqanda_5_AnswerOut",
        "ListAnswersResponseIn": "_mybusinessqanda_6_ListAnswersResponseIn",
        "ListAnswersResponseOut": "_mybusinessqanda_7_ListAnswersResponseOut",
        "AuthorIn": "_mybusinessqanda_8_AuthorIn",
        "AuthorOut": "_mybusinessqanda_9_AuthorOut",
        "QuestionIn": "_mybusinessqanda_10_QuestionIn",
        "QuestionOut": "_mybusinessqanda_11_QuestionOut",
        "EmptyIn": "_mybusinessqanda_12_EmptyIn",
        "EmptyOut": "_mybusinessqanda_13_EmptyOut",
        "ListQuestionsResponseIn": "_mybusinessqanda_14_ListQuestionsResponseIn",
        "ListQuestionsResponseOut": "_mybusinessqanda_15_ListQuestionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UpsertAnswerRequestIn"] = t.struct(
        {"answer": t.proxy(renames["AnswerIn"])}
    ).named(renames["UpsertAnswerRequestIn"])
    types["UpsertAnswerRequestOut"] = t.struct(
        {
            "answer": t.proxy(renames["AnswerOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpsertAnswerRequestOut"])
    types["AnswerIn"] = t.struct({"text": t.string()}).named(renames["AnswerIn"])
    types["AnswerOut"] = t.struct(
        {
            "upvoteCount": t.integer().optional(),
            "name": t.string().optional(),
            "author": t.proxy(renames["AuthorOut"]).optional(),
            "text": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnswerOut"])
    types["ListAnswersResponseIn"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["AnswerIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListAnswersResponseIn"])
    types["ListAnswersResponseOut"] = t.struct(
        {
            "answers": t.array(t.proxy(renames["AnswerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAnswersResponseOut"])
    types["AuthorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "profilePhotoUri": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["AuthorIn"])
    types["AuthorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "profilePhotoUri": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorOut"])
    types["QuestionIn"] = t.struct(
        {"text": t.string(), "name": t.string().optional()}
    ).named(renames["QuestionIn"])
    types["QuestionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "topAnswers": t.array(t.proxy(renames["AnswerOut"])).optional(),
            "text": t.string(),
            "upvoteCount": t.integer().optional(),
            "author": t.proxy(renames["AuthorOut"]).optional(),
            "createTime": t.string().optional(),
            "totalAnswerCount": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListQuestionsResponseIn"] = t.struct(
        {
            "questions": t.array(t.proxy(renames["QuestionIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListQuestionsResponseIn"])
    types["ListQuestionsResponseOut"] = t.struct(
        {
            "questions": t.array(t.proxy(renames["QuestionOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQuestionsResponseOut"])

    functions = {}
    functions["locationsQuestionsList"] = mybusinessqanda.post(
        "v1/{parent}",
        t.struct(
            {
                "parent": t.string(),
                "text": t.string(),
                "name": t.string().optional(),
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
                "text": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsDelete"] = mybusinessqanda.post(
        "v1/{parent}",
        t.struct(
            {
                "parent": t.string(),
                "text": t.string(),
                "name": t.string().optional(),
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
                "text": t.string(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersList"] = mybusinessqanda.delete(
        "v1/{name}/answers:delete",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersUpsert"] = mybusinessqanda.delete(
        "v1/{name}/answers:delete",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersDelete"] = mybusinessqanda.delete(
        "v1/{name}/answers:delete",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessqanda", renames=renames, types=types, functions=functions
    )
