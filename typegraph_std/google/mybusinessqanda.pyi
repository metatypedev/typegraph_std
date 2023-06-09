from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListQuestionsResponseIn: t.typedef = ...
    ListQuestionsResponseOut: t.typedef = ...
    ListAnswersResponseIn: t.typedef = ...
    ListAnswersResponseOut: t.typedef = ...
    QuestionIn: t.typedef = ...
    QuestionOut: t.typedef = ...
    AnswerIn: t.typedef = ...
    AnswerOut: t.typedef = ...
    AuthorIn: t.typedef = ...
    AuthorOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    UpsertAnswerRequestIn: t.typedef = ...
    UpsertAnswerRequestOut: t.typedef = ...

class FuncList:
    locationsQuestionsList: t.func = ...
    locationsQuestionsDelete: t.func = ...
    locationsQuestionsCreate: t.func = ...
    locationsQuestionsPatch: t.func = ...
    locationsQuestionsAnswersList: t.func = ...
    locationsQuestionsAnswersDelete: t.func = ...
    locationsQuestionsAnswersUpsert: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_mybusinessqanda() -> Import: ...
