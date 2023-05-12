from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    TokenIn: t.typedef = ...
    TokenOut: t.typedef = ...
    AnalyzeEntitiesRequestIn: t.typedef = ...
    AnalyzeEntitiesRequestOut: t.typedef = ...
    AnalyzeEntitiesResponseIn: t.typedef = ...
    AnalyzeEntitiesResponseOut: t.typedef = ...
    EntityMentionIn: t.typedef = ...
    EntityMentionOut: t.typedef = ...
    ClassificationCategoryIn: t.typedef = ...
    ClassificationCategoryOut: t.typedef = ...
    AnalyzeEntitySentimentResponseIn: t.typedef = ...
    AnalyzeEntitySentimentResponseOut: t.typedef = ...
    AnalyzeSentimentResponseIn: t.typedef = ...
    AnalyzeSentimentResponseOut: t.typedef = ...
    TextSpanIn: t.typedef = ...
    TextSpanOut: t.typedef = ...
    V1ModelIn: t.typedef = ...
    V1ModelOut: t.typedef = ...
    AnnotateTextRequestIn: t.typedef = ...
    AnnotateTextRequestOut: t.typedef = ...
    V2ModelIn: t.typedef = ...
    V2ModelOut: t.typedef = ...
    AnalyzeEntitySentimentRequestIn: t.typedef = ...
    AnalyzeEntitySentimentRequestOut: t.typedef = ...
    DependencyEdgeIn: t.typedef = ...
    DependencyEdgeOut: t.typedef = ...
    PartOfSpeechIn: t.typedef = ...
    PartOfSpeechOut: t.typedef = ...
    SentimentIn: t.typedef = ...
    SentimentOut: t.typedef = ...
    FeaturesIn: t.typedef = ...
    FeaturesOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    AnalyzeSyntaxResponseIn: t.typedef = ...
    AnalyzeSyntaxResponseOut: t.typedef = ...
    ClassifyTextResponseIn: t.typedef = ...
    ClassifyTextResponseOut: t.typedef = ...
    AnnotateTextResponseIn: t.typedef = ...
    AnnotateTextResponseOut: t.typedef = ...
    AnalyzeSyntaxRequestIn: t.typedef = ...
    AnalyzeSyntaxRequestOut: t.typedef = ...
    DocumentIn: t.typedef = ...
    DocumentOut: t.typedef = ...
    AnalyzeSentimentRequestIn: t.typedef = ...
    AnalyzeSentimentRequestOut: t.typedef = ...
    ClassifyTextRequestIn: t.typedef = ...
    ClassifyTextRequestOut: t.typedef = ...
    EntityIn: t.typedef = ...
    EntityOut: t.typedef = ...
    ClassificationModelOptionsIn: t.typedef = ...
    ClassificationModelOptionsOut: t.typedef = ...
    SentenceIn: t.typedef = ...
    SentenceOut: t.typedef = ...

class FuncList:
    documentsAnalyzeSyntax: t.func = ...
    documentsClassifyText: t.func = ...
    documentsAnnotateText: t.func = ...
    documentsAnalyzeEntitySentiment: t.func = ...
    documentsAnalyzeEntities: t.func = ...
    documentsAnalyzeSentiment: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_language() -> Import: ...
