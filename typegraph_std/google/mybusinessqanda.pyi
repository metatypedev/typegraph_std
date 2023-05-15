from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListAnswersResponseIn: t.typedef = ...
    ListAnswersResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    AnswerIn: t.typedef = ...
    AnswerOut: t.typedef = ...
    ListQuestionsResponseIn: t.typedef = ...
    ListQuestionsResponseOut: t.typedef = ...
    UpsertAnswerRequestIn: t.typedef = ...
    UpsertAnswerRequestOut: t.typedef = ...
    AuthorIn: t.typedef = ...
    AuthorOut: t.typedef = ...
    QuestionIn: t.typedef = ...
    QuestionOut: t.typedef = ...

class FuncList:
    locationsQuestionsPatch: t.func = ...
    locationsQuestionsCreate: t.func = ...
    locationsQuestionsDelete: t.func = ...
    locationsQuestionsList: t.func = ...
    locationsQuestionsAnswersUpsert: t.func = ...
    locationsQuestionsAnswersList: t.func = ...
    locationsQuestionsAnswersDelete: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_mybusinessqanda() -> Import: ...