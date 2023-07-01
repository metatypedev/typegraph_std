from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_language():
    language = HTTPRuntime("https://language.googleapis.com/")

    renames = {
        "ErrorResponse": "_language_1_ErrorResponse",
        "AnalyzeSentimentResponseIn": "_language_2_AnalyzeSentimentResponseIn",
        "AnalyzeSentimentResponseOut": "_language_3_AnalyzeSentimentResponseOut",
        "ClassifyTextResponseIn": "_language_4_ClassifyTextResponseIn",
        "ClassifyTextResponseOut": "_language_5_ClassifyTextResponseOut",
        "FeaturesIn": "_language_6_FeaturesIn",
        "FeaturesOut": "_language_7_FeaturesOut",
        "TokenIn": "_language_8_TokenIn",
        "TokenOut": "_language_9_TokenOut",
        "AnalyzeEntitySentimentResponseIn": "_language_10_AnalyzeEntitySentimentResponseIn",
        "AnalyzeEntitySentimentResponseOut": "_language_11_AnalyzeEntitySentimentResponseOut",
        "SentenceIn": "_language_12_SentenceIn",
        "SentenceOut": "_language_13_SentenceOut",
        "AnalyzeEntitySentimentRequestIn": "_language_14_AnalyzeEntitySentimentRequestIn",
        "AnalyzeEntitySentimentRequestOut": "_language_15_AnalyzeEntitySentimentRequestOut",
        "SentimentIn": "_language_16_SentimentIn",
        "SentimentOut": "_language_17_SentimentOut",
        "TextSpanIn": "_language_18_TextSpanIn",
        "TextSpanOut": "_language_19_TextSpanOut",
        "DependencyEdgeIn": "_language_20_DependencyEdgeIn",
        "DependencyEdgeOut": "_language_21_DependencyEdgeOut",
        "AnalyzeEntitiesResponseIn": "_language_22_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_language_23_AnalyzeEntitiesResponseOut",
        "ClassificationModelOptionsIn": "_language_24_ClassificationModelOptionsIn",
        "ClassificationModelOptionsOut": "_language_25_ClassificationModelOptionsOut",
        "StatusIn": "_language_26_StatusIn",
        "StatusOut": "_language_27_StatusOut",
        "ClassificationCategoryIn": "_language_28_ClassificationCategoryIn",
        "ClassificationCategoryOut": "_language_29_ClassificationCategoryOut",
        "AnalyzeSyntaxResponseIn": "_language_30_AnalyzeSyntaxResponseIn",
        "AnalyzeSyntaxResponseOut": "_language_31_AnalyzeSyntaxResponseOut",
        "EntityMentionIn": "_language_32_EntityMentionIn",
        "EntityMentionOut": "_language_33_EntityMentionOut",
        "ClassifyTextRequestIn": "_language_34_ClassifyTextRequestIn",
        "ClassifyTextRequestOut": "_language_35_ClassifyTextRequestOut",
        "EntityIn": "_language_36_EntityIn",
        "EntityOut": "_language_37_EntityOut",
        "DocumentIn": "_language_38_DocumentIn",
        "DocumentOut": "_language_39_DocumentOut",
        "AnalyzeEntitiesRequestIn": "_language_40_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_language_41_AnalyzeEntitiesRequestOut",
        "AnnotateTextRequestIn": "_language_42_AnnotateTextRequestIn",
        "AnnotateTextRequestOut": "_language_43_AnnotateTextRequestOut",
        "PartOfSpeechIn": "_language_44_PartOfSpeechIn",
        "PartOfSpeechOut": "_language_45_PartOfSpeechOut",
        "ModerateTextResponseIn": "_language_46_ModerateTextResponseIn",
        "ModerateTextResponseOut": "_language_47_ModerateTextResponseOut",
        "AnalyzeSyntaxRequestIn": "_language_48_AnalyzeSyntaxRequestIn",
        "AnalyzeSyntaxRequestOut": "_language_49_AnalyzeSyntaxRequestOut",
        "V2ModelIn": "_language_50_V2ModelIn",
        "V2ModelOut": "_language_51_V2ModelOut",
        "ModerateTextRequestIn": "_language_52_ModerateTextRequestIn",
        "ModerateTextRequestOut": "_language_53_ModerateTextRequestOut",
        "AnnotateTextResponseIn": "_language_54_AnnotateTextResponseIn",
        "AnnotateTextResponseOut": "_language_55_AnnotateTextResponseOut",
        "AnalyzeSentimentRequestIn": "_language_56_AnalyzeSentimentRequestIn",
        "AnalyzeSentimentRequestOut": "_language_57_AnalyzeSentimentRequestOut",
        "V1ModelIn": "_language_58_V1ModelIn",
        "V1ModelOut": "_language_59_V1ModelOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AnalyzeSentimentResponseIn"] = t.struct(
        {
            "language": t.string().optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
        }
    ).named(renames["AnalyzeSentimentResponseIn"])
    types["AnalyzeSentimentResponseOut"] = t.struct(
        {
            "language": t.string().optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSentimentResponseOut"])
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
    types["FeaturesIn"] = t.struct(
        {
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsIn"]
            ).optional(),
            "classifyText": t.boolean().optional(),
            "moderateText": t.boolean().optional(),
            "extractSyntax": t.boolean().optional(),
            "extractEntitySentiment": t.boolean().optional(),
            "extractDocumentSentiment": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
        }
    ).named(renames["FeaturesIn"])
    types["FeaturesOut"] = t.struct(
        {
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsOut"]
            ).optional(),
            "classifyText": t.boolean().optional(),
            "moderateText": t.boolean().optional(),
            "extractSyntax": t.boolean().optional(),
            "extractEntitySentiment": t.boolean().optional(),
            "extractDocumentSentiment": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeaturesOut"])
    types["TokenIn"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "dependencyEdge": t.proxy(renames["DependencyEdgeIn"]).optional(),
            "lemma": t.string().optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechIn"]).optional(),
        }
    ).named(renames["TokenIn"])
    types["TokenOut"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "dependencyEdge": t.proxy(renames["DependencyEdgeOut"]).optional(),
            "lemma": t.string().optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenOut"])
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
    types["SentimentIn"] = t.struct(
        {"magnitude": t.number().optional(), "score": t.number().optional()}
    ).named(renames["SentimentIn"])
    types["SentimentOut"] = t.struct(
        {
            "magnitude": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SentimentOut"])
    types["TextSpanIn"] = t.struct(
        {"content": t.string().optional(), "beginOffset": t.integer().optional()}
    ).named(renames["TextSpanIn"])
    types["TextSpanOut"] = t.struct(
        {
            "content": t.string().optional(),
            "beginOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextSpanOut"])
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
    types["AnalyzeSyntaxResponseIn"] = t.struct(
        {
            "language": t.string().optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseIn"])
    types["AnalyzeSyntaxResponseOut"] = t.struct(
        {
            "language": t.string().optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseOut"])
    types["EntityMentionIn"] = t.struct(
        {
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
            "type": t.string().optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
        }
    ).named(renames["EntityMentionIn"])
    types["EntityMentionOut"] = t.struct(
        {
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "type": t.string().optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionOut"])
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
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionIn"])).optional(),
            "name": t.string().optional(),
            "salience": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "type": t.string().optional(),
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionOut"])).optional(),
            "name": t.string().optional(),
            "salience": t.number().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["DocumentIn"] = t.struct(
        {
            "content": t.string().optional(),
            "type": t.string(),
            "language": t.string().optional(),
            "gcsContentUri": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "content": t.string().optional(),
            "type": t.string(),
            "language": t.string().optional(),
            "gcsContentUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
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
    types["AnnotateTextRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "features": t.proxy(renames["FeaturesIn"]),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnnotateTextRequestIn"])
    types["AnnotateTextRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "features": t.proxy(renames["FeaturesOut"]),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextRequestOut"])
    types["PartOfSpeechIn"] = t.struct(
        {
            "voice": t.string().optional(),
            "reciprocity": t.string().optional(),
            "case": t.string().optional(),
            "gender": t.string().optional(),
            "tense": t.string().optional(),
            "tag": t.string().optional(),
            "mood": t.string().optional(),
            "form": t.string().optional(),
            "aspect": t.string().optional(),
            "person": t.string().optional(),
            "proper": t.string().optional(),
            "number": t.string().optional(),
        }
    ).named(renames["PartOfSpeechIn"])
    types["PartOfSpeechOut"] = t.struct(
        {
            "voice": t.string().optional(),
            "reciprocity": t.string().optional(),
            "case": t.string().optional(),
            "gender": t.string().optional(),
            "tense": t.string().optional(),
            "tag": t.string().optional(),
            "mood": t.string().optional(),
            "form": t.string().optional(),
            "aspect": t.string().optional(),
            "person": t.string().optional(),
            "proper": t.string().optional(),
            "number": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartOfSpeechOut"])
    types["ModerateTextResponseIn"] = t.struct(
        {
            "moderationCategories": t.array(
                t.proxy(renames["ClassificationCategoryIn"])
            ).optional()
        }
    ).named(renames["ModerateTextResponseIn"])
    types["ModerateTextResponseOut"] = t.struct(
        {
            "moderationCategories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModerateTextResponseOut"])
    types["AnalyzeSyntaxRequestIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]),
            "encodingType": t.string().optional(),
        }
    ).named(renames["AnalyzeSyntaxRequestIn"])
    types["AnalyzeSyntaxRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "encodingType": t.string().optional(),
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
    types["ModerateTextRequestIn"] = t.struct(
        {"document": t.proxy(renames["DocumentIn"])}
    ).named(renames["ModerateTextRequestIn"])
    types["ModerateTextRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModerateTextRequestOut"])
    types["AnnotateTextResponseIn"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryIn"])
            ).optional(),
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
            "language": t.string().optional(),
            "moderationCategories": t.array(
                t.proxy(renames["ClassificationCategoryIn"])
            ).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
        }
    ).named(renames["AnnotateTextResponseIn"])
    types["AnnotateTextResponseOut"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "language": t.string().optional(),
            "moderationCategories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextResponseOut"])
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
    types["V1ModelIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1ModelIn"]
    )
    types["V1ModelOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1ModelOut"])

    functions = {}
    functions["documentsAnalyzeEntitySentiment"] = language.post(
        "v1/documents:analyzeEntities",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsModerateText"] = language.post(
        "v1/documents:analyzeEntities",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsClassifyText"] = language.post(
        "v1/documents:analyzeEntities",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeSyntax"] = language.post(
        "v1/documents:analyzeEntities",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnnotateText"] = language.post(
        "v1/documents:analyzeEntities",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeSentiment"] = language.post(
        "v1/documents:analyzeEntities",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeEntities"] = language.post(
        "v1/documents:analyzeEntities",
        t.struct(
            {
                "encodingType": t.string().optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzeEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="language", renames=renames, types=Box(types), functions=Box(functions)
    )
