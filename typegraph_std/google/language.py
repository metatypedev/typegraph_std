from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_language() -> Import:
    language = HTTPRuntime("https://language.googleapis.com/")

    renames = {
        "ErrorResponse": "_language_1_ErrorResponse",
        "AnalyzeEntitiesRequestIn": "_language_2_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_language_3_AnalyzeEntitiesRequestOut",
        "TokenIn": "_language_4_TokenIn",
        "TokenOut": "_language_5_TokenOut",
        "AnnotateTextRequestIn": "_language_6_AnnotateTextRequestIn",
        "AnnotateTextRequestOut": "_language_7_AnnotateTextRequestOut",
        "SentimentIn": "_language_8_SentimentIn",
        "SentimentOut": "_language_9_SentimentOut",
        "AnalyzeSyntaxResponseIn": "_language_10_AnalyzeSyntaxResponseIn",
        "AnalyzeSyntaxResponseOut": "_language_11_AnalyzeSyntaxResponseOut",
        "AnalyzeSentimentRequestIn": "_language_12_AnalyzeSentimentRequestIn",
        "AnalyzeSentimentRequestOut": "_language_13_AnalyzeSentimentRequestOut",
        "StatusIn": "_language_14_StatusIn",
        "StatusOut": "_language_15_StatusOut",
        "AnalyzeEntitySentimentResponseIn": "_language_16_AnalyzeEntitySentimentResponseIn",
        "AnalyzeEntitySentimentResponseOut": "_language_17_AnalyzeEntitySentimentResponseOut",
        "AnalyzeSyntaxRequestIn": "_language_18_AnalyzeSyntaxRequestIn",
        "AnalyzeSyntaxRequestOut": "_language_19_AnalyzeSyntaxRequestOut",
        "V2ModelIn": "_language_20_V2ModelIn",
        "V2ModelOut": "_language_21_V2ModelOut",
        "TextSpanIn": "_language_22_TextSpanIn",
        "TextSpanOut": "_language_23_TextSpanOut",
        "ClassificationModelOptionsIn": "_language_24_ClassificationModelOptionsIn",
        "ClassificationModelOptionsOut": "_language_25_ClassificationModelOptionsOut",
        "AnnotateTextResponseIn": "_language_26_AnnotateTextResponseIn",
        "AnnotateTextResponseOut": "_language_27_AnnotateTextResponseOut",
        "AnalyzeSentimentResponseIn": "_language_28_AnalyzeSentimentResponseIn",
        "AnalyzeSentimentResponseOut": "_language_29_AnalyzeSentimentResponseOut",
        "DocumentIn": "_language_30_DocumentIn",
        "DocumentOut": "_language_31_DocumentOut",
        "AnalyzeEntitySentimentRequestIn": "_language_32_AnalyzeEntitySentimentRequestIn",
        "AnalyzeEntitySentimentRequestOut": "_language_33_AnalyzeEntitySentimentRequestOut",
        "ClassifyTextResponseIn": "_language_34_ClassifyTextResponseIn",
        "ClassifyTextResponseOut": "_language_35_ClassifyTextResponseOut",
        "DependencyEdgeIn": "_language_36_DependencyEdgeIn",
        "DependencyEdgeOut": "_language_37_DependencyEdgeOut",
        "ClassifyTextRequestIn": "_language_38_ClassifyTextRequestIn",
        "ClassifyTextRequestOut": "_language_39_ClassifyTextRequestOut",
        "EntityIn": "_language_40_EntityIn",
        "EntityOut": "_language_41_EntityOut",
        "SentenceIn": "_language_42_SentenceIn",
        "SentenceOut": "_language_43_SentenceOut",
        "V1ModelIn": "_language_44_V1ModelIn",
        "V1ModelOut": "_language_45_V1ModelOut",
        "AnalyzeEntitiesResponseIn": "_language_46_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_language_47_AnalyzeEntitiesResponseOut",
        "FeaturesIn": "_language_48_FeaturesIn",
        "FeaturesOut": "_language_49_FeaturesOut",
        "EntityMentionIn": "_language_50_EntityMentionIn",
        "EntityMentionOut": "_language_51_EntityMentionOut",
        "ClassificationCategoryIn": "_language_52_ClassificationCategoryIn",
        "ClassificationCategoryOut": "_language_53_ClassificationCategoryOut",
        "PartOfSpeechIn": "_language_54_PartOfSpeechIn",
        "PartOfSpeechOut": "_language_55_PartOfSpeechOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AnalyzeEntitiesRequestIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]),
            "encodingType": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestIn"])
    types["AnalyzeEntitiesRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "encodingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestOut"])
    types["TokenIn"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "dependencyEdge": t.proxy(renames["DependencyEdgeIn"]).optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechIn"]).optional(),
            "lemma": t.string().optional(),
        }
    ).named(renames["TokenIn"])
    types["TokenOut"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "dependencyEdge": t.proxy(renames["DependencyEdgeOut"]).optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechOut"]).optional(),
            "lemma": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenOut"])
    types["AnnotateTextRequestIn"] = t.struct(
        {
            "features": t.proxy(renames["FeaturesIn"]),
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnnotateTextRequestIn"])
    types["AnnotateTextRequestOut"] = t.struct(
        {
            "features": t.proxy(renames["FeaturesOut"]),
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextRequestOut"])
    types["SentimentIn"] = t.struct(
        {"score": t.number().optional(), "magnitude": t.number().optional()}
    ).named(renames["SentimentIn"])
    types["SentimentOut"] = t.struct(
        {
            "score": t.number().optional(),
            "magnitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SentimentOut"])
    types["AnalyzeSyntaxResponseIn"] = t.struct(
        {
            "language": t.string().optional(),
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseIn"])
    types["AnalyzeSyntaxResponseOut"] = t.struct(
        {
            "language": t.string().optional(),
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseOut"])
    types["AnalyzeSentimentRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnalyzeSentimentRequestIn"])
    types["AnalyzeSentimentRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSentimentRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AnalyzeEntitySentimentResponseIn"] = t.struct(
        {
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
        }
    ).named(renames["AnalyzeEntitySentimentResponseIn"])
    types["AnalyzeEntitySentimentResponseOut"] = t.struct(
        {
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitySentimentResponseOut"])
    types["AnalyzeSyntaxRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnalyzeSyntaxRequestIn"])
    types["AnalyzeSyntaxRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSyntaxRequestOut"])
    types["V2ModelIn"] = t.struct(
        {"contentCategoriesVersion": t.string().optional()}
    ).named(renames["V2ModelIn"])
    types["V2ModelOut"] = t.struct(
        {
            "contentCategoriesVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ModelOut"])
    types["TextSpanIn"] = t.struct(
        {"beginOffset": t.integer().optional(), "content": t.string().optional()}
    ).named(renames["TextSpanIn"])
    types["TextSpanOut"] = t.struct(
        {
            "beginOffset": t.integer().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextSpanOut"])
    types["ClassificationModelOptionsIn"] = t.struct(
        {
            "v1Model": t.proxy(renames["V1ModelIn"]).optional(),
            "v2Model": t.proxy(renames["V2ModelIn"]).optional(),
        }
    ).named(renames["ClassificationModelOptionsIn"])
    types["ClassificationModelOptionsOut"] = t.struct(
        {
            "v1Model": t.proxy(renames["V1ModelOut"]).optional(),
            "v2Model": t.proxy(renames["V2ModelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassificationModelOptionsOut"])
    types["AnnotateTextResponseIn"] = t.struct(
        {
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryIn"])
            ).optional(),
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
        }
    ).named(renames["AnnotateTextResponseIn"])
    types["AnnotateTextResponseOut"] = t.struct(
        {
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextResponseOut"])
    types["AnalyzeSentimentResponseIn"] = t.struct(
        {
            "language": t.string().optional(),
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
        }
    ).named(renames["AnalyzeSentimentResponseIn"])
    types["AnalyzeSentimentResponseOut"] = t.struct(
        {
            "language": t.string().optional(),
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSentimentResponseOut"])
    types["DocumentIn"] = t.struct(
        {
            "gcsContentUri": t.string().optional(),
            "language": t.string().optional(),
            "content": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "gcsContentUri": t.string().optional(),
            "language": t.string().optional(),
            "content": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
    types["AnalyzeEntitySentimentRequestIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]),
            "encodingType": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitySentimentRequestIn"])
    types["AnalyzeEntitySentimentRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "encodingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitySentimentRequestOut"])
    types["ClassifyTextResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["ClassificationCategoryIn"])).optional()}
    ).named(renames["ClassifyTextResponseIn"])
    types["ClassifyTextResponseOut"] = t.struct(
        {
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassifyTextResponseOut"])
    types["DependencyEdgeIn"] = t.struct(
        {"label": t.string().optional(), "headTokenIndex": t.integer().optional()}
    ).named(renames["DependencyEdgeIn"])
    types["DependencyEdgeOut"] = t.struct(
        {
            "label": t.string().optional(),
            "headTokenIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DependencyEdgeOut"])
    types["ClassifyTextRequestIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsIn"]
            ).optional(),
        }
    ).named(renames["ClassifyTextRequestIn"])
    types["ClassifyTextRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassifyTextRequestOut"])
    types["EntityIn"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionIn"])).optional(),
            "salience": t.number().optional(),
            "name": t.string().optional(),
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionOut"])).optional(),
            "salience": t.number().optional(),
            "name": t.string().optional(),
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["SentenceIn"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
        }
    ).named(renames["SentenceIn"])
    types["SentenceOut"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SentenceOut"])
    types["V1ModelIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1ModelIn"]
    )
    types["V1ModelOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1ModelOut"])
    types["AnalyzeEntitiesResponseIn"] = t.struct(
        {
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseIn"])
    types["AnalyzeEntitiesResponseOut"] = t.struct(
        {
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseOut"])
    types["FeaturesIn"] = t.struct(
        {
            "extractDocumentSentiment": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
            "extractSyntax": t.boolean().optional(),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsIn"]
            ).optional(),
            "extractEntitySentiment": t.boolean().optional(),
            "classifyText": t.boolean().optional(),
        }
    ).named(renames["FeaturesIn"])
    types["FeaturesOut"] = t.struct(
        {
            "extractDocumentSentiment": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
            "extractSyntax": t.boolean().optional(),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsOut"]
            ).optional(),
            "extractEntitySentiment": t.boolean().optional(),
            "classifyText": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeaturesOut"])
    types["EntityMentionIn"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["EntityMentionIn"])
    types["EntityMentionOut"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionOut"])
    types["ClassificationCategoryIn"] = t.struct(
        {"confidence": t.number().optional(), "name": t.string().optional()}
    ).named(renames["ClassificationCategoryIn"])
    types["ClassificationCategoryOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassificationCategoryOut"])
    types["PartOfSpeechIn"] = t.struct(
        {
            "number": t.string().optional(),
            "tense": t.string().optional(),
            "mood": t.string().optional(),
            "reciprocity": t.string().optional(),
            "aspect": t.string().optional(),
            "proper": t.string().optional(),
            "voice": t.string().optional(),
            "form": t.string().optional(),
            "person": t.string().optional(),
            "tag": t.string().optional(),
            "case": t.string().optional(),
            "gender": t.string().optional(),
        }
    ).named(renames["PartOfSpeechIn"])
    types["PartOfSpeechOut"] = t.struct(
        {
            "number": t.string().optional(),
            "tense": t.string().optional(),
            "mood": t.string().optional(),
            "reciprocity": t.string().optional(),
            "aspect": t.string().optional(),
            "proper": t.string().optional(),
            "voice": t.string().optional(),
            "form": t.string().optional(),
            "person": t.string().optional(),
            "tag": t.string().optional(),
            "case": t.string().optional(),
            "gender": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartOfSpeechOut"])

    functions = {}
    functions["documentsAnalyzeSentiment"] = language.post(
        "v1/documents:annotateText",
        t.struct(
            {
                "features": t.proxy(renames["FeaturesIn"]),
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsClassifyText"] = language.post(
        "v1/documents:annotateText",
        t.struct(
            {
                "features": t.proxy(renames["FeaturesIn"]),
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeEntitySentiment"] = language.post(
        "v1/documents:annotateText",
        t.struct(
            {
                "features": t.proxy(renames["FeaturesIn"]),
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeSyntax"] = language.post(
        "v1/documents:annotateText",
        t.struct(
            {
                "features": t.proxy(renames["FeaturesIn"]),
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeEntities"] = language.post(
        "v1/documents:annotateText",
        t.struct(
            {
                "features": t.proxy(renames["FeaturesIn"]),
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnnotateText"] = language.post(
        "v1/documents:annotateText",
        t.struct(
            {
                "features": t.proxy(renames["FeaturesIn"]),
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnnotateTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="language", renames=renames, types=types, functions=functions
    )
