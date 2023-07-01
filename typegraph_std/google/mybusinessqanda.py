from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_mybusinessqanda():
    mybusinessqanda = HTTPRuntime("https://mybusinessqanda.googleapis.com/")

    renames = {
        "ErrorResponse": "_mybusinessqanda_1_ErrorResponse",
        "ListQuestionsResponseIn": "_mybusinessqanda_2_ListQuestionsResponseIn",
        "ListQuestionsResponseOut": "_mybusinessqanda_3_ListQuestionsResponseOut",
        "ListAnswersResponseIn": "_mybusinessqanda_4_ListAnswersResponseIn",
        "ListAnswersResponseOut": "_mybusinessqanda_5_ListAnswersResponseOut",
        "QuestionIn": "_mybusinessqanda_6_QuestionIn",
        "QuestionOut": "_mybusinessqanda_7_QuestionOut",
        "AnswerIn": "_mybusinessqanda_8_AnswerIn",
        "AnswerOut": "_mybusinessqanda_9_AnswerOut",
        "AuthorIn": "_mybusinessqanda_10_AuthorIn",
        "AuthorOut": "_mybusinessqanda_11_AuthorOut",
        "EmptyIn": "_mybusinessqanda_12_EmptyIn",
        "EmptyOut": "_mybusinessqanda_13_EmptyOut",
        "UpsertAnswerRequestIn": "_mybusinessqanda_14_UpsertAnswerRequestIn",
        "UpsertAnswerRequestOut": "_mybusinessqanda_15_UpsertAnswerRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListQuestionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "questions": t.array(t.proxy(renames["QuestionIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListQuestionsResponseIn"])
    types["ListQuestionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "questions": t.array(t.proxy(renames["QuestionOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListQuestionsResponseOut"])
    types["ListAnswersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "answers": t.array(t.proxy(renames["AnswerIn"])).optional(),
        }
    ).named(renames["ListAnswersResponseIn"])
    types["ListAnswersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "answers": t.array(t.proxy(renames["AnswerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAnswersResponseOut"])
    types["QuestionIn"] = t.struct(
        {"name": t.string().optional(), "text": t.string()}
    ).named(renames["QuestionIn"])
    types["QuestionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "upvoteCount": t.integer().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "text": t.string(),
            "author": t.proxy(renames["AuthorOut"]).optional(),
            "topAnswers": t.array(t.proxy(renames["AnswerOut"])).optional(),
            "totalAnswerCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuestionOut"])
    types["AnswerIn"] = t.struct({"text": t.string()}).named(renames["AnswerIn"])
    types["AnswerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "upvoteCount": t.integer().optional(),
            "author": t.proxy(renames["AuthorOut"]).optional(),
            "text": t.string(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnswerOut"])
    types["AuthorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "profilePhotoUri": t.string().optional(),
        }
    ).named(renames["AuthorIn"])
    types["AuthorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "profilePhotoUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UpsertAnswerRequestIn"] = t.struct(
        {"answer": t.proxy(renames["AnswerIn"])}
    ).named(renames["UpsertAnswerRequestIn"])
    types["UpsertAnswerRequestOut"] = t.struct(
        {
            "answer": t.proxy(renames["AnswerOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpsertAnswerRequestOut"])

    functions = {}
    functions["locationsQuestionsList"] = mybusinessqanda.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsDelete"] = mybusinessqanda.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsCreate"] = mybusinessqanda.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsPatch"] = mybusinessqanda.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "text": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["QuestionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersList"] = mybusinessqanda.post(
        "v1/{parent}/answers:upsert",
        t.struct(
            {
                "parent": t.string(),
                "answer": t.proxy(renames["AnswerIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnswerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersDelete"] = mybusinessqanda.post(
        "v1/{parent}/answers:upsert",
        t.struct(
            {
                "parent": t.string(),
                "answer": t.proxy(renames["AnswerIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnswerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["locationsQuestionsAnswersUpsert"] = mybusinessqanda.post(
        "v1/{parent}/answers:upsert",
        t.struct(
            {
                "parent": t.string(),
                "answer": t.proxy(renames["AnswerIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnswerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="mybusinessqanda",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
