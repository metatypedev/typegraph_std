from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_language() -> Import:
    language = HTTPRuntime("https://language.googleapis.com/")

    renames = {
        "ErrorResponse": "_language_1_ErrorResponse",
        "TokenIn": "_language_2_TokenIn",
        "TokenOut": "_language_3_TokenOut",
        "AnalyzeEntitiesRequestIn": "_language_4_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_language_5_AnalyzeEntitiesRequestOut",
        "AnalyzeEntitiesResponseIn": "_language_6_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_language_7_AnalyzeEntitiesResponseOut",
        "EntityMentionIn": "_language_8_EntityMentionIn",
        "EntityMentionOut": "_language_9_EntityMentionOut",
        "ClassificationCategoryIn": "_language_10_ClassificationCategoryIn",
        "ClassificationCategoryOut": "_language_11_ClassificationCategoryOut",
        "AnalyzeEntitySentimentResponseIn": "_language_12_AnalyzeEntitySentimentResponseIn",
        "AnalyzeEntitySentimentResponseOut": "_language_13_AnalyzeEntitySentimentResponseOut",
        "AnalyzeSentimentResponseIn": "_language_14_AnalyzeSentimentResponseIn",
        "AnalyzeSentimentResponseOut": "_language_15_AnalyzeSentimentResponseOut",
        "TextSpanIn": "_language_16_TextSpanIn",
        "TextSpanOut": "_language_17_TextSpanOut",
        "V1ModelIn": "_language_18_V1ModelIn",
        "V1ModelOut": "_language_19_V1ModelOut",
        "AnnotateTextRequestIn": "_language_20_AnnotateTextRequestIn",
        "AnnotateTextRequestOut": "_language_21_AnnotateTextRequestOut",
        "V2ModelIn": "_language_22_V2ModelIn",
        "V2ModelOut": "_language_23_V2ModelOut",
        "AnalyzeEntitySentimentRequestIn": "_language_24_AnalyzeEntitySentimentRequestIn",
        "AnalyzeEntitySentimentRequestOut": "_language_25_AnalyzeEntitySentimentRequestOut",
        "DependencyEdgeIn": "_language_26_DependencyEdgeIn",
        "DependencyEdgeOut": "_language_27_DependencyEdgeOut",
        "PartOfSpeechIn": "_language_28_PartOfSpeechIn",
        "PartOfSpeechOut": "_language_29_PartOfSpeechOut",
        "SentimentIn": "_language_30_SentimentIn",
        "SentimentOut": "_language_31_SentimentOut",
        "FeaturesIn": "_language_32_FeaturesIn",
        "FeaturesOut": "_language_33_FeaturesOut",
        "StatusIn": "_language_34_StatusIn",
        "StatusOut": "_language_35_StatusOut",
        "AnalyzeSyntaxResponseIn": "_language_36_AnalyzeSyntaxResponseIn",
        "AnalyzeSyntaxResponseOut": "_language_37_AnalyzeSyntaxResponseOut",
        "ClassifyTextResponseIn": "_language_38_ClassifyTextResponseIn",
        "ClassifyTextResponseOut": "_language_39_ClassifyTextResponseOut",
        "AnnotateTextResponseIn": "_language_40_AnnotateTextResponseIn",
        "AnnotateTextResponseOut": "_language_41_AnnotateTextResponseOut",
        "AnalyzeSyntaxRequestIn": "_language_42_AnalyzeSyntaxRequestIn",
        "AnalyzeSyntaxRequestOut": "_language_43_AnalyzeSyntaxRequestOut",
        "DocumentIn": "_language_44_DocumentIn",
        "DocumentOut": "_language_45_DocumentOut",
        "AnalyzeSentimentRequestIn": "_language_46_AnalyzeSentimentRequestIn",
        "AnalyzeSentimentRequestOut": "_language_47_AnalyzeSentimentRequestOut",
        "ClassifyTextRequestIn": "_language_48_ClassifyTextRequestIn",
        "ClassifyTextRequestOut": "_language_49_ClassifyTextRequestOut",
        "EntityIn": "_language_50_EntityIn",
        "EntityOut": "_language_51_EntityOut",
        "ClassificationModelOptionsIn": "_language_52_ClassificationModelOptionsIn",
        "ClassificationModelOptionsOut": "_language_53_ClassificationModelOptionsOut",
        "SentenceIn": "_language_54_SentenceIn",
        "SentenceOut": "_language_55_SentenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TokenIn"] = t.struct(
        {
            "dependencyEdge": t.proxy(renames["DependencyEdgeIn"]).optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechIn"]).optional(),
            "lemma": t.string().optional(),
        }
    ).named(renames["TokenIn"])
    types["TokenOut"] = t.struct(
        {
            "dependencyEdge": t.proxy(renames["DependencyEdgeOut"]).optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechOut"]).optional(),
            "lemma": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenOut"])
    types["AnalyzeEntitiesRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnalyzeEntitiesRequestIn"])
    types["AnalyzeEntitiesRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestOut"])
    types["AnalyzeEntitiesResponseIn"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseIn"])
    types["AnalyzeEntitiesResponseOut"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseOut"])
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
        {"name": t.string().optional(), "confidence": t.number().optional()}
    ).named(renames["ClassificationCategoryIn"])
    types["ClassificationCategoryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "confidence": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassificationCategoryOut"])
    types["AnalyzeEntitySentimentResponseIn"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitySentimentResponseIn"])
    types["AnalyzeEntitySentimentResponseOut"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitySentimentResponseOut"])
    types["AnalyzeSentimentResponseIn"] = t.struct(
        {
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["AnalyzeSentimentResponseIn"])
    types["AnalyzeSentimentResponseOut"] = t.struct(
        {
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSentimentResponseOut"])
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
    types["V1ModelIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1ModelIn"]
    )
    types["V1ModelOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1ModelOut"])
    types["AnnotateTextRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
            "features": t.proxy(renames["FeaturesIn"]),
        }
    ).named(renames["AnnotateTextRequestIn"])
    types["AnnotateTextRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "features": t.proxy(renames["FeaturesOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextRequestOut"])
    types["V2ModelIn"] = t.struct(
        {"contentCategoriesVersion": t.string().optional()}
    ).named(renames["V2ModelIn"])
    types["V2ModelOut"] = t.struct(
        {
            "contentCategoriesVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ModelOut"])
    types["AnalyzeEntitySentimentRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnalyzeEntitySentimentRequestIn"])
    types["AnalyzeEntitySentimentRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitySentimentRequestOut"])
    types["DependencyEdgeIn"] = t.struct(
        {"headTokenIndex": t.integer().optional(), "label": t.string().optional()}
    ).named(renames["DependencyEdgeIn"])
    types["DependencyEdgeOut"] = t.struct(
        {
            "headTokenIndex": t.integer().optional(),
            "label": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DependencyEdgeOut"])
    types["PartOfSpeechIn"] = t.struct(
        {
            "gender": t.string().optional(),
            "voice": t.string().optional(),
            "case": t.string().optional(),
            "tag": t.string().optional(),
            "tense": t.string().optional(),
            "form": t.string().optional(),
            "aspect": t.string().optional(),
            "proper": t.string().optional(),
            "person": t.string().optional(),
            "reciprocity": t.string().optional(),
            "mood": t.string().optional(),
            "number": t.string().optional(),
        }
    ).named(renames["PartOfSpeechIn"])
    types["PartOfSpeechOut"] = t.struct(
        {
            "gender": t.string().optional(),
            "voice": t.string().optional(),
            "case": t.string().optional(),
            "tag": t.string().optional(),
            "tense": t.string().optional(),
            "form": t.string().optional(),
            "aspect": t.string().optional(),
            "proper": t.string().optional(),
            "person": t.string().optional(),
            "reciprocity": t.string().optional(),
            "mood": t.string().optional(),
            "number": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartOfSpeechOut"])
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
    types["FeaturesIn"] = t.struct(
        {
            "classifyText": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsIn"]
            ).optional(),
            "extractSyntax": t.boolean().optional(),
            "extractEntitySentiment": t.boolean().optional(),
            "extractDocumentSentiment": t.boolean().optional(),
        }
    ).named(renames["FeaturesIn"])
    types["FeaturesOut"] = t.struct(
        {
            "classifyText": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsOut"]
            ).optional(),
            "extractSyntax": t.boolean().optional(),
            "extractEntitySentiment": t.boolean().optional(),
            "extractDocumentSentiment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeaturesOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AnalyzeSyntaxResponseIn"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseIn"])
    types["AnalyzeSyntaxResponseOut"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseOut"])
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
    types["AnnotateTextResponseIn"] = t.struct(
        {
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryIn"])
            ).optional(),
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
        }
    ).named(renames["AnnotateTextResponseIn"])
    types["AnnotateTextResponseOut"] = t.struct(
        {
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextResponseOut"])
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
    types["DocumentIn"] = t.struct(
        {
            "type": t.string(),
            "language": t.string().optional(),
            "gcsContentUri": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "type": t.string(),
            "language": t.string().optional(),
            "gcsContentUri": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
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
    types["ClassifyTextRequestIn"] = t.struct(
        {
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsIn"]
            ).optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["ClassifyTextRequestIn"])
    types["ClassifyTextRequestOut"] = t.struct(
        {
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsOut"]
            ).optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassifyTextRequestOut"])
    types["EntityIn"] = t.struct(
        {
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
            "salience": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionIn"])).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "salience": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionOut"])).optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["ClassificationModelOptionsIn"] = t.struct(
        {
            "v2Model": t.proxy(renames["V2ModelIn"]).optional(),
            "v1Model": t.proxy(renames["V1ModelIn"]).optional(),
        }
    ).named(renames["ClassificationModelOptionsIn"])
    types["ClassificationModelOptionsOut"] = t.struct(
        {
            "v2Model": t.proxy(renames["V2ModelOut"]).optional(),
            "v1Model": t.proxy(renames["V1ModelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassificationModelOptionsOut"])
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

    functions = {}
    functions["documentsAnalyzeSyntax"] = language.post(
        "v1/documents:analyzeSentiment",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeSentimentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsClassifyText"] = language.post(
        "v1/documents:analyzeSentiment",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeSentimentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnnotateText"] = language.post(
        "v1/documents:analyzeSentiment",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeSentimentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeEntitySentiment"] = language.post(
        "v1/documents:analyzeSentiment",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeSentimentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeEntities"] = language.post(
        "v1/documents:analyzeSentiment",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeSentimentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeSentiment"] = language.post(
        "v1/documents:analyzeSentiment",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeSentimentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="language", renames=renames, types=Box(types), functions=Box(functions)
    )
